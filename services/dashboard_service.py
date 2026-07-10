from services.analytics_service import analytics_service


class DashboardService:

    def get_dashboard(self):

        stats = analytics_service.get_stats()

        return {

            "documents": stats["documents"],

            "websites": stats["websites"],

            "chunks": stats["chunks"],

            "sources": stats["sources"],

            "storage": stats["storage_mb"],

            "llm": "Gemini 2.5 Flash",

            "embedding": stats["embedding_model"],

            "vector_db": stats["vector_db"],

            "status": stats["status"]

        }


dashboard_service = DashboardService()