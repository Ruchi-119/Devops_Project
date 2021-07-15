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

## to start spark shell and pyspark

```
spark-shell

pyspark
```
