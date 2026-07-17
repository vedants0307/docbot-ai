import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(

    os.getenv("SUPABASE_URL"),

    os.getenv("SUPABASE_SERVICE_KEY")

)


def upload_document(file_path, filename):

    with open(file_path, "rb") as file:

        supabase.storage.from_(

            "documents"

        ).upload(

            path=filename,

            file=file,

            file_options={

                "upsert": "true"

            }

        )


def delete_document(filename):

    supabase.storage.from_(

        "documents"

    ).remove(

        [

            filename

        ]

    )


def get_signed_url(filename):

    response = supabase.storage.from_(

        "documents"

    ).create_signed_url(

        filename,

        3600

    )

    return response