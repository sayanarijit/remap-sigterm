import celery
import os
import time
from celery.exceptions import WorkerTerminate
from celery.platforms import EX_FAILURE
from functools import partial

app = celery.Celery("example")

app.conf.update(
    broker_url=os.environ["REDIS_URL"],
    celery_backend_result=os.environ["REDIS_URL"],
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    task_time_limit=300,
)
app.conf.broker_transport_options = {"visibility_timeout": 60 * 60}  # 60 minutes


@celery.signals.celeryd_after_setup.connect
def worker_ready(*args, **kwargs):
    try:
        celery.apps.worker.install_worker_term_handler = partial(
            celery.apps.worker._shutdown_handler,
            sig="SIGTERM",
            how="Cold",
            exc=WorkerTerminate,
            exitcode=EX_FAILURE,
        )
    except Exception as e:
        print(e)


@app.task
def add(x, y):
    print("adding", x, y)

    time.sleep(300)

    return x + y
