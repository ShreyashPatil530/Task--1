from flask import Blueprint, request, jsonify
from app import db
from models import Task, Comment

bp = Blueprint('bp', __name__)

# Create a comment (FIXED: Only inserts once)
@bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def create_comment(task_id):
    data = request.json
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    comment = Comment(content=data['content'], task_id=task_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify(comment.to_dict()), 201


# Get comments for a task
@bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([c.to_dict() for c in comments]), 200


# Update a comment
@bp.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    comment.content = data["content"]
    db.session.commit()

    return jsonify(comment.to_dict()), 200


# Delete a comment
@bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted"}), 200
