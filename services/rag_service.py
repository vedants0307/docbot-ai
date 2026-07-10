import os

from langchain_core.output_parsers import (
    StrOutputParser
)

from langchain_core.runnables import (
    RunnablePassthrough
)

from services.document_service import (
    document_service
)

from services.website_service import (
    website_service
)

from services.vector_store import (
    get_vector_store
)

from services.llm_service import (
    get_llm
)

from services.prompt_service import (
    QA_PROMPT
)


class RAGService:

    def __init__(self):

        self.vectorstore = get_vector_store()

    # ---------------------------------
    # Upload PDF / TXT
    # ---------------------------------

    def upload_document(
        self,
        file_path
    ):

        chunks = document_service.process_document(
            file_path
        )

        self.vectorstore.add_documents(
            chunks
        )

        return len(chunks)

    # ---------------------------------
    # Upload Website
    # ---------------------------------

# ---------------------------------
# Upload Website
# ---------------------------------

    def upload_website(
        self,
        url
    ):

        print("Starting website crawl...")

        documents = website_service.crawl_website(
            url
        )

        print(f"Pages Crawled : {len(documents)}")

        if not documents:

            return 0

        chunks = document_service.split_document(
            documents
        )

        print(f"Chunks Created : {len(chunks)}")

        self.vectorstore.add_documents(
            chunks
        )

        print("Website Indexed Successfully.")

        return len(chunks)

    # ---------------------------------
    # Retrieve Documents
    # ---------------------------------

    def retrieve_documents(

        self,

        question,

        scope="global",

        k=10

    ):

        if scope == "global":

            retriever = self.vectorstore.as_retriever(

                search_kwargs={

                    "k": k

                }

            )

            return retriever.invoke(

                question

            )

        else:

            return self.vectorstore.similarity_search(

                question,

                k=k,

                filter={

                    "source": scope

                }

            )

    # ---------------------------------
    # Ask Question
    # ---------------------------------

    def ask_question(

        self,

        question,

        scope="global"

    ):

        docs = self.retrieve_documents(

            question,

            scope

        )

        print("=" * 60)
        print("Question:", question)
        print("Scope:", scope)
        print("Retrieved Docs:", len(docs))

        for doc in docs:

            print(doc.metadata)

        print("=" * 60)

        context = "\n\n".join(

            doc.page_content

            for doc in docs

        )

        print("Context Length:", len(context))

        llm = get_llm()

        chain = (

            {

                "context": RunnablePassthrough(),

                "question": RunnablePassthrough()

            }

            |

            QA_PROMPT

            |

            llm

            |

            StrOutputParser()

        )

        answer = chain.invoke(

            {

                "context": context,

                "question": question

            }

        )

        return {

            "answer": answer,

            "sources": docs

        }
    # ---------------------------------
    # Similarity Search
    # ---------------------------------

    def similarity_search(

        self,

        query,

        k=5

    ):

        return self.vectorstore.similarity_search(

            query,

            k=k

        )

    # ---------------------------------
    # List Sources
    # ---------------------------------

    def list_sources(

        self

    ):

        results = self.vectorstore.get()

        sources = set()

        if "metadatas" in results:

            for metadata in results["metadatas"]:

                source = metadata.get(

                    "source"

                )

                if source:

                    sources.add(

                        source

                    )

        return sorted(

            list(

                sources

            )

        )

    # ---------------------------------
    # Delete Document
    # ---------------------------------

    def delete_document(

        self,

        filename

    ):

        results = self.vectorstore.get(

            where={

                "source": filename

            }

        )

        ids = results.get(

            "ids",

            []

        )

        if ids:

            self.vectorstore.delete(

                ids=ids

            )

        return len(

            ids

        )

rag_service = RAGService()