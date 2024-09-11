from numpy.core.multiarray import result_type
from user.user import user
from flask import *
from flask_session import Session
from bson import ObjectId
from model import model


@user.route('/')
def index():
    return render_template('index.html')


@user.route('/about')
def about():
    return render_template('about.html')


@user.route('/menu')
def menu():
    return render_template('menu.html', l=model.menu(model))


@user.route('/signin')
def signin():
    return render_template('signin.html')


@user.route('/signup')
def signup():
    return render_template('signup.html')


@user.route('/order')
def order():
    return render_template('order.html')  # edhu simens da mathanu summa pooturuka


@user.route('/cart')
def cart():
    return render_template('cart.html')


@user.route('/checkout')
def checkout():
    return render_template('checkout.html')


@user.route('/payment')
def payment():
    return render_template('payment.html')


@user.route('/trackorder')
def trackorder():
    return render_template('ordertrack.html')


# signup function
@user.route('/signup/user', methods=['GET', 'POST'])
def user_signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        mobnum = request.form['mobnum']
        password = request.form['pass']
        cpassword = request.form['cpass']
        role = "user"
        if password == cpassword:
            if model.register(model, username, email, mobnum, password, role):
                flash("success", 'login')
                return redirect(url_for('user.signin'))
            else:
                flash("fail", 'login')
                return redirect(request.referrer)
        else:
            flash("fail", 'login')
            return redirect(request.referrer)
    return redirect(request.referrer)


# signin function
@user.route('/signin/user', methods=['GET', 'POST'])
def user_signin():
    if request.method == "POST":
        password = request.form['pass']
        email = request.form['email']
        result = model.login(model, email, password)
        if len(result) == 1:
            session["id"] = str(result[0]['_id'])
            session["name"] = result[0]['username'].upper()
            flash("success", 'success')
            return redirect(url_for('user.index'))
        else:
            flash("fail", 'login')
            return redirect(request.referrer)
    else:
        flash("fail", 'login')
        return redirect(request.referrer)


#logout
@user.route('/logout')
def logout():
    session['name'] = None
    session["id"] = None
    session.clear()
    return redirect(url_for('user.index'))


# addcart function
@user.route('/addcart/<string:id>', methods=['POST', 'GET'])
def addcart(id):
    if not session.get("name"):
        return redirect(request.referrer)
    else:
        size = request.form['size']
        qnt = request.form['qnt']
        r = model.cartcheck(model, session)
        if ObjectId(id) in r['cart']:
            return redirect(request.referrer)
        else:
            model.addcart(model, id, session, qnt)
            return redirect(request.referrer)


# removecart function
@user.route('/removecart/<string:id>')
def removecart(id):
    if not session.get("name"):
        return redirect(request.referrer)
    else:
        model.removecart(model, id, session)
        return redirect(request.referrer)
