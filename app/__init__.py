from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes.clubes import bp as clubes_bp
    app.register_blueprint(clubes_bp)

    with app.app_context():
        from app.models.clubes import db
        db.create_all()


    return app