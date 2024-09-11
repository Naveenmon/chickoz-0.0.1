from flask import *

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', static_url_path='/admin')

#from admin.route import *
