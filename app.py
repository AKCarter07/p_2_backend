from flask import Flask
from flask_session import Session
from flask_cors import CORS
from controller.user_controller import uc
from controller.review_controller import rc
from controller.book_controller import bc




if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'hello'
    app.config['SESSION_TYPE'] = 'filesystem'
    # app.config['SECRET_KEY'] = 'hello'
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True

    app.register_blueprint(uc)
    app.register_blueprint(bc)
    app.register_blueprint(rc)

    CORS(app)
    Session(app)
    app.run(host="0.0.0.0", port=8080, debug=True)