FROM ubuntu:20.04
run apt update
ARG DEBIAN_FRONTEND=noninteractive
run apt  install  default-jdk  git  scala -y
run apt-get install -y wget tar
run wget  https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
run tar xvzf  spark-3.1.2-bin-hadoop3.2.tgz
run mv  spark-3.1.2-bin-hadoop3.2/  /opt/spark 
run apt install python3 -y
run apt install net-tools -y
run rm  spark-3.1.2-bin-hadoop3.2.tgz 
run echo export SPARK_HOME=/opt/spark>> /root/.bashrc
run echo export PATH='$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> /root/.bashrc
run echo export PYSPARK_PYTHON=/usr/bin/python3 >> /root/.bashrc
ENV SPARK_HOME "/opt/spark"
ENV PYSPARK_PYTHON "/usr/bin/python3"
ENV PATH "${SPARK_HOME}/bin: ${SPARK_HOME}/sbin:${PATH}"
