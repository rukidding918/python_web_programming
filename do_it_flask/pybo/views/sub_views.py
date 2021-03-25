from flask import Blueprint

bp = Blueprint('sub', __name__, url_prefix='/')

@bp.route('/yo')
def yo():
    return 'yo!'