import celery
import os
import time

app = celery.Celery("example")

app.conf.update(
    broker_url=os.environ["REDIS_URL"],
    celery_backend_result=os.environ["REDIS_URL"],
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    task_time_limit=300,
)
app.conf.broker_transport_options = {"visibility_timeout": 60 * 60}  # 60 minutes


@app.task
def add(x, y):
    print("adding", x, y)

    time.sleep(300)

    return x + y
