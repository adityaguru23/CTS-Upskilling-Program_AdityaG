from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

mock_courses = []

@courses_bp.route('/', methods=['GET'])
def list_courses():
    return jsonify(mock_courses), 200

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()

    if not data or 'name' not in data or 'code' not in data or 'credits' not in data:
            return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    new_id = len(mock_courses) + 1
    new_course = {
        'id': new_id,
        'name': data['name'],
        'code': data['code'],
        'credits': int(data['credits'])
    }

    mock_courses.append(new_course)
    return jsonify({'status': 'success', 'data': new_course}), 201