# handson_05/courses/routes.py
from flask import Blueprint, jsonify, request
from app import db
from .models import Course

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

@courses_bp.route('/', methods=['GET'])
def list_courses():
    # Fetch all records via the ORM and serialize to dictionaries
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses]), 200

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data or 'name' not in data or 'code' not in data or 'credits' not in data or 'department_id' not in data:
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=int(data['credits']),
        department_id=int(data['department_id'])
    )

    # Staging the transaction and saving to database
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'status': 'success', 'data': new_course.to_dict()}), 201