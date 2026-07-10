from flask import Blueprint
from flask import render_template
from flask import jsonify

from services.dashboard_service import (
    dashboard_service
)

dashboard_bp = Blueprint(

    "dashboard",

    __name__,

    url_prefix="/dashboard"

)


# -----------------------------
# Dashboard Page
# -----------------------------

@dashboard_bp.route("/")
def dashboard():

    return render_template(

        "dashboard/index.html"

    )


# -----------------------------
# Dashboard Stats API
# -----------------------------

@dashboard_bp.route("/stats")
def dashboard_stats():

    return jsonify(

        dashboard_service.get_dashboard()

    )