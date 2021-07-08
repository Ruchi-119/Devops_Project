# Devops_Project

# Installing hadoop on ubuntu machine
``

wget https://downloads.apache.org/hadoop/common/stable/hadoop-3.3.1.tar.gz
``
```wget https://downloads.apache.org/hadoop/common/stable/hadoop-3.3.1.tar.gz
--2021-07-05 02:45:04--  https://downloads.apache.org/hadoop/common/stable/hadoop-3.3.1.tar.gz
Resolving downloads.apache.org (downloads.apache.org)... 135.181.214.104, 88.99.95.219, 135.181.209.10, ...
Connecting to downloads.apache.org (downloads.apache.org)|135.181.214.104|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 605187279 (577M) [application/x-gzip]
Saving to: ‘hadoop-3.3.1.tar.gz’
```

## Transfer hadoop to containers

`
docker cp hadoop-3.3.1.tar.gz namenode:/
ubuntu@ip-172-31-16-251:~/docker$ docker cp hadoop-3.3.1.tar.gz datnode1:/
no such directory
ubuntu@ip-172-31-16-251:~/docker$ docker cp hadoop-3.3.1.tar.gz datanode1:/
ubuntu@ip-172-31-16-251:~/docker$ docker cp hadoop-3.3.1.tar.gz datanode2:/
ubuntu@ip-172-31-16-251:~/docker$ 

`
## to install tar

dnf install tar

# to unzip tar.gz file

tar -xvzf hadoop-3.3.1.tar.gz

mv hadoop-3.3.1/ hadoop3  // to move hadoop3.3.1 to hadoop3


### to set hadoop home path

cd hadoop3/

vi /root/.bashrc

``
# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.292.b10-1.el8_4.x86_64
HADOOP_HOME=/hadoop3
PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

export PATH

``
## FOR ALL NODES

vi hadoop-env.sh

``


## FOR ALL NODES

vi core-site.xml

``
<configuration>
<property>
	<name>fs.default.name</name>
	<value>hdfs://namenode:9000</value>
</property>

</configuration>

``
## For namenode 

vi hdfs-site.xml

``
configuration>
<property>
	<name>dfs.namenode.name.dir</name>
	<value>/mynndata</value>
	<description>location where namenode will store its metadata </description>
</property>

<property>
	<name>dfs.replication</name>
	<value>3</value>
	<description> number of copy for each block or chunk </description>
</property>
</configuration>

``

## For datanode1

vi hdfs-site.xml

``
<configuration>

<property>
	<name>dfs.datanode.data.dir</name>
	<value>/mydndata1</value>
        <description>location where datanode will store its data</description>
</property>
</configuration>

``
## For datanode2

vi hdfs-site.xml

``
<configuration>

<property>
	<name>dfs.datanode.data.dir</name>
	<value>/mydndata2</value>
        <description>location where datanode will store its data</description>
</property>
</configuration>

``
## In namenode 

hdfs  namenode  -format

hdfs  --daemon  start namenode 

jps

## In datnodes

hdfs  --daemon  start datanode 

jps








