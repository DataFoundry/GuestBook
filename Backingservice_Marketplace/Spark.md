# Spark

![](img/Spark.png)

版本：v1.6.0

Spark 是 UC Berkeley AMP lab 所开源的类 Hadoop MapReduce 的通用并行框架。Spark 启用了内存分布数据集，除了能够提供交互式查询外，还可以优化迭代工作负载。

## Spark 后端服务

### 申请 Spark 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Spark 仪表盘

![](img/Spark_Dashbroad.png)


### Spark 实例环境变量举例

- BSI:

```
- name: BSI_SPARK_SPARKDEMO_URI
  value: http://36.110.132.55:8088
- name: BSI_SPARK_SPARKDEMO_NAME
  value: root.b0d85230-fd47-41f0-a317-23bebf3701f6:bd9b843986dc11e68852fa163d0e0615
- name: BSI_SPARK_SPARKDEMO_USERNAME
  value: serviceinstance_040e8122-6d3f-4a89-a23e-75e9d73a29c3@ASIAINFO.COM
- name: BSI_SPARK_SPARKDEMO_PASSWORD
  value: 7a36ebcf-bbaa-4058-8882-ff7dd7602e4c
- name: BSI_SPARK_SPARKDEMO_HOST
  value: hadoop-2.jcloud.local
- name: BSI_SPARK_SPARKDEMO_PORT
  value: 8088
```

- JSON:

```
{
    "Spark": [
        {
            "credentials": {
                "Host": "hadoop-2.jcloud.local",
                "Name": "root.b0d85230-fd47-41f0-a317-23bebf3701f6:bd9b843986dc11e68852fa163d0e0615",
                "Password": "7a36ebcf-bbaa-4058-8882-ff7dd7602e4c",
                "Port": "8088",
                "Uri": "http://36.110.132.55:8088",
                "Username": "serviceinstance_040e8122-6d3f-4a89-a23e-75e9d73a29c3@ASIAINFO.COM",
                "Vhost": ""
            },
            "label": "",
            "name": "sparkdemo",
            "plan": "shared"
        }
    ]
}
```

### 使用 Spark 实例

- 使用HDFS实例与服务绑定返回的BSI_SPARK_SPARKDEMO_URI, BSI_SPARK_SPARKDEMO_NAME, BSI_SPARK_SPARKDEMO_USERNAME, BSI_SPARK_SPARKDEMO_PASSWORD, BSI_SPARK_SPARKDEMO_HOST, BSI_SPARK_SPARKDEMO_PORT接Spark实例，环境变量说明如下：
    - BSI_SPARK_SPARKDEMO_URI: Yarn ResourceManager的URI
    - BSI_SPARK_SPARKDEMO_NAME: Spark实例的资源,包括一个Yarn的资源队列和一个Hive的数据库,名称以(:)分隔
    - BSI_SPARK_SPARKDEMO_USERNAME: Spark实例的用户名
    - BSI_SPARK_SPARKDEMO_PASSWORD: Spark实例的用户密码
    - BSI_SPARK_SPARKDEMO_HOST: Yarn ResourceManager的主机名
    - BSI_SPARK_SPARKDEMO_PORT: Yarn ResourceManager的端口

- 在服务代码中,通过代码方式(以JAVA为例)获取Kerberos票据:
    - 利用Broker注入的Credential信息(BSI_SPARK_SPARKDEMO_USERNAME/BSI_SPARK_SPARKDEMO_PASSWORD),
    构造javax.security.auth.Subject对象;
    - 通过Hadoop的UserGroupInformation.loginUserFromSubject方法获取Kerberos票据

- 在服务代码中,根据Broker注入的Yarn的URI(BSI_SPARK_SPARKDEMO_URI)通过代码方式(以JAVA为例)提交MapReduce作业到Broker为用户分配的队列中

- Spark SQL应用可以通过Spark SQL的JDBC接口访问Broker为用户分配的数据库

## 其他文档

- 官方文档： http://spark.apache.org/
- 帮助文档： http://spark.apache.org/docs/1.6.0/
- API 文档： http://spark.apache.org/examples.html



