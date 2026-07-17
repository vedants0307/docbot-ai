from dotenv import load_dotenv
import os

load_dotenv()

print("URL:", os.getenv("SUPABASE_URL"))
print("KEY:", os.getenv("SUPABASE_SERVICE_KEY")[:20])

from services.supabase_service import supabase

print(supabase.storage.list_buckets())