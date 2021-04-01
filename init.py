import logging
from flask import Flask

from config import CONFIG
from models import db

from handlers.authentication_handler import AUTHENTICATION
from handlers.ornament_handler import ORNAMENT
from handlers.category_handler import CATEGORY
from handlers.cart_handler import CART

logging.basicConfig(
    format='%(levelname)-8s %(asctime)s,%(msecs)d  [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO
)

def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    app.register_blueprint(ORNAMENT)
    app.register_blueprint(CATEGORY)
    app.register_blueprint(CART)
    app.register_blueprint(AUTHENTICATION)

    return app

