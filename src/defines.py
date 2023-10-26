import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    R2_ENDPOINT_URL = os.environ["R2_ENDPOINT_URL"]
    R2_BUCKET_NAME = os.environ["R2_BUCKET_NAME"]
    R2_PUBLIC_URL = os.environ["R2_PUBLIC_URL"]
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID", "")
    ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY", "")
