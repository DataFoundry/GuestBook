# Hive

![](img/Hive.png)

版本：v1.2.1

Hive是一个可以通过SQL去读写，管理存储在分布式存储系统上的大规模数据集的数据仓库解决方案。

## Hive后端服务

### 申请Hive实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Hive仪表盘

无

### Hive实例环境变量举例

- BSI:

```
    - name: BSI_HIVE_HIVEDEMO_URI
      value: jdbc:hive2://36.110.132.55:10000/default;principal=hive/hadoop-2.jcloud.local@ASIAINFO.COM
    - name: BSI_HIVE_HIVEDEMO_NAME
      value: 10c6953c86d811e68852fa163d0e0615
    - name: BSI_HIVE_HIVEDEMO_USERNAMEE
      value: serviceinstance_b6561384-2a69-43cd-8cd7-345f93dc0b73@ASIAINFO.COM
    - name: BSI_HIVE_HIVEDEMO_PASSWORD
      value: 4c2b4931-aa2e-4870-ba03-bb80b3939ff2
    - name: BSI_HIVE_HIVEDEMO_HOST
      value: 36.110.132.55
    - name: BSI_HIVE_HIVEDEMO_PORT
      value: 10000
```

- JSON:

```
{
    "Hive": [
        {
            "credentials": {
                "Host": "36.110.132.55",
                "Name": "10c6953c86d811e68852fa163d0e0615",
                "Password": "4c2b4931-aa2e-4870-ba03-bb80b3939ff2",
                "Port": "10000",
                "Uri": "jdbc:hive2://36.110.132.55:10000/default;principal=hive/hadoop-2.jcloud.local@ASIAINFO.COM",
                "Username": "serviceinstance_b6561384-2a69-43cd-8cd7-345f93dc0b73@ASIAINFO.COM",
                "Vhost": ""
            },
            "label": "",
            "name": "hivedemo",
            "plan": "shared"
        }
    ]
}

```


### 使用Hive实例

- 使用HDFS实例与服务绑定返回的BSI_HIVE_HIVEDEMO_URI, BSI_HIVE_HIVEDEMO_NAME, BSI_HIVE_HIVEDEMO_USERNAME, BSI_HIVE_HIVEDEMO_PASSWORD, BSI_HIVE_HIVEDEMO_HOST, BSI_HIVE_HIVEDEMO_PORT接Hive实例，环境变量说明如下：
    - BSI_HIVE_HIVEDEMO_URI: Hive实例的JDBC URI
    - BSI_HIVE_HIVEDEMO_NAME: Hive的数据库名
    - BSI_HIVE_HIVEDEMO_USERNAME: Hive实例的用户名
    - BSI_HIVE_HIVEDEMO_PASSWORD: Hive实例的用户密码
    - BSI_HIVE_HIVEDEMO_HOST: HiveServer2的主机名
    - BSI_HIVE_HIVEDEMO_PORT: HiveServer2的端口

- 在服务代码中,通过代码方式(以JAVA为例)获取Kerberos票据:
    - 利用Broker注入的Credential信息(BSI_HIVE_HIVEDEMO_USERNAME/BSI_HIVE_HIVEDEMO_PASSWORD),
    构造javax.security.auth.Subject对象;
    - 通过Hadoop的UserGroupInformation.loginUserFromSubject方法获取Kerberos票据

- 在服务代码中,根据Broker注入的Hive的JDBC连接信息通过Hive的JDBC接口访问Broker为用户分配的数据库, JDBC connection string如下:
    ```
    jdbc:hive2://${BSI_HIVE_HIVEDEMO_HOST}:${BSI_HIVE_HIVEDEMO_PORT}/${BSI_HIVE_HIVEDEMO_NAME};principal=${BSI_HIVE_HIVEDEMO_USERNAME}"
    ```

## 其他文档

- 官方文档： http://hive.apache.org/
- 帮助文档： https://cwiki.apache.org/confluence/display/Hive/GettingStarted
- API文档： http://hive.apache.org/javadocs/r1.2.1/api/index.html
