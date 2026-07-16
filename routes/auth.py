from flask import Blueprint
from flask import jsonify
from flask import request
from flask import render_template
from flask import make_response
from services.auth_service import auth_service


auth_bp = Blueprint(

    "auth",

    __name__,

    url_prefix="/auth"

)


# ---------------------------------
# Landing Page
# ---------------------------------

@auth_bp.route(
    "/",
    methods=["GET"]
)
def landing():

    return render_template(

        "auth/landing.html"

    )


# ---------------------------------
# Login Page
# ---------------------------------

@auth_bp.route(
    "/login",
    methods=["GET"]
)
def login_page():

    return render_template(

        "auth/login.html"

    )


# ---------------------------------
# Register Page
# ---------------------------------

@auth_bp.route(
    "/register",
    methods=["GET"]
)
def register_page():

    return render_template(

        "auth/register.html"

    )


@auth_bp.route(

    "/logout",

    methods=["POST"]

)
def logout():

    response = make_response(

        jsonify(

            {

                "success": True

            }

        )

    )

    response.delete_cookie(

        "access_token"

    )

    return response
# ---------------------------------
# Register API
# ---------------------------------

@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.get_json()

    if not data:

        return jsonify(

            {

                "success": False,

                "message": "Invalid Request."

            }

        ), 400

    name = data.get(

        "name"

    )

    email = data.get(

        "email"

    )

    password = data.get(

        "password"

    )

    if not name or not email or not password:

        return jsonify(

            {

                "success": False,

                "message": "All fields are required."

            }

        ), 400

    result = auth_service.register(

        name,

        email,

        password

    )

    status_code = 200

    if not result["success"]:

        status_code = 400

    return jsonify(

        result

    ), status_code


# ---------------------------------
# Login API
# ---------------------------------

@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    if not data:

        return jsonify(

            {

                "success": False,

                "message": "Invalid Request."

            }

        ), 400

    email = data.get(

        "email"

    )

    password = data.get(

        "password"

    )

    if not email or not password:

        return jsonify(

            {

                "success": False,

                "message": "Email and Password are required."

            }

        ), 400

    result = auth_service.login(

        email,

        password

    )

    status_code = 200

    if not result["success"]:

        status_code = 401

    if result["success"]:

        response = make_response(

            jsonify(result)

        )

        response.set_cookie(

            "access_token",

            result["token"],

            httponly=True,

            samesite="Lax",

            secure=False   # True after HTTPS deployment

        )

        return response

    return jsonify(result), status_code


