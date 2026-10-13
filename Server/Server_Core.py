from flask import Flask, jsonify, request, render_template
import psycopg

app_core = Flask(__name__)

connection = psycopg.connect(
    user="postgres",
    password='0208',
    host='db',
    port='5432',
    dbname='demo'
)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS data(
    username VARCHAR(15) UNIQUE NOT NULL,
    id INTEGER PRIMARY KEY NOT NULL
);""")
connection.commit()

@app_core.route('/create', methods=["POST"])
def Create_user():
    data = request.get_json() or {}

    name = data.get('name')
    user_id = data.get('id')
    if name and user_id:
        try:
            cursor.execute("""
                INSERT INTO data(username, id)
                VALUES (%s, %s);
            """, (name, user_id))
        
            connection.commit()
            return jsonify({'status': 'success', 'message': 'User created'})

        except psycopg.errors.UniqueViolation:
            connection.rollback()
            return jsonify({'status': 'error', 'message': 'User already exists'})
        except psycopg.errors.NotNullViolation:
            connection.rollback()
            return jsonify({'status': 'error', 'message': 'Fields cannot be null'})
    else:
        return jsonify({'status': 'error', 'message': 'Missing name or id'})


@app_core.route('/delete', methods=["DELETE"])
def Delete_user():
    data = request.get_json() or {}
    user_id = data.get('id')

    if not user_id:
        return jsonify({'status': 'error', 'message': 'Missing user id'}), 400

    try:
        cursor.execute("DELETE FROM data WHERE id = %s;", (user_id,))
        connection.commit()
        return jsonify({'status': 'success', 'message': f'User {user_id} deleted'})
    except Exception as e:
        connection.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    print('Starting the Server...')
    try:
        app_core.run(host='0.0.0.0', port=8000, debug=False)
    finally:
        cursor.close()
        connection.close()