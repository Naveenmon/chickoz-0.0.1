from flask import *
from admin.admin import admin


@admin.route('/')
def dash():
    return render_template('dashboard.html')


@admin.route('/a')
def eitem():
    return render_template('user.html')


@admin.route('/editorders')
def eorders():
    return render_template('editorders.html')


@admin.route('/edittrans')
def etrans():
    return render_template('edittransaction.html')


@admin.route('/editusers')
def eusers():
    return render_template('editusers.html')


@admin.route('/items')
def items():
    return render_template('items.html')


@admin.route('/orders')
def orders():
    return render_template('orders.html')


@admin.route('/transaction')
def transact():
    return render_template('transaction.html')


@admin.route('/users')
def users():
    return render_template('userlist.html')


@admin.route('/profile')
def profile():
    return "profile page"


@admin.route('/login')
def login():
    return "login page"
