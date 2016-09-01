# Greenplum

![](img/Greenplum.jpg) 

版本：v4.3.7

Greenplum 是 Pivotal 开源的 MPP 数据库。提供 PD 级别数据量的强大和快速分析能力，特别是面向大数据方面的分析能力，支持大数据的超高性能分析查询。

## Greenplum 后端服务

### 申请 Greenplum 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Greenplum 仪表盘

![](img/Greenplum_Dashboard.png) 

### Greenplum 实例环境变量举例

- BSI:

```
- name: BSI_GREENPLUM_GREENPLUMTEST_USERNAME  value: u3c49b0527173612- name: BSI_GREENPLUM_GREENPLUMTEST_PASSWORD  value: pf094cc77dd5ba92- name: BSI_GREENPLUM_GREENPLUMTEST_HOST  value: greenplumshare.servicebroker.dataos.io- name: BSI_GREENPLUM_GREENPLUMTEST_PORT  value: "5432"- name: BSI_GREENPLUM_GREENPLUMTEST_URI  value: postgres://u3c49b0527173612:pf094cc77dd5ba92@greenplumshare.servicebroker.dataos.io:5432/d710fcbe5ab0f9fc- name: BSI_GREENPLUM_GREENPLUMTEST_NAME  value: d710fcbe5ab0f9fc
```

- JSON:

```
{
  "Greenplum": [
    {
      "name": "greenplum-test", 
      "label": "", 
      "plan": "Experimental", 
      "credentials": {
        "Host": "greenplumshare.servicebroker.dataos.io", 
        "Name": "d710fcbe5ab0f9fc", 
        "Password": "pf094cc77dd5ba92", 
        "Port": "5432", 
        "Uri": "postgres://u3c49b0527173612:pf094cc77dd5ba92@greenplumshare.servicebroker.dataos.io:5432/d710fcbe5ab0f9fc", 
        "Username": "u3c49b0527173612", 
        "Vhost": ""
      }
    }
  ]
}

```

### 使用 Greenplum 实例

- 创建 bs 并绑定可以得到 url，username，dbname，password。

## 其他文档

- 官方网站： http://www.oracle.com/technetwork/database/index.html- 官方文档： http://docs.oracle.com/cd/E11882_01/index.htm- API 文档： http://www.oracle.com/us/products/middleware/soa/api-management/overview/index.html