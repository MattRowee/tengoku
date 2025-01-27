from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)

    # Register blueprints
    from app.routes.home_routes import home_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    return app