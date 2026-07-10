from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from services.rag_service import rag_service


website_bp = Blueprint(

    "website",

    __name__,

    url_prefix="/website"

)


@website_bp.route("/")
def website():

    return render_template(

        "website/index.html"

    )


# -----------------------------------
# Index Website
# -----------------------------------

@website_bp.route(
    "/index",
    methods=["POST"]
)
def index_website():

    print("===== WEBSITE INDEX REQUEST =====")

    data = request.get_json()

    print(data)

    url = data.get("url")

    print("URL:", url)

    if not url:

        return jsonify({
            "success": False,
            "message": "Website URL is required."
        }), 400

    print("Starting crawl...")

    chunks = rag_service.upload_website(url)

    print("Finished crawling")

    print("Chunks:", chunks)

    return jsonify({

        "success": True,

        "message": "Website Indexed Successfully.",

        "chunks": chunks

    })


# -----------------------------------
# List Websites
# -----------------------------------

@website_bp.route("/list")
def list_websites():

    sources = rag_service.list_sources()

    websites = []

    for source in sources:

        if source.startswith("http"):

            websites.append(

                source

            )

    return jsonify(

        websites

    )


# -----------------------------------
# Delete Website
# -----------------------------------

@website_bp.route(

    "/delete",

    methods=["DELETE"]

)
def delete_website():

    data = request.get_json()

    url = data.get(

        "url"

    )

    results = rag_service.vectorstore.get(

        where={

            "source":url

        }

    )

    ids = results.get(

        "ids",

        []

    )

    if ids:

        rag_service.vectorstore.delete(

            ids=ids

        )

    return jsonify(

        {

            "success":True

        }

    )