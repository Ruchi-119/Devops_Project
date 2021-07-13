# Devops_Project


## Setup for resourcemanager
## in mapered-site.xml

```
<configuration>
<property>
	<name>mapreduce.framework.name</name>
	<value>yarn</value>
</property>
</configuration>
```

## in yarn-site.xml

```
<configuration>

<!-- Site specific YARN configuration properties -->
<property>
<name>yarn.resourcemanager.address</name>
<value>namenode:8032</value>
</property>
<property>
<name>yarn.resourcemanager.schedular.address</name>
<value>namenode:8030</value>
</property>

<property>
<name>yarn.resourcemanager.resource-tracker.address</name>
<value>namenode:8025</value>
</property>
</configuration>

```


## to start yarn resource manager

yarn -daemon start resourcemanager

