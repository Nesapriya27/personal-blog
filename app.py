from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Welcome to the Blog API!"
@app.route("/posts", methods=["GET"])
def get_posts():
    posts = BlogPost.query.all()
    return jsonify([{"id": post.id, "title": post.title, "content": post.content} for post in posts])
@app.route("/create_sample_data")
def create_sample_data():
    post1 = BlogPost(title="First Post", content="This is the content of the first post.")
    post2 = BlogPost(title="Second Post", content="This is the content of the second post.")
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return "Sample data created!"
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()  # Parse the JSON payload
    new_post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!", "post": {"id": new_post.id, "title": new_post.title, "content": new_post.content}}), 201

@app.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    post = BlogPost.query.get(id)
    if post is None:
        return jsonify({"message": "Post not found"}), 404
    return jsonify({"id": post.id, "title": post.title, "content": post.content})

@app.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    post = BlogPost.query.get(id)
    if post is None:
        return jsonify({"message": "Post not found"}), 404
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({"message": "Post updated successfully!", "post": {"id": post.id, "title": post.title, "content": post.content}})

@app.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    post = BlogPost.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Post deleted successfully"})
    else:
        return jsonify({"message": "Post not found"}), 404




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

