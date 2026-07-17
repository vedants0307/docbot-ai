import os

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request
from flask_jwt_extended import jwt_required
from services.document_db_service import (
    document_db_service
)
from services.supabase_service import (

    upload_document,

    delete_document

)
from services.supabase_service import (

    upload_document as upload_to_supabase,

    delete_document as delete_from_supabase

)

from services.rag_service import (
    rag_service
)

upload_bp = Blueprint(

    "upload",

    __name__,

    url_prefix="/upload"

)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "..",
    "uploads"
)

UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

os.makedirs(

    UPLOAD_FOLDER,

    exist_ok=True

)


# -----------------------------------
# Upload Page
# -----------------------------------

@upload_bp.route("/")
@jwt_required()
def upload():

    return render_template(

        "upload/index.html"

    )


# -----------------------------------
# Upload Files
# -----------------------------------

@upload_bp.route(

    "/upload_files",

    methods=["POST"]

)
@jwt_required()
def upload_files():

    files = request.files.getlist(

        "files"

    )

    uploaded = []

    for file in files:

        if file.filename == "":

            continue

        file_path = os.path.join(

            UPLOAD_FOLDER,

            file.filename

        )

        file.save(

            file_path

        )

        upload_document(
            file_path,
            file.filename
        )

        print("Saved Path:", file_path)
        print("Exists:", os.path.exists(file_path))

        rag_service.delete_document(
            file.filename
        )

        chunks = rag_service.upload_document(

            file_path

        )

        document_db_service.add_document(

            filename=file.filename,

            chunks=chunks,

            file_size=os.path.getsize(

                file_path

            )

        )

        uploaded.append(

            {

                "filename": file.filename,

                "chunks": chunks

            }

        )

        if os.path.exists(
            file_path
        ):
            os.remove(
                file_path
            )

    return jsonify(

        {

            "success": True,

            "documents": uploaded

        }

    )


# -----------------------------------
# List Uploaded Documents
# -----------------------------------

@upload_bp.route(
    "/documents"
)
@jwt_required()
def documents():

    docs = document_db_service.list_documents()

    return jsonify(

        [

            doc.filename

            for doc in docs

        ]

    )


# -----------------------------------
# Delete Document
# -----------------------------------

@upload_bp.route(
    "/delete/<filename>",
    methods=["DELETE"]
)
@jwt_required()
def delete_document(filename):

    file_path = os.path.join(

        UPLOAD_FOLDER,

        filename

    )

    # Delete from Supabase Storage
    delete_from_supabase(

        filename

    )

    # Delete local temp file if present
    if os.path.exists(file_path):

        os.remove(file_path)

    # Delete embeddings
    deleted = rag_service.delete_document(

        filename

    )

    # Delete metadata
    document_db_service.delete_document(

        filename

    )

    return jsonify(

        {

            "success": True,

            "deleted_chunks": deleted

        }

    )