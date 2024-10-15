from flask import *
from chickoz.chatbot.chat import get_response

chatbot = Blueprint('chatbot', __name__, template_folder='templates', static_folder='static', static_url_path='/chatbot')


@chatbot.get("/")
def index_get():
    return render_template("base.html")


@chatbot.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)



