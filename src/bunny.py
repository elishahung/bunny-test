import requests
from defines import Settings


def upload_bunny():
    print(f"Uploading image to BunnyCDN")

    with open("sample.jpg", "rb") as image:
        data = image.read()

    response = requests.put(
        f"{Settings.BUNNY_UPLOAD_URL}/test_interval.jpg",
        data=data,
        headers={
            "AccessKey": Settings.BUNNY_API_KEY,
            "content-type": "application/octet-stream",
        },
        # 5 minutes
        timeout=300,
    )
    response.raise_for_status()
