import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class DocumentService:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200

        )

    # ---------------------------------
    # Load Document
    # ---------------------------------

    def load_document(

        self,

        file_path

    ):

        extension = os.path.splitext(

            file_path

        )[1].lower()

        if extension == ".pdf":
            from pypdf import PdfReader

            print(file_path)

            reader = PdfReader(file_path)

            print("Pages:", len(reader.pages))

            loader = PyPDFLoader(

                file_path

            )

        elif extension == ".txt":

            loader = TextLoader(

                file_path

            )

        else:

            raise Exception(

                "Unsupported file type."

            )

        return loader.load()

    # ---------------------------------
    # Split Document
    # ---------------------------------

    def split_document(

        self,

        documents

    ):

        return self.splitter.split_documents(

            documents

        )

    # ---------------------------------
    # Process Document
    # ---------------------------------

    def process_document(

        self,

        file_path

    ):

        documents = self.load_document(

            file_path

        )

        chunks = self.split_document(

            documents

        )

        filename = os.path.basename(

            file_path

        )

        extension = os.path.splitext(

            file_path

        )[1].replace(

            ".",

            ""

        )

        for index, chunk in enumerate(chunks):

            chunk.metadata["source"] = filename

            chunk.metadata["filename"] = filename

            chunk.metadata["type"] = extension

            chunk.metadata["chunk"] = index + 1

        return chunks


document_service = DocumentService()