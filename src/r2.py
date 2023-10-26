import requests
from defines import Settings
from time import perf_counter
import boto3


r2_client = boto3.client(
    service_name="s3",
    endpoint_url=Settings.R2_ENDPOINT_URL,
    region_name="apac",
)

def upload_r2():
    print(f"Uploading image to R2")

    with open("sample.jpg", "rb") as image:
        r2_client.upload_fileobj(
            image,
            Settings.R2_BUCKET_NAME,
            "dev_test_interval.jpg",
        )

    start = perf_counter()
    return perf_counter() - start
