from bunny import upload_bunny
from elastic import elastic_client
from time import perf_counter, sleep
import traceback
from datetime import datetime


def log_status(status: str, error: str = None):
    elastic_client.index(
        index="bunny-external-test",
        document={
            "@timestamp": datetime.utcnow(),
            "status": status,
            "error": error,
        },
    )


if __name__ == "__main__":
    while True:
        start = perf_counter()

        try:
            upload_bunny()
            log_status("success")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            log_status("failed", str(e))

        duration = perf_counter() - start
        diff = 60 - duration

        if diff > 0:
            print(f"Sleeping for {diff} seconds")
            sleep(diff)
