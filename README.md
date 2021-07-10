# Devops_Project

### Creating directory in namenode from hdfs
```
[root@namenode /]# hdfs dfs -ls /
[root@namenode /]# hdfs dfs -mkdir /hadoop
[root@namenode /]# hdfs dfs -ls /
Found 1 items
drwxr-xr-x   - root supergroup          0 2021-07-08 15:57 /hadoop
[root@namenode /]# hdfs dfs -mkdir /hadoop/data
[root@namenode /]# hdfs dfs -mkdir /ruchi
^[[A^[[A[root@namenode /]# hdfs dfs -mkdir /ruchi/data-engg
[root@namenode /]# hdfs dfs -ls -R /
drwxr-xr-x   - root supergroup          0 2021-07-08 15:57 /hadoop
drwxr-xr-x   - root supergroup          0 2021-07-08 15:57 /hadoop/data
drwxr-xr-x   - root supergroup          0 2021-07-08 15:58 /ruchi
drwxr-xr-x   - root supergroup          0 2021-07-08 15:58 /ruchi/data-engg

```
## Generate data
```
[root@namenode /]# yes "Hello welcome to hadoop" >/tmp/data.txt
^C
[root@namenode /]# ls -lh /tmp/data.txt
-rw-r--r-- 1 root root 520M Jul  8 16:01 /tmp/data.txt
[root@namenode /]# wc -l /tmp/data.txt
21773189 /tmp/data.txt
[root@namenode /]# 
```

## For copy from data.txt to /ruchi/data-engg

```
[root@namenode /]# hdfs dfs -copyFromLocal /tmp/data.txt /ruchi/data-engg/

```


