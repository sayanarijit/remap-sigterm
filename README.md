Works fine.

Ref: https://github.com/celery/celery/pull/6249

```
ul 28 08:28:04 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 08:28:04 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 08:28:07 remap-sigterm app/worker.1  
Jul 28 08:28:07 remap-sigterm app/worker.1  -------------- celery@b48b45e2-1e36-42b0-9c20-36c47b35508e v4.4.6 (cliffs)
Jul 28 08:28:07 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 08:28:07 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 15:28:06
Jul 28 08:28:07 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 08:28:07 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 08:28:07 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f6512748630
Jul 28 08:28:07 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 08:28:07 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 08:28:07 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 08:28:07 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 08:28:07 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 08:28:07 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 08:28:07 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 08:28:07 remap-sigterm app/worker.1                 
Jul 28 08:28:07 remap-sigterm app/worker.1 
Jul 28 08:28:07 remap-sigterm app/worker.1 [tasks]
Jul 28 08:28:07 remap-sigterm app/worker.1   . tasks.add
Jul 28 08:28:07 remap-sigterm app/worker.1 
Jul 28 08:28:07 remap-sigterm app/worker.1 [2020-07-28 15:28:07,090: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 08:28:07 remap-sigterm app/worker.1 [2020-07-28 15:28:07,114: INFO/MainProcess] mingle: searching for neighbors
Jul 28 08:28:08 remap-sigterm app/worker.1 [2020-07-28 15:28:08,150: INFO/MainProcess] mingle: all alone
Jul 28 08:28:08 remap-sigterm app/worker.1 [2020-07-28 15:28:08,182: INFO/MainProcess] celery@b48b45e2-1e36-42b0-9c20-36c47b35508e ready.
Jul 28 08:28:10 remap-sigterm app/api Build succeeded
Jul 28 08:30:01 remap-sigterm app/heroku-redis source=REDIS addon=redis-corrugated-06071 sample#active-connections=11 sample#load-avg-1m=0.26 sample#load-avg-5m=0.215 sample#load-avg-15m=0.185 sample#read-iops=0 sample#write-iops=0 sample#memory-total=15664244kB sample#memory-free=12948476kB sample#memory-cached=705296kB sample#memory-redis=525568bytes sample#hit-rate=0.48261 sample#evicted-keys=0
Jul 28 08:30:36 remap-sigterm app/worker.1 [2020-07-28 15:30:35,963: INFO/MainProcess] Received task: tasks.add[47b48d85-0a37-4b24-99be-285b1f9d4485]  
Jul 28 08:30:36 remap-sigterm app/worker.1 [2020-07-28 15:30:35,966: WARNING/ForkPoolWorker-8] adding
Jul 28 08:30:36 remap-sigterm app/worker.1 [2020-07-28 15:30:35,967: WARNING/ForkPoolWorker-8] 1
Jul 28 08:30:36 remap-sigterm app/worker.1 [2020-07-28 15:30:35,967: WARNING/ForkPoolWorker-8] 2
Jul 28 08:30:53 remap-sigterm heroku/worker.1 State changed from up to down
Jul 28 08:30:53 remap-sigterm app/api Scaled to worker@0:Free by user ab@niteo.co
Jul 28 08:30:54 remap-sigterm heroku/worker.1 Stopping all processes with SIGTERM
Jul 28 08:30:54 remap-sigterm app/worker.1 
Jul 28 08:30:54 remap-sigterm app/worker.1 worker: Cold shutdown (MainProcess)
Jul 28 08:30:55 remap-sigterm app/worker.1 [2020-07-28 15:30:55,680: WARNING/MainProcess] Restoring 1 unacknowledged message(s)
Jul 28 08:30:55 remap-sigterm heroku/worker.1 Process exited with status 0
Jul 28 08:30:56 remap-sigterm app/api Scaled to worker@1:Free by user ab@niteo.co
Jul 28 08:31:02 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 08:31:02 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 08:31:08 remap-sigterm app/worker.1  
Jul 28 08:31:08 remap-sigterm app/worker.1  -------------- celery@29ce6666-06a9-462c-8997-313d84ad6ac8 v4.4.6 (cliffs)
Jul 28 08:31:08 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 08:31:08 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 15:31:08
Jul 28 08:31:08 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 08:31:08 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 08:31:08 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7fe4c6784630
Jul 28 08:31:08 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 08:31:08 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 08:31:08 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 08:31:08 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 08:31:08 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 08:31:08 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 08:31:08 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 08:31:08 remap-sigterm app/worker.1                 
Jul 28 08:31:08 remap-sigterm app/worker.1 
Jul 28 08:31:08 remap-sigterm app/worker.1 [tasks]
Jul 28 08:31:08 remap-sigterm app/worker.1   . tasks.add
Jul 28 08:31:08 remap-sigterm app/worker.1 
Jul 28 08:31:09 remap-sigterm app/worker.1 [2020-07-28 15:31:08,827: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 08:31:09 remap-sigterm app/worker.1 [2020-07-28 15:31:08,872: INFO/MainProcess] mingle: searching for neighbors
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,058: INFO/MainProcess] mingle: all alone
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,270: INFO/MainProcess] celery@29ce6666-06a9-462c-8997-313d84ad6ac8 ready.
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,346: INFO/MainProcess] Received task: tasks.add[47b48d85-0a37-4b24-99be-285b1f9d4485]  
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,382: WARNING/ForkPoolWorker-8] adding
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,383: WARNING/ForkPoolWorker-8] 1
Jul 28 08:31:10 remap-sigterm app/worker.1 [2020-07-28 15:31:10,383: WARNING/ForkPoolWorker-8] 2
```
