import os

from extensions import db

from models.document import Document


class DocumentDBService:

    def add_document(

        self,

        filename,

        chunks,

        file_size

    ):

        extension = os.path.splitext(

            filename

        )[1].replace(".", "")

        document = Document.query.filter_by(

            filename=filename

        ).first()

        if document:

            document.file_type = extension

            document.chunks = chunks

            document.file_size = round(

                file_size / (1024 * 1024),

                2

            )

        else:

            document = Document(

                filename=filename,

                file_type=extension,

                chunks=chunks,

                file_size=round(

                    file_size / (1024 * 1024),

                    2

                )

            )

            db.session.add(

                document

            )

        db.session.commit()

    # ------------------------------

    # List Documents

    # ------------------------------

    def list_documents(

        self

    ):

        return Document.query.order_by(

            Document.uploaded_at.desc()

        ).all()

    # ------------------------------

    # Delete

    # ------------------------------

    def delete_document(

        self,

        filename

    ):

        document = Document.query.filter_by(

            filename=filename

        ).first()

        if document:

            db.session.delete(

                document

            )

            db.session.commit()

def exists(

    self,

    filename

):

    return Document.query.filter_by(

        filename=filename

    ).first() is not None


document_db_service = DocumentDBService()