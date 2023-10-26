from bunny import upload_bunny
from elastic import elastic_client
from time import perf_counter, sleep
import traceback
from datetime import datetime


def log_status(status: str, error: str = None, upload_time: float = None):
    elastic_client.index(
        index="bunny-external-test",
        document={
            "@timestamp": datetime.utcnow(),
            "status": status,
            "error": error,
            "upload_time": upload_time,
        },
    )


if __name__ == "__main__":
    while True:
        start = perf_counter()
        upload_time = None

        try:
            upload_time = upload_bunny()
            log_status("success", None, upload_time)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            log_status("failed", str(e))

        duration = perf_counter() - start
        diff = 60 - duration

        if diff > 0:
            print(f"Sleeping for {diff} seconds")
            sleep(diff)
