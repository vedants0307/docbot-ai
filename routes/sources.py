from flask import Blueprint
from flask import jsonify
from flask_jwt_extended import jwt_required
from services.rag_service import rag_service


sources_bp = Blueprint(

    "sources",

    __name__,

    url_prefix="/sources"

)


# ---------------------------------
# All Sources
# ---------------------------------

@sources_bp.route("/list")
@jwt_required()
def list_sources():

    return jsonify(

        rag_service.list_sources()

    )


# ---------------------------------
# Documents Only
# ---------------------------------

@sources_bp.route("/documents")
@jwt_required()
def document_sources():

    documents = []

    for source in rag_service.list_sources():

        if not source.startswith("http"):

            documents.append(

                source

            )

    return jsonify(

        documents

    )


# ---------------------------------
# Websites Only
# ---------------------------------

@sources_bp.route("/websites")
@jwt_required()
def website_sources():

    websites = []

    for source in rag_service.list_sources():

        if source.startswith("http"):

            websites.append(

                source

            )

    return jsonify(

        websites

    )