import os

from services.rag_service import rag_service


class AnalyticsService:

    def get_stats(self):

        uploads_folder = "uploads"

        documents = 0
        websites = 0
        chunks = 0
        storage = 0

        # -----------------------
        # Uploaded Files
        # -----------------------

        if os.path.exists(uploads_folder):

            for file in os.listdir(uploads_folder):

                path = os.path.join(
                    uploads_folder,
                    file
                )

                if os.path.isfile(path):

                    documents += 1

                    storage += os.path.getsize(path)

        # -----------------------
        # ChromaDB
        # -----------------------

        results = rag_service.vectorstore.get()

        metadatas = results.get(
            "metadatas",
            []
        )

        chunks = len(metadatas)

        sources = set()

        type_count = {

            "pdf": 0,

            "txt": 0,

            "website": 0

        }

        source_chunks = {}

        for metadata in metadatas:

            source = metadata.get(
                "source"
            )

            doc_type = metadata.get(
                "type"
            )

            if doc_type in type_count:

                type_count[doc_type] += 1

            if source:

                sources.add(source)

                source_chunks[source] = (

                    source_chunks.get(
                        source,
                        0
                    ) + 1

                )

                if doc_type == "website":

                    websites += 1

        storage_mb = round(

            storage / (1024 * 1024),

            2

        )

        recent_sources = list(

            source_chunks.keys()

        )[-5:]

        average_chunks = round(

            chunks / max(
                len(source_chunks),
                1
            ),

            2

        )

        if source_chunks:

            largest_source = max(

                source_chunks,

                key=source_chunks.get

            )

            largest_chunks = source_chunks[
                largest_source
            ]

        else:

            largest_source = "-"

            largest_chunks = 0

        return {

            "documents": documents,

            "websites": len(

                [

                    s for s in sources

                    if s.startswith("http")

                ]

            ),

            "chunks": chunks,

            "sources": len(sources),

            "storage_mb": storage_mb,

            "embedding_model": "all-MiniLM-L6-v2",

            "vector_db": "ChromaDB",

            "status": "Healthy",

            "type_distribution": type_count,

            "recent_sources": recent_sources,

            "average_chunks": average_chunks,

            "largest_source": largest_source,

            "largest_chunks": largest_chunks

        }


analytics_service = AnalyticsService()