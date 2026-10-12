from flask import Flask, jsonify, request, render_template
import psycopg2

app_core = Flask(__name__)

connection = psycopg2.connect(
    user="postgres",
    password='0208',
    host='127.0.0.1',
    port='8120',
    database='demo'
)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS data(
    username VARCHAR(15) UNIQUE NOT NULL,
    id INTEGER PRIMARY KEY NOT NULL
);""")
connection.commit()

@app_core.route('/create', methods = ["POST"])
def Create_user():
    data = request.get_json() or {}

    name = data.get('name')
    id = data.get('id')

    if name and id:
        try:
            cursor.execute("""
                INSERT INTO data(username, id)
                VALUES (%s, %s);
            """, (name, id))
        
            connection.commit()
            return jsonify({'status' : 'success'})

        except psycopg2.errors.UniqueViolation:
            connection.rollback()
            return jsonify({'status' : 'error'})
        except psycopg2.errors.NotNullViolation:
            connection.rollback()
            return jsonify({'status' : 'error'})
    else:
        return jsonify({'status' : 'error'})

if __name__ == '__main__':
    print('Starting the Server...')
    try:
        app_core.run(host='127.0.0.1', port=8000, debug=False)
    finally:
        cursor.close()
        connection.close()