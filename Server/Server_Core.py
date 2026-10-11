from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app_core = Flask(__name__)
app_core.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app_core.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app_core)

class Post_Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)

with app_core.app_context():
    db.create_all()

@app_core.route('/newpost', methods=["POST"])
def create_post():
    data = request.get_json()

    post_id = data.get('id')
    post_name = data.get('name', 'Template_Post-Name')

    find_post = Post_Creator.query.filter_by(id=post_id).first()
    
    if find_post:
        return jsonify(f'Post with id: {post_id} alredy exists!')

    new_post = Post_Creator(id=post_id, name=post_name)
    db.session.add(new_post)
    db.session.commit()
        
    return jsonify({
        "message": "SuccesFully created a post",
        "data": {
            "id": new_post.id,
            "name": new_post.name
        }
    }), 201

@app_core.route('/deletepost', methods=["DELETE"])
def delete_post():
    data = request.get_json()
    id = data.get('id')

    find_post_by_id = Post_Creator.query.filter_by(id=id).first()
    if find_post_by_id:
        db.session.delete(find_post_by_id)
        db.session.commit()

        return jsonify({
            "Answer-From-Server:" : "Succesfully deleted a post."
        })
    
    else:
        return jsonify(f'Error post not found: {id}')

@app_core.route('/getposts', methods = ["GET"])
def get_posts():
    find_all_posts = Post_Creator.query.all()

    result = [{'id' : post.id, 'name' : post.name} for post in find_all_posts]

    if result == []:
        return jsonify('0 Users...')
    else:
        return jsonify(f'result: {result}')

@app_core.route('/')
def main_page():
    return render_template('home.html', title = 'This is home page')

@app_core.route('/users')
def userslist():
    find_all_posts = Post_Creator.query.all()

    result = [{'id' : post.id, 'name' : post.name} for post in find_all_posts]

    if result == []:
        return render_template('home.html', title = '0 Users...')
    else:
        return render_template('home.html', title = f'result: {result}')


if __name__ == '__main__':
    app_core.run(host='127.0.0.1', port=8120, debug=False)
