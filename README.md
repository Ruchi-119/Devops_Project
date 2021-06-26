# Devops_Project

 After create dockerfile and indexfile 
 
 docker build -t do:v1
 
 docker images
 
 ```
 ubuntu@ip-172-31-16-251:~/docker/docker_testing/apachefile$ docker images
REPOSITORY   TAG             IMAGE ID       CREATED             SIZE
do           v1              c2d30290de23   12 minutes ago      215MB

```

docker run -itd --name ruchij -p 1343:80 do:v1

docker ps

```
ubuntu@ip-172-31-16-251:~/docker/docker_testing/apachefile$ docker run -itd --name ruchij -p 1343:80 do:v1
a00fbb6eda708d346f3c6a27d3748dfed73e40cdcda8539f287f0bfb79fa5530
ubuntu@ip-172-31-16-251:~/docker/docker_testing/apachefile$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
a00fbb6eda70   do:v1     "/bin/sh -c 'apache2…"   8 seconds ago   Up 7 seconds   0.0.0.0:1343->80/tcp, :::1343->80/tcp   ruchij

```
