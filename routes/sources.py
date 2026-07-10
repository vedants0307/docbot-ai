from flask import Blueprint
from flask import jsonify

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
def list_sources():

    return jsonify(

        rag_service.list_sources()

    )


# ---------------------------------
# Documents Only
# ---------------------------------

@sources_bp.route("/documents")
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