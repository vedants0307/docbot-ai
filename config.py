import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "docbot-secret-key"
    )

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "docbot-jwt-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "uploads"

    EMBEDDING_FOLDER = "embeddings"