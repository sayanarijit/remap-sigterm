This Works as per expectation.

```
Jul 28 06:27:41 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 06:27:42 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 06:27:45 remap-sigterm app/worker.1  
Jul 28 06:27:45 remap-sigterm app/worker.1  -------------- celery@e58f232d-2f5e-43eb-b872-e8b2b6520b68 v4.4.6 (cliffs)
Jul 28 06:27:45 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:27:45 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 13:27:44
Jul 28 06:27:45 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 06:27:45 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 06:27:45 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f1bb85336a0
Jul 28 06:27:45 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:27:45 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 06:27:45 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 06:27:45 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 06:27:45 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:27:45 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 06:27:45 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 06:27:45 remap-sigterm app/worker.1                 
Jul 28 06:27:45 remap-sigterm app/worker.1 
Jul 28 06:27:45 remap-sigterm app/worker.1 [tasks]
Jul 28 06:27:45 remap-sigterm app/worker.1   . tasks.add
Jul 28 06:27:45 remap-sigterm app/worker.1 
Jul 28 06:27:45 remap-sigterm app/worker.1 [2020-07-28 13:27:45,010: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:27:45 remap-sigterm app/worker.1 [2020-07-28 13:27:45,044: INFO/MainProcess] mingle: searching for neighbors
Jul 28 06:27:46 remap-sigterm app/api Build succeeded
Jul 28 06:27:46 remap-sigterm app/worker.1 [2020-07-28 13:27:46,206: INFO/MainProcess] mingle: all alone
Jul 28 06:27:46 remap-sigterm app/worker.1 [2020-07-28 13:27:46,234: INFO/MainProcess] celery@e58f232d-2f5e-43eb-b872-e8b2b6520b68 ready.
Jul 28 06:27:57 remap-sigterm app/heroku-redis source=REDIS addon=redis-corrugated-06071 sample#active-connections=6 sample#load-avg-1m=0.14 sample#load-avg-5m=0.14 sample#load-avg-15m=0.135 sample#read-iops=0 sample#write-iops=0 sample#memory-total=15664244kB sample#memory-free=12956796kB sample#memory-cached=703864kB sample#memory-redis=422368bytes sample#hit-rate=0.49414 sample#evicted-keys=0
Jul 28 06:28:09 remap-sigterm app/worker.1 [2020-07-28 13:28:08,736: INFO/MainProcess] Received task: tasks.add[cceb21a7-c559-4718-9484-46f25b70f26a]  
Jul 28 06:28:09 remap-sigterm app/worker.1 [2020-07-28 13:28:08,739: WARNING/ForkPoolWorker-8] adding
Jul 28 06:28:09 remap-sigterm app/worker.1 [2020-07-28 13:28:08,740: WARNING/ForkPoolWorker-8] 1
Jul 28 06:28:09 remap-sigterm app/worker.1 [2020-07-28 13:28:08,740: WARNING/ForkPoolWorker-8] 2
Jul 28 06:28:23 remap-sigterm heroku/worker.1 State changed from up to down
Jul 28 06:28:23 remap-sigterm app/api Scaled to worker@0:Free by user ab@niteo.co
Jul 28 06:28:24 remap-sigterm heroku/worker.1 Stopping all processes with SIGTERM
Jul 28 06:28:24 remap-sigterm app/worker.1 
Jul 28 06:28:24 remap-sigterm app/worker.1 worker: Cold shutdown (MainProcess)
Jul 28 06:28:26 remap-sigterm app/worker.1 [2020-07-28 13:28:25,858: WARNING/MainProcess] Restoring 1 unacknowledged message(s)
Jul 28 06:28:26 remap-sigterm heroku/worker.1 Process exited with status 0
Jul 28 06:28:29 remap-sigterm app/api Scaled to worker@1:Free by user ab@niteo.co
Jul 28 06:28:32 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 06:28:33 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 06:28:35 remap-sigterm app/worker.1  
Jul 28 06:28:35 remap-sigterm app/worker.1  -------------- celery@749a3080-f24e-4628-9601-89cf618adf83 v4.4.6 (cliffs)
Jul 28 06:28:35 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:28:35 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 13:28:34
Jul 28 06:28:35 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 06:28:35 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 06:28:35 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f8fb4156860
Jul 28 06:28:35 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:28:35 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 06:28:35 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 06:28:35 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 06:28:35 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:28:35 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 06:28:35 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 06:28:35 remap-sigterm app/worker.1                 
Jul 28 06:28:35 remap-sigterm app/worker.1 
Jul 28 06:28:35 remap-sigterm app/worker.1 [tasks]
Jul 28 06:28:35 remap-sigterm app/worker.1   . tasks.add
Jul 28 06:28:35 remap-sigterm app/worker.1 
Jul 28 06:28:35 remap-sigterm app/worker.1 [2020-07-28 13:28:35,032: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:28:35 remap-sigterm app/worker.1 [2020-07-28 13:28:35,055: INFO/MainProcess] mingle: searching for neighbors
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,090: INFO/MainProcess] mingle: all alone
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,123: INFO/MainProcess] celery@749a3080-f24e-4628-9601-89cf618adf83 ready.
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,241: INFO/MainProcess] Received task: tasks.add[cceb21a7-c559-4718-9484-46f25b70f26a]  
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,244: WARNING/ForkPoolWorker-8] adding
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,244: WARNING/ForkPoolWorker-8] 1
Jul 28 06:28:36 remap-sigterm app/worker.1 [2020-07-28 13:28:36,244: WARNING/ForkPoolWorker-8] 2
```
