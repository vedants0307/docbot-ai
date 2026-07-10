from flask_jwt_extended import create_access_token

from extensions import bcrypt

from models.user import User

from extensions import db


class AuthService:

    # -----------------------------
    # Register User
    # -----------------------------

    def register(

        self,

        name,

        email,

        password

    ):

        existing_user = User.query.filter_by(

            email=email

        ).first()

        if existing_user:

            return {

                "success": False,

                "message": "Email already exists."

            }

        password_hash = bcrypt.generate_password_hash(

            password

        ).decode("utf-8")

        user = User(

            name=name,

            email=email,

            password_hash=password_hash

        )

        db.session.add(

            user

        )

        db.session.commit()

        return {

            "success": True,

            "message": "Registration Successful."

        }

    # -----------------------------
    # Login User
    # -----------------------------

    def login(

        self,

        email,

        password

    ):

        user = User.query.filter_by(

            email=email

        ).first()

        if not user:

            return {

                "success": False,

                "message": "Invalid Email or Password."

            }

        if not bcrypt.check_password_hash(

            user.password_hash,

            password

        ):

            return {

                "success": False,

                "message": "Invalid Email or Password."

            }

        access_token = create_access_token(

            identity=str(user.id),   # use string for compatibility
            additional_claims={

                "name": user.name,

                "email": user.email

            }

        )

        return {

            "success": True,

            "token": access_token,

            "user": {

                "id": user.id,

                "name": user.name,

                "email": user.email

            }

        }


auth_service = AuthService()