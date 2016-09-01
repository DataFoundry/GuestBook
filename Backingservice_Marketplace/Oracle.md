# Oracle

![](img/Oracle.gif) 

版本：v11.2

亚马逊 AWS 提供的 Oracle 关系型数据库。数据库系统可移植性好、使用方便、功能强，适用于各类大、中、小、微机环境。它是一种高效率、可靠性好的 适应高吞吐量的数据库解决方案。

## Oracle 后端服务

### 申请 Oracle 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Oracle 仪表盘

无

### Oracle 实例环境变量举例

- BSI:

```
- name: BSI_ORACLE_ORACLETEST_PORT
  value: "1521"- name: BSI_ORACLE_ORACLETEST_URI  value: tsdb9bdd14707a2b:p3f37848c72f35f8@oracle-instance.dataos.io:1521/ORCL- name: BSI_ORACLE_ORACLETEST_NAME  value: tsdb9bdd14707a2b- name: BSI_ORACLE_ORACLETEST_USERNAME  value: ua2618ecf8e9114a- name: BSI_ORACLE_ORACLETEST_PASSWORD  value: p3f37848c72f35f8- name: BSI_ORACLE_ORACLETEST_HOST  value: oracle-instance.dataos.io
```

- JSON:

```
{
  "Oracle": [
    {
      "name": "oracle-test", 
      "label": "", 
      "plan": "shared", 
      "credentials": {
        "Host": "oracle-instance.dataos.io", 
        "Name": "tsdb9bdd14707a2b", 
        "Password": "p3f37848c72f35f8", 
        "Port": "1521", 
        "Uri": "tsdb9bdd14707a2b:p3f37848c72f35f8@oracle-instance.dataos.io:1521/ORCL", 
        "Username": "ua2618ecf8e9114a", 
        "Vhost": ""
      }
    }
  ]
}
```

### 使用 Oracle 实例

- 使用 bind 返回的 uri 连接串连接 oracle。- bind 返回的 name 环境变量为表空间名字。

## 其他文档

- 官方网站： http://www.oracle.com/technetwork/database/index.html- 官方文档： http://docs.oracle.com/cd/E11882_01/index.htm- API 文档： http://www.oracle.com/us/products/middleware/soa/api-management/overview/index.html