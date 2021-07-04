# Devops_Project

# to create a network bridge using docker

```
ubuntu@ip-172-31-16-251:~$ docker network create bigdata --subnet 192.162.100.0/24
3e2abd65eeee4ddf239c98f7cd4610d6d443a58663233ea78c4cca76652938a8
ubuntu@ip-172-31-16-251:~$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
3e2abd65eeee   bigdata   bridge    local
e549ae463592   bridge    bridge    local
f05be347504a   host      host      local
10d2f3284420   none      null      local

```

To create a container of name namenode with a unique ip 

 ```
 buntu@ip-172-31-16-251:~$ docker  run  -itd --name  namenode  --hostname namenode --network bigdata --ip 192.162.100.100 
 oraclelinux:8.3  bash 
Unable to find image 'oraclelinux:8.3' locally
8.3: Pulling from library/oraclelinux
dd34f38d274c: Pull complete 
Digest: sha256:af3182ee6c1e56f18fc1fecaf638da57d7c47233862e5c32f5ad723a6ab4c6db
Status: Downloaded newer image for oraclelinux:8.3
0ec70ce9633312017b01657680ef9d0c73003551b4501ac9cbeb85e3305b42c2
ubuntu@ip-172-31-16-251:~$ docker ps
CONTAINER ID   IMAGE             COMMAND   CREATED         STATUS         PORTS     NAMES
0ec70ce96333   oraclelinux:8.3   "bash"    9 seconds ago   Up 8 seconds             namenode
ubuntu@ip-172-31-16-251:~$ 

```

To create ba two data node container under a bridge ip range

```
ubuntu@ip-172-31-16-251:~$ docker  run  -itd --name  datanode1  --hostname datanode1 --network bigdata  oraclelinux:8.3  b
ash 
4173378f90ff129bf5d8cb3ad94da46c389d3966bf6894531b24be18568a2874
ubuntu@ip-172-31-16-251:~$ docker  run  -itd --name  datanode2  --hostname datanode2 --network bigdata  oraclelinux:8.3  b
ash 
e8e12ba7e8dcdd78f57da9143fbccc16fb73b0e726e51fdac665d8ee547e137e
ubuntu@ip-172-31-16-251:~$ docker ps
CONTAINER ID   IMAGE             COMMAND   CREATED          STATUS          PORTS     NAMES
e8e12ba7e8dc   oraclelinux:8.3   "bash"    8 seconds ago    Up 7 seconds              datanode2
4173378f90ff   oraclelinux:8.3   "bash"    40 seconds ago   Up 39 seconds             datanode1
0ec70ce96333   oraclelinux:8.3   "bash"    5 minutes ago    Up 5 minutes              namenode
ubuntu@ip-172-31-16-251:~$ 

```
To check the ip of datanode1

```
datanode1:/[root@datanode1 /]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
7: eth0@if8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c0:a2:64:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.162.100.2/24 brd 192.162.100.255 scope global eth0
       valid_lft forever preferred_lft foreve
       
 ```      
 To check the ip of datanode2
 
 ```
 ocker exec -it datanode2 bash
datanode2:/[root@datanode2 /]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
9: eth0@if10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c0:a2:64:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.162.100.3/24 brd 192.162.100.255 scope global eth0
 ```
 
 To connect name node via name (DNS)
 
 ```
 ocker exec -it datanode1 bash
datanode1:/[root@datanode1 /]# ping namenode
PING namenode (192.162.100.100) 56(84) bytes of data.
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=1 ttl=64 time=0.062 ms
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=2 ttl=64 time=0.063 ms
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=3 ttl=64 time=0.062 ms
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=4 ttl=64 time=0.072 ms
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=5 ttl=64 time=0.070 ms
64 bytes from namenode.bigdata (192.162.100.100): icmp_seq=6 ttl=64 time=0.071 ms
^C
--- namenode ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 109ms
rtt min/avg/max/mdev = 0.062/0.066/0.072/0.010 ms
datanode1:/[root@datanode1 /]# 
 ```
  To install jdk in namenode
  
  ```
  dnf  install  java-1.8.0-openjdk.x86_64  java-1.8.0-openjdk-devel.x86_64 -y
  
  ```
  To setting up java path
  
  ```
  lias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
. /etc/bashrc
fi
JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.292.b10-1.el8_4.x86_64
PATH=$PATH:$JAVA_HOME/bin

export PATH
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
~                                                                                                                         
".bashrc" 16L, 286C written
namenode:~[root@namenode ~]# source .bashrc
namenode:~[root@namenode ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.292.b10-1.el8_4.x86_64/
bin
namenode:~[root@namenode ~]# 
```


SAME FOR DATANODES

