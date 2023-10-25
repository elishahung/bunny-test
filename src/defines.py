import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    BUNNY_API_KEY = os.environ.get("BUNNY_API_KEY", "")
    BUNNY_UPLOAD_URL = os.environ.get("BUNNY_UPLOAD_URL", "")
    BUNNY_PUBLIC_URL = os.environ.get("BUNNY_PUBLIC_URL", "")
    ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID", "")
    ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY", "")
