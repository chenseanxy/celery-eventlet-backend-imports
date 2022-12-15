# celery-eventlet-backend-imports

Pool: Eventlet, Concurrency: 4

Run: `docker-compose up --build`

Result: result backend created for every task, even when task count > concurrency

```log
worker_1  | [2022-12-15 07:57:59,970: INFO/MainProcess] Task app.add[0ba80a3e-a005-4130-a0a6-e1bcfea3a237] received
worker_1  | [2022-12-15 07:57:59,971: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:57:59,997: INFO/MainProcess] Task app.add[c01d55a0-e1bc-4383-9ec2-c9d731eea754] received
worker_1  | [2022-12-15 07:57:59,999: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:00,024: INFO/MainProcess] Task app.add[0ba80a3e-a005-4130-a0a6-e1bcfea3a237] succeeded in 0.05403857305645943s: 3
worker_1  | [2022-12-15 07:58:00,060: INFO/MainProcess] Task app.add[c01d55a0-e1bc-4383-9ec2-c9d731eea754] succeeded in 0.06138216389808804s: 3
worker_1  | [2022-12-15 07:58:00,061: INFO/MainProcess] Task app.add[b5573261-40e7-47a2-b096-06d10815c7d5] received
worker_1  | [2022-12-15 07:58:00,062: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:00,092: INFO/MainProcess] Task app.add[b5573261-40e7-47a2-b096-06d10815c7d5] succeeded in 0.029728221939876676s: 3
worker_1  | [2022-12-15 07:58:00,313: INFO/MainProcess] Task app.add[cc15e275-42b6-4d65-9e97-e1f3f5b50b4a] received
worker_1  | [2022-12-15 07:58:00,314: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:00,339: INFO/MainProcess] Task app.add[cc15e275-42b6-4d65-9e97-e1f3f5b50b4a] succeeded in 0.025137985940091312s: 3
worker_1  | [2022-12-15 07:58:00,816: INFO/MainProcess] Task app.add[5a3cd184-a99a-4688-8e3a-7ef4712db083] received
worker_1  | [2022-12-15 07:58:00,817: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:00,843: INFO/MainProcess] Task app.add[5a3cd184-a99a-4688-8e3a-7ef4712db083] succeeded in 0.026621881988830864s: 3
worker_1  | [2022-12-15 07:58:01,320: INFO/MainProcess] Task app.add[8d0ef999-314e-4e78-87d1-58660367e870] received
worker_1  | [2022-12-15 07:58:01,321: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:01,343: INFO/MainProcess] Task app.add[8d0ef999-314e-4e78-87d1-58660367e870] succeeded in 0.021889708936214447s: 3
worker_1  | [2022-12-15 07:58:01,824: INFO/MainProcess] Task app.add[8104dd74-5858-4900-a063-289b49770354] received
worker_1  | [2022-12-15 07:58:01,825: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:01,845: INFO/MainProcess] Task app.add[8104dd74-5858-4900-a063-289b49770354] succeeded in 0.020653114072047174s: 3
worker_1  | [2022-12-15 07:58:02,328: INFO/MainProcess] Task app.add[a5806f1c-50d9-4228-9073-97b4cde7697d] received
worker_1  | [2022-12-15 07:58:02,329: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:02,350: INFO/MainProcess] Task app.add[a5806f1c-50d9-4228-9073-97b4cde7697d] succeeded in 0.02123527997173369s: 3
worker_1  | [2022-12-15 07:58:02,831: INFO/MainProcess] Task app.add[8a69444f-5fd7-4d0c-8ee8-e292ce4a7e81] received
worker_1  | [2022-12-15 07:58:02,833: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:02,855: INFO/MainProcess] Task app.add[8a69444f-5fd7-4d0c-8ee8-e292ce4a7e81] succeeded in 0.02192578709218651s: 3
worker_1  | [2022-12-15 07:58:03,334: INFO/MainProcess] Task app.add[400a2206-4822-407d-9a88-162831afd6db] received
worker_1  | [2022-12-15 07:58:03,335: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:03,357: INFO/MainProcess] Task app.add[400a2206-4822-407d-9a88-162831afd6db] succeeded in 0.021764658973552287s: 3
worker_1  | [2022-12-15 07:58:03,838: INFO/MainProcess] Task app.add[47c246e2-508c-4de2-8af1-a4047dd8d894] received
worker_1  | [2022-12-15 07:58:03,839: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:03,861: INFO/MainProcess] Task app.add[47c246e2-508c-4de2-8af1-a4047dd8d894] succeeded in 0.021861515939235687s: 3
worker_1  | [2022-12-15 07:58:04,341: INFO/MainProcess] Task app.add[298a61bf-7c2b-43ae-bf11-19514f4acf8f] received
worker_1  | [2022-12-15 07:58:04,342: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:04,363: INFO/MainProcess] Task app.add[298a61bf-7c2b-43ae-bf11-19514f4acf8f] succeeded in 0.02133279899135232s: 3
worker_1  | [2022-12-15 07:58:04,845: INFO/MainProcess] Task app.add[83167e3a-35af-4fc5-82c7-4d4b9dd38ee3] received
worker_1  | [2022-12-15 07:58:04,846: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:04,867: INFO/MainProcess] Task app.add[83167e3a-35af-4fc5-82c7-4d4b9dd38ee3] succeeded in 0.021252352045848966s: 3
worker_1  | [2022-12-15 07:58:05,348: INFO/MainProcess] Task app.add[6086f343-a332-4301-8d6e-b5ab017de05a] received
worker_1  | [2022-12-15 07:58:05,350: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:05,371: INFO/MainProcess] Task app.add[6086f343-a332-4301-8d6e-b5ab017de05a] succeeded in 0.021871726028621197s: 3
worker_1  | [2022-12-15 07:58:05,851: INFO/MainProcess] Task app.add[bff48c0d-b4fa-4e55-be0f-59106449eab2] received
worker_1  | [2022-12-15 07:58:05,852: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:05,873: INFO/MainProcess] Task app.add[bff48c0d-b4fa-4e55-be0f-59106449eab2] succeeded in 0.021623586071655154s: 3
worker_1  | [2022-12-15 07:58:06,354: INFO/MainProcess] Task app.add[0d3eb7a0-f93c-4eba-85ca-c5dfd0faf12e] received
worker_1  | [2022-12-15 07:58:06,355: INFO/MainProcess] Importing backend from redis://redis/0
worker_1  | [2022-12-15 07:58:06,377: INFO/MainProcess] Task app.add[0d3eb7a0-f93c-4eba-85ca-c5dfd0faf12e] succeeded in 0.022579420008696616s: 3
```


