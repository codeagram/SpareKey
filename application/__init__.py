from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


from config import ProdConfig, DevConfig


if app.config["ENV"] == "production":
    app.config.from_object(ProdConfig)

else:
    app.config.from_object(DevConfig)


with app.app_context():

    db = SQLAlchemy(app)


    from application.spare_key import SpareKey
    from application.auth import AuthBP


    app.register_blueprint(SpareKeyBP)
    app.register_blueprint(AuthBP

    db.create_all()
