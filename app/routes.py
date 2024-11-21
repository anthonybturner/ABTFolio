from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/api/portfolio')
def portfolio():
    # Return some example data
    return jsonify({"projects": ["Project 1", "Project 2", "Project 3"]})
