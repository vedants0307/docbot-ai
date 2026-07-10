import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

from langchain_community.document_loaders import (
    WebBaseLoader
)


class WebsiteService:

    # ---------------------------------
    # Get Internal Links
    # ---------------------------------

    def get_internal_links(
        self,
        base_url
    ):

        try:

            response = requests.get(

                base_url,

                timeout=10

            )

            soup = BeautifulSoup(

                response.text,

                "html.parser"

            )

            links = set()

            domain = urlparse(

                base_url

            ).netloc

            for tag in soup.find_all(

                "a",

                href=True

            ):

                full_url = urljoin(

                    base_url,

                    tag["href"]

                )

                parsed = urlparse(

                    full_url

                )

                if parsed.netloc == domain:

                    links.add(

                        full_url

                    )

            return list(

                links

            )

        except Exception as e:

            print(

                "Link Extraction Error:",

                e

            )

            return []

    # ---------------------------------
    # Crawl Website
    # ---------------------------------

    def crawl_website(

        self,

        start_url,

        max_pages=20

    ):

        urls = [

            start_url

        ]

        visited = set()

        documents = []

        while urls and len(visited) < max_pages:

            current = urls.pop(0)

            if current in visited:

                continue

            print(

                f"Crawling: {current}"

            )

            visited.add(

                current

            )

            try:

                loader = WebBaseLoader(

                    current

                )

                loader.requests_kwargs = {

                    "timeout":10

                }

                docs = loader.load()

                print(

                    f"Loaded {len(docs)} document(s)"

                )

                for index, doc in enumerate(docs):

                    doc.metadata["source"] = start_url

                    doc.metadata["page_url"] = current

                    doc.metadata["type"] = "website"

                    doc.metadata["chunk"] = index + 1

                documents.extend(

                    docs

                )

                links = self.get_internal_links(

                    current

                )

                for link in links:

                    if (

                        link not in visited

                        and

                        link not in urls

                    ):

                        urls.append(

                            link

                        )

            except Exception as e:

                print(

                    f"Error crawling {current}:",

                    e

                )

        print(

            f"Finished crawling {len(visited)} page(s)"

        )

        return documents


website_service = WebsiteService()