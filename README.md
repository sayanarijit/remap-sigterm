

Papertrail logs
---------------
```
Jul 28 06:18:49 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 06:18:49 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 06:18:53 remap-sigterm app/worker.1  
Jul 28 06:18:53 remap-sigterm app/worker.1  -------------- celery@edc6ced4-7394-44b1-b287-1c49c06a75a2 v4.4.6 (cliffs)
Jul 28 06:18:53 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:18:53 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 13:18:52
Jul 28 06:18:53 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 06:18:53 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 06:18:53 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7f1c46c46630
Jul 28 06:18:53 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:18:53 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 06:18:53 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 06:18:53 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 06:18:53 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:18:53 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 06:18:53 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 06:18:53 remap-sigterm app/worker.1                 
Jul 28 06:18:53 remap-sigterm app/worker.1 
Jul 28 06:18:53 remap-sigterm app/worker.1 [tasks]
Jul 28 06:18:53 remap-sigterm app/worker.1   . tasks.add
Jul 28 06:18:53 remap-sigterm app/worker.1 
Jul 28 06:18:53 remap-sigterm app/worker.1 [2020-07-28 13:18:53,012: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:18:53 remap-sigterm app/worker.1 [2020-07-28 13:18:53,039: INFO/MainProcess] mingle: searching for neighbors
Jul 28 06:18:53 remap-sigterm app/api Build succeeded
Jul 28 06:18:54 remap-sigterm app/worker.1 [2020-07-28 13:18:54,099: INFO/MainProcess] mingle: all alone
Jul 28 06:18:54 remap-sigterm app/worker.1 [2020-07-28 13:18:54,140: INFO/MainProcess] celery@edc6ced4-7394-44b1-b287-1c49c06a75a2 ready.
Jul 28 06:19:45 remap-sigterm app/worker.1 [2020-07-28 13:19:44,711: INFO/MainProcess] Received task: tasks.add[57908042-66ca-40a3-8972-083385a8ea4c]  
Jul 28 06:19:45 remap-sigterm app/worker.1 [2020-07-28 13:19:44,732: WARNING/ForkPoolWorker-8] adding
Jul 28 06:19:45 remap-sigterm app/worker.1 [2020-07-28 13:19:44,733: WARNING/ForkPoolWorker-8] 1
Jul 28 06:19:45 remap-sigterm app/worker.1 [2020-07-28 13:19:44,733: WARNING/ForkPoolWorker-8] 2
Jul 28 06:19:57 remap-sigterm app/api Scaled to worker@0:Free by user ab@niteo.co
Jul 28 06:19:58 remap-sigterm heroku/worker.1 State changed from up to down
Jul 28 06:19:59 remap-sigterm heroku/worker.1 Stopping all processes with SIGTERM
Jul 28 06:19:59 remap-sigterm app/worker.1 
Jul 28 06:19:59 remap-sigterm app/worker.1 worker: Cold shutdown (MainProcess)
Jul 28 06:20:01 remap-sigterm app/api Scaled to worker@1:Free by user ab@niteo.co
Jul 28 06:20:08 remap-sigterm heroku/worker.1 Starting process with command `REMAP_SIGTERM=SIGQUIT celery -A tasks worker -l info`
Jul 28 06:20:08 remap-sigterm heroku/worker.1 State changed from starting to up
Jul 28 06:20:11 remap-sigterm app/worker.1  
Jul 28 06:20:11 remap-sigterm app/worker.1  -------------- celery@6dba84f3-0ec8-4447-bb25-931d4e3bf12b v4.4.6 (cliffs)
Jul 28 06:20:11 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:20:11 remap-sigterm app/worker.1 -- ******* ---- Linux-4.4.0-1074-aws-x86_64-with-debian-buster-sid 2020-07-28 13:20:10
Jul 28 06:20:11 remap-sigterm app/worker.1 - *** --- * --- 
Jul 28 06:20:11 remap-sigterm app/worker.1 - ** ---------- [config]
Jul 28 06:20:11 remap-sigterm app/worker.1 - ** ---------- .> app:         example:0x7ff6dc244630
Jul 28 06:20:11 remap-sigterm app/worker.1 - ** ---------- .> transport:   redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:20:11 remap-sigterm app/worker.1 - ** ---------- .> results:     disabled://
Jul 28 06:20:11 remap-sigterm app/worker.1 - *** --- * --- .> concurrency: 8 (prefork)
Jul 28 06:20:11 remap-sigterm app/worker.1 -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
Jul 28 06:20:11 remap-sigterm app/worker.1 --- ***** ----- 
Jul 28 06:20:11 remap-sigterm app/worker.1  -------------- [queues]
Jul 28 06:20:11 remap-sigterm app/worker.1                 .> celery           exchange=celery(direct) key=celery
Jul 28 06:20:11 remap-sigterm app/worker.1                 
Jul 28 06:20:11 remap-sigterm app/worker.1 
Jul 28 06:20:11 remap-sigterm app/worker.1 [tasks]
Jul 28 06:20:11 remap-sigterm app/worker.1   . tasks.add
Jul 28 06:20:11 remap-sigterm app/worker.1 
Jul 28 06:20:11 remap-sigterm app/worker.1 [2020-07-28 13:20:10,987: INFO/MainProcess] Connected to redis://h:**@ec2-23-21-96-121.compute-1.amazonaws.com:24849//
Jul 28 06:20:11 remap-sigterm app/worker.1 [2020-07-28 13:20:11,012: INFO/MainProcess] mingle: searching for neighbors
Jul 28 06:20:12 remap-sigterm app/worker.1 [2020-07-28 13:20:12,058: INFO/MainProcess] mingle: all alone
Jul 28 06:20:12 remap-sigterm app/worker.1 [2020-07-28 13:20:12,102: INFO/MainProcess] celery@6dba84f3-0ec8-4447-bb25-931d4e3bf12b ready.
Jul 28 06:20:29 remap-sigterm heroku/worker.1 Error R12 (Exit timeout) -> At least one process failed to exit within 30 seconds of SIGTERM
Jul 28 06:20:29 remap-sigterm heroku/worker.1 Stopping remaining processes with SIGKILL
Jul 28 06:20:29 remap-sigterm heroku/worker.1 Process exited with status 137
```
