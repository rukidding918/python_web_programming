from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint(name='main', import_name=__name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello, pybo.'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.errorhandler(404)
def page_not_found(error):
    return 'hello! I love you!'