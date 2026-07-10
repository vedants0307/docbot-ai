from flask import Flask
from flask import redirect

from config import Config

import models

from extensions import db
from extensions import migrate
from extensions import bcrypt
from extensions import jwt

from services.startup_service import startup_service

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.upload import upload_bp
from routes.website import website_bp
from routes.sources import sources_bp
from routes.chat import chat_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # -----------------------------
    # Initialize Extensions
    # -----------------------------

    db.init_app(app)

    migrate.init_app(

        app,

        db

    )

    bcrypt.init_app(

        app

    )

    jwt.init_app(

        app

    )

    # -----------------------------
    # Register Blueprints
    # -----------------------------

    app.register_blueprint(

        auth_bp

    )

    app.register_blueprint(

        dashboard_bp

    )

    app.register_blueprint(

        upload_bp

    )

    app.register_blueprint(

        website_bp

    )

    app.register_blueprint(

        sources_bp

    )

    app.register_blueprint(

        chat_bp

    )

    # -----------------------------
    # Startup Sync
    # -----------------------------

    with app.app_context():

        startup_service.sync_documents()

    # -----------------------------
    # Home Route
    # -----------------------------

    @app.route("/")
    def home():

        return redirect(

            "/auth/"

        )

    return app


app = create_app()


if __name__ == "__main__":

    app.run(

        debug=True

    )