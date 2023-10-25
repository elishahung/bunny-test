from elasticsearch import Elasticsearch
from defines import Settings

elastic_client = Elasticsearch(
    cloud_id=Settings.ELASTIC_CLOUD_ID,
    api_key=Settings.ELASTIC_API_KEY,
)
