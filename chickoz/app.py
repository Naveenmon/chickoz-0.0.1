from flask import *
from user.user import user
from admin.admin import admin
from flask_session import Session
from config import Config
from chickoz.chatbot.chatbot import chatbot

app = Flask(__name__, static_folder='static', static_url_path='/')
app.register_blueprint(user, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(chatbot, url_prefix="/chatbot")
app.config.from_object(Config)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
app.jinja_env.globals.update(zip=zip)
app.jinja_env.add_extension('jinja2.ext.do')
if __name__ == '__main__':
    app.secret_key = 'Chickoz039'
    app.run(debug=True, port=5000)
