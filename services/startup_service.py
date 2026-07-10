import os

from services.rag_service import rag_service


class StartupService:

    def sync_documents(self):

        upload_folder = "uploads"

        if not os.path.exists(upload_folder):

            return

        indexed = set(

            rag_service.list_sources()

        )

        for file in os.listdir(upload_folder):

            path = os.path.join(

                upload_folder,

                file

            )

            if not os.path.isfile(path):

                continue

            if file in indexed:

                print(

                    f"✓ Already Indexed : {file}"

                )

                continue

            print(

                f"Indexing : {file}"

            )

            rag_service.upload_document(

                path

            )


startup_service = StartupService()