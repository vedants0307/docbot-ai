from langchain_chroma import Chroma

from services.embedding_service import get_embedding_model

VECTOR_DB_DIR = "embeddings_db"

_vector_store = None


def get_vector_store():

    global _vector_store

    if _vector_store is None:

        _vector_store = Chroma(

            persist_directory=VECTOR_DB_DIR,

            embedding_function=get_embedding_model()

        )

    return _vector_store