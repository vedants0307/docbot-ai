from flask import Blueprint
from flask import request
from flask import jsonify

from services.rag_service import rag_service


chat_bp = Blueprint(

    "chat",

    __name__,

    url_prefix="/chat"

)


@chat_bp.route(
    "/send_message",
    methods=["POST"]
)
def send_message():

    data = request.get_json()

    question = data.get(

        "question"

    )

    scope = data.get(

        "scope",

        "global"

    )

    result = rag_service.ask_question(

        question,

        scope

    )

    sources = []

    seen = set()

    for doc in result["sources"]:

        metadata = doc.metadata

        source = {

            "source": metadata.get(

                "source",

                "Unknown"

            ),

            "type": metadata.get(

                "type",

                "document"

            ),

            "page": metadata.get(

                "page"

            ),

            "title": metadata.get(

                "title",

                ""

            )

        }

        key = (

            source["source"],

            source["page"]

        )

        if key not in seen:

            seen.add(

                key

            )

            sources.append(

                source

            )

    return jsonify(

        {

            "answer": result["answer"],

            "sources": sources

        }

    )