Context
-------

[Using REMAP_SIGTERM](https://devcenter.heroku.com/articles/celery-heroku#using-remap_sigterm)

How to reproduce
----------------

Run

```bash
poetry shell
export REDIS_URL="<redis url>"

python
```

```python
import tasks

tasks.add.delay(1, 2)
```

Then within 300 seconds (5 min) reboot the Heroku worker.


What should happen
------------------

- The task is queued by redis.
- Heroku worker starts executing the task which goes to a 5 min. sleep.
- When shutdown, Heroku worker sends SIGQUIT (because [REMAP_SIGTERM="SIGQUIT"](https://github.com/sayanarijit/remap-sigterm/blob/master/Procfile#L1)) to the worker.
- The worker exists immediately never acknowledging the task (the task stays in queue).
- After the worker comes back, it fetches the task from queue and starts running again.

What happens
------------

- The task is queued by redis.
- Heroku worker starts executing the task which goes to a 5 min. sleep.
- When shutdown, Heroku worker sends SIGTERM to the worker.
- The worker waits for the process to exit.
- After 30 seconds it kills the worker.
- After the worker comes back, the queue is empty. Hence task is lost.

Papertrail logs
---------------
```
Jul 24 05:12:38 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 24 05:12:39 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 24 05:12:42 remap-sigterm app/worker.1  
Jul 24 05:12:42 remap-sigterm app/worker.1  -------------- celery@7f757907-bb34-4df9-ad10-aa6b9c64ab0b v4.4.6 (cliffs)
Jul 24 05:12:42 remap-sigterm app/worker.1 --- ***** ----- 
Jul 24 05:12:42 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-24 12:12:41
Jul 24 05:12:42 remap-sigterm app/worker.1 - *** --- * --- 
Jul 24 05:12:42 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 24 05:12:42 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f3aa2b546a0
Jul 24 05:12:42 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-34-197-70-65.compute-1.amazonaws.com:7589//
Jul 24 05:12:42 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 24 05:12:42 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 24 05:12:42 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 24 05:12:42 remap-sigterm app/worker.1 --- ***** ----- 
Jul 24 05:12:42 remap-sigterm app/worker.1  -------------- [queues]
Jul 24 05:12:42 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 24 05:12:42 remap-sigterm app/worker.1                 
Jul 24 05:12:42 remap-sigterm app/worker.1 
Jul 24 05:12:42 remap-sigterm app/worker.1 [tasks]
Jul 24 05:12:42 remap-sigterm app/worker.1   . tasks.add
Jul 24 05:12:42 remap-sigterm app/worker.1 
Jul 24 05:12:42 remap-sigterm app/worker.1 [2020-07-24 12:12:41,740: INFO/MainProcess] Connected to redis://h:**@ec2-34-197-70-65.compute-1.amazonaws.com:7589//
Jul 24 05:12:42 remap-sigterm app/worker.1 [2020-07-24 12:12:41,776: INFO/MainProcess] mingle: searching for neighbors
Jul 24 05:12:43 remap-sigterm app/worker.1 [2020-07-24 12:12:42,824: INFO/MainProcess] mingle: all alone
Jul 24 05:12:43 remap-sigterm app/worker.1 [2020-07-24 12:12:42,858: INFO/MainProcess] celery@7f757907-bb34-4df9-ad10-aa6b9c64ab0b ready.
Jul 24 05:14:08 remap-sigterm app/heroku-redis source=REDIS addon=redis-corrugated-06071 sample#active-connections=11 sample#load-avg-1m=0.27 sample#load-avg-5m=0.235 sample#load-avg-15m=0.23 sample#read-iops=0 sample#write-iops=0 sample#memory-total=15664256kB sample#memory-free=12061936kB sample#memory-cached=1490592kB sample#memory-redis=566232bytes sample#hit-rate=0.045455 sample#evicted-keys=0
Jul 24 05:16:31 remap-sigterm app/worker.1 [2020-07-24 12:16:31,487: INFO/MainProcess] Received task: tasks.add[fe663179-4bcb-4301-90f8-191eb907571d]  
Jul 24 05:16:31 remap-sigterm app/worker.1 [2020-07-24 12:16:31,489: WARNING/ForkPoolWorker-8] adding
Jul 24 05:16:31 remap-sigterm app/worker.1 [2020-07-24 12:16:31,490: WARNING/ForkPoolWorker-8] 1
Jul 24 05:16:31 remap-sigterm app/worker.1 [2020-07-24 12:16:31,490: WARNING/ForkPoolWorker-8] 2
Jul 24 05:16:54 remap-sigterm heroku/worker.1 State changed from up to down
Jul 24 05:16:54 remap-sigterm app/api Scaled to worker@0:Free by user ab@niteo.co
Jul 24 05:16:55 remap-sigterm heroku/worker.1 Stopping all processes with SIGTERM
Jul 24 05:16:56 remap-sigterm app/worker.1 
Jul 24 05:16:56 remap-sigterm app/worker.1 worker: Warm shutdown (MainProcess)
Jul 24 05:17:20 remap-sigterm app/api Scaled to worker@1:Free by user ab@niteo.co
Jul 24 05:17:23 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 24 05:17:24 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 24 05:17:25 remap-sigterm heroku/worker.1 Error R12 (Exit timeout) -> At least one process failed to exit within 30 seconds of SIGTERM
Jul 24 05:17:25 remap-sigterm heroku/worker.1 Stopping remaining processes with SIGKILL
Jul 24 05:17:25 remap-sigterm heroku/worker.1 Process exited with status 137
Jul 24 05:17:27 remap-sigterm app/worker.1  
Jul 24 05:17:27 remap-sigterm app/worker.1  -------------- celery@4984b568-e615-4eb0-87f8-05fa547391ea v4.4.6 (cliffs)
Jul 24 05:17:27 remap-sigterm app/worker.1 --- ***** ----- 
Jul 24 05:17:27 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-24 12:17:27
Jul 24 05:17:27 remap-sigterm app/worker.1 - *** --- * --- 
Jul 24 05:17:27 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 24 05:17:27 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f9f2c8f36a0
Jul 24 05:17:27 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-34-197-70-65.compute-1.amazonaws.com:7589//
Jul 24 05:17:27 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 24 05:17:27 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 24 05:17:27 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 24 05:17:27 remap-sigterm app/worker.1 --- ***** ----- 
Jul 24 05:17:27 remap-sigterm app/worker.1  -------------- [queues]
Jul 24 05:17:27 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 24 05:17:27 remap-sigterm app/worker.1                 
Jul 24 05:17:27 remap-sigterm app/worker.1 
Jul 24 05:17:27 remap-sigterm app/worker.1 [tasks]
Jul 24 05:17:27 remap-sigterm app/worker.1   . tasks.add
Jul 24 05:17:27 remap-sigterm app/worker.1 
Jul 24 05:17:27 remap-sigterm app/worker.1 [2020-07-24 12:17:27,273: INFO/MainProcess] Connected to redis://h:**@ec2-34-197-70-65.compute-1.amazonaws.com:7589//
Jul 24 05:17:27 remap-sigterm app/worker.1 [2020-07-24 12:17:27,289: INFO/MainProcess] mingle: searching for neighbors
Jul 24 05:17:28 remap-sigterm app/worker.1 [2020-07-24 12:17:28,331: INFO/MainProcess] mingle: all alone
Jul 24 05:17:28 remap-sigterm app/worker.1 [2020-07-24 12:17:28,370: INFO/MainProcess] celery@4984b568-e615-4eb0-87f8-05fa547391ea ready.
```
