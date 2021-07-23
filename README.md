# Devops_Project

## run Docker file

```
docker build -t spark:v1 .

docker run -it  --name apache_spark spark:v1 bash

```

## to push docker file in  my docker hub

```
docker tag spark:v1  ruchijain12/spark:v1

docker login -u ruchijain12

docker push ruchijain12/spark:v1
```

## to pull this docker image

```
docker pull ruchijain12/spark:v1

```


## docker images

```

ubuntu@ip-172-31-16-251:~/docker/hadoop$ docker images
REPOSITORY          TAG       IMAGE ID       CREATED             SIZE
spark               v1        d04c3990df10   38 minutes ago      1.65GB
ruchijain12/spark   v1        d04c3990df10   38 minutes ago      1.65GB
<none>              <none>    1bc0bd1449b4   57 minutes ago      1.4GB
<none>              <none>    1163fa4626ec   About an hour ago   1.14GB

```
## To check this image is working fine

```
ubuntu@ip-172-31-16-251:~/docker/hadoop$ docker exec -it apache_spark bash
root@ac2747b126b3:/# echo $SPARK_HOME
/opt/spark
root@ac2747b126b3:/# jps
27 Jps
root@ac2747b126b3:/# java --version
openjdk 11.0.11 2021-04-20
OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2.20.04)
OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2.20.04, mixed mode, sharing)
root@ac2747b126b3:/# scala --version
bad option: '--version'

Usage: scala <options> [<script|class|object|jar> <arguments>]
   or  scala -help

All options to scalac (see scalac -help) are also allowed.

root@ac2747b126b3:/# scala -version
Scala code runner version 2.11.12 -- Copyright 2002-2017, LAMP/EPFL
root@ac2747b126b3:/# 
```

## to start master
```
root@ac2747b126b3:/# start-master.sh
starting org.apache.spark.deploy.master.Master, logging to /opt/spark/logs/spark--org.apache.spark.deploy.master.Master-1-ac2747b126b3.out
root@ac2747b126b3:/# jps
129 Master
178 Jps
```
## to run this image always

```
docker  run -itd  --name sparkmaster --hostname sparkM  --network bridge  -p 9898:8080 --restart  always  ruchijain12/spark:v1   bash
```
## to start worker

```
docker exec -it sparkmaster bash

start-worker.sh spark://sparkM:7077
starting org.apache.spark.deploy.worker.Worker, logging to /opt/spark/logs/spark--org
.apache.spark.deploy.worker.Worker-1-sparkM.out
oot@sparkM: /root@sparkM:/# jps
49 Master
299 Worker
350 Jps
```
## to start spark shell and pyspark

```
sprk-shell

pyspark
```
## create a text file  /tmp/data.txt
## enter pyspark

```
park context Web UI available at http://sparkM:4040
Spark context available as 'sc' (master = local[*], app id = local-1627029083298).
SparkSession available as 'spark'.
>>> firstrdd=sc.textFile('/tmp/data.txt')
>>> firstRDD.first()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'firstRDD' is not defined
>>> firstrdd.first()
'pache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface for p
rogramming entire clusters with implicit data parallelism and fault tolerance.'
>>> firstrdd.take(5)
['pache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface for 
programming entire clusters with implicit data parallelism and fault tolerance.', 'Apache Spark is an open-source unified 
analytics engine for large-scale data processing. Spark provides an interface for programming entire clusters with implici
t data parallelism and fault tolerance.', 'Apache Spark is an open-source unified analytics engine for large-scale data pr
ocessing. Spark provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.'
, 'Apache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface fo
r programming entire clusters with implicit data parallelism and fault tolerance.', 'Apache Spark is an open-source unifie
d analytics engine for large-scale data processing. Spark provides an interface for programming entire clusters with impli
cit data parallelism and fault tolerance.']

```


## for python as a pyspark we import a pyspark module
## creating python file

