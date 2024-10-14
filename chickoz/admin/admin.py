from flask import *

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', static_url_path='/admin')


@admin.route('/')
def dash():
    return render_template('dashboard.html')


@admin.route('/user')
def user():
    return render_template('user.html')


@admin.route('/order')
def order():
    return render_template('order.html')


@admin.route('/current-order')
def current_order():
    return render_template('current-order.html')


@admin.route('/menu')
def menu():
    return render_template('category.html')


@admin.route('/add-category')
def add_category():
    return render_template('add-category.html')


@admin.route('/category')
def category():
    return render_template('category.html')


@admin.route('/transaction')
def transaction():
    return render_template('transcation-details.html')
