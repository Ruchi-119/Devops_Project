FROM ubuntu:20.04
# this image will be pulled from docker hub if not present
MAINTAINER jnru501@gmail.com
# optional field but good to write 
RUN  apt update -y
RUN  apt install python3 -y
# RUN instruction is for getting shell during image build time
RUN mkdir /myworld
# creating a directory to put  my code inside docker image 
COPY ruchi.py  /myworld/ruchi.py
# to copy data from client location to docker image 
# make sure your code location is same as Dockerfile location
WORKDIR  /myworld
# changing location of docker image like cd command in linux
CMD  ["python3","ruchi.py"]
# to set default process for container
