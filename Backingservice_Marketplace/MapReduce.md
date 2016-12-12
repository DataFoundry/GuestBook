# MapReduce

![](img/MapReduce.png)

版本：v2.7.1

Hadoop MapReduce是一个可以快速编写能够在大规模集群(数千节点)上处理大规模数据(TB级)的可靠的，容错的应用的软件框架。

## MapReduce后端服务

### 申请MapReduce实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### MapReduce仪表盘

![](img/mapreduce_dashboard.png)

### MapReduce实例环境变量举例

- BSI:

```
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_URI
      value: http://36.110.132.55:8088
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_NAME
      value: root.b2cf1fc3-cabc-4c64-982d-c39365ca0c4b:/user/dc5f8782-8462-11e6-8852-fa163d0e0615
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_USERNAME
      value: serviceinstance_9046f955-067e-4a6d-9052-9134967275cf@ASIAINFO.COM
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_PASSWORD
      value: 8268edc5-1db7-4437-9839-20276ab1b308
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_HOST
      value: hadoop-2.jcloud.local
    - name: BSI_MAPREDUCE_MAPREDUCEDEMO_PORT
      value: 8088
```

- JSON:

```
{
    "MapReduce": [
        {
            "credentials": {
                "Host": "hadoop-2.jcloud.local",
                "Name": "root.b2cf1fc3-cabc-4c64-982d-c39365ca0c4b:/user/dc5f8782-8462-11e6-8852-fa163d0e0615",
                "Password": "8268edc5-1db7-4437-9839-20276ab1b308",
                "Port": "8088",
                "Uri": "http://36.110.132.55:8088",
                "Username": "serviceinstance_9046f955-067e-4a6d-9052-9134967275cf@ASIAINFO.COM",
                "Vhost": ""
            },
            "label": "",
            "name": "mapreducedemo",
            "plan": "shared"
        }
    ]
}
```

### 使用MapReduce实例

- 使用HDFS实例与服务绑定返回的BSI_MAPREDUCE_MAPREDUCEDEMO_URI, BSI_MAPREDUCE_MAPREDUCEDEMO_NAME, BSI_MAPREDUCE_MAPREDUCEDEMO_USERNAME, BSI_MAPREDUCE_MAPREDUCEDEMO_PASSWORD, BSI_MAPREDUCE_MAPREDUCEDEMO_HOST, BSI_MAPREDUCE_MAPREDUCEDEMO_PORT接MapReduce实例，环境变量说明如下：
    - BSI_MAPREDUCE_MAPREDUCEDEMO_URI: Yarn ResourceManager的URI
    - BSI_MAPREDUCE_MAPREDUCEDEMO_NAME: MapReduce服务实例的资源,包括Yarn的资源队列和HDFS的目录,以(:)分隔
    - BSI_MAPREDUCE_MAPREDUCEDEMO_USERNAME: MapReduce实例的用户名
    - BSI_MAPREDUCE_MAPREDUCEDEMO_PASSWORD: MapReduce实例的用户密码
    - BSI_MAPREDUCE_MAPREDUCEDEMO_HOST: Yarn ResourceManager的主机名
    - BSI_MAPREDUCE_MAPREDUCEDEMO_PORT: Yarn ResourceManager的端口

- 构建MapReduce应用容器基于Yarn Client镜像(registry.dataos.io/ocdp/yarn-client), Datafoundry提供的Yarn Client镜像为用户容器提供了Yarn Client相关的依赖包和集群配置

- 在构建MapReduce应用容器时,将用户的MapReduce作业的jar包拷贝到容器中

- 在MapReduce应用容器中, 利用Broker注入的Credential信息(BSI_MAPREDUCE_MAPREDUCEDEMO_USERNAME/BSI_MAPREDUCE_MAPREDUCEDEMO_PASSWORD), 使用KERBEROS命令行完成身份认证;
  - 用户认证亦可以在用户应用中通过代码方式进行:
      - 利用Broker注入的Credential信息(BSI_MAPREDUCE_MAPREDUCEDEMO_USERNAME/BSI_MAPREDUCE_MAPREDUCEDEMO_PASSWORD),
      构造javax.security.auth.Subject对象;
      - 通过Hadoop的UserGroupInformation.loginUserFromSubject方法获取Kerberos票据

- 在MapReduce应用容器中, 通过Yarn Client的命令行(yarn jar命令)提交用户的MapReduce作业到OCDP集群中
    - 在依赖的Yarn Client镜像中已经配置了Yarn集群以及HDFS集群的URL,所以通过yarn jar方式提交的MapReduce作业将被提交到OCDP集群中的Broker为用户分配的队列中

- 具体可以参考例子: https://github.com/asiainfoLDP/datafoundry_ocdp_mapreduce_demo

## 其他文档

- 官方文档： https://hadoop.apache.org/docs/r2.7.1/
- 帮助文档： http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
- API文档： http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html
