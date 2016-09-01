# MongoDB

![](img/MongoDB.png) 

版本：v3.2.3

MongoDB 是一个基于分布式文件存储的数据库。支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。

## MongoDB 后端服务

### 申请 MongoDB 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### MongoDB 仪表盘

![](img/MongoDB_Dashboard.png) 

### MongoDB 实例环境变量举例

- BSI:

```
- name: BSI_MONGODB_MONGODBTEST_HOST  value: dashboard.servicebroker.dataos.io- name: BSI_MONGODB_MONGODBTEST_PORT  value: "27017"- name: BSI_MONGODB_MONGODBTEST_URI  value: mongodb://b85d6cb62579d3d4e6ffea12f8c0c33e:d7ca80c2cb87c857080dabffcfc478e1@dashboard.servicebroker.dataos.io:27017/2a1ce30a-6aa7-11e6-867a-fa163d0e0615- name: BSI_MONGODB_MONGODBTEST_NAME  value: 2a1ce30a-6aa7-11e6-867a-fa163d0e0615- name: BSI_MONGODB_MONGODBTEST_USERNAME  value: b85d6cb62579d3d4e6ffea12f8c0c33e- name: BSI_MONGODB_MONGODBTEST_PASSWORD  value: d7ca80c2cb87c857080dabffcfc478e1
```

- JSON:

```
{
  "MongoDB": [
    {
      "name": "mongodb-test", 
      "label": "", 
      "plan": "Experimental", 
      "credentials": {
        "Host": "dashboard.servicebroker.dataos.io", 
        "Name": "2a1ce30a-6aa7-11e6-867a-fa163d0e0615", 
        "Password": "d7ca80c2cb87c857080dabffcfc478e1", 
        "Port": "27017", 
        "Uri": "mongodb://b85d6cb62579d3d4e6ffea12f8c0c33e:d7ca80c2cb87c857080dabffcfc478e1@dashboard.servicebroker.dataos.io:27017/2a1ce30a-6aa7-11e6-867a-fa163d0e0615", 
        "Username": "b85d6cb62579d3d4e6ffea12f8c0c33e", 
        "Vhost": ""
      }
    }
  ]
}
```

### 使用 MongoDB 实例

- 创建 bs 并绑定可以得到 url，username，dbname，password。

## 其他文档

- 官方网站： https://www.mongodb.com/- 官方文档（英）： https://docs.mongodb.com/manual/- 官方文档（中）： https://docs.mongodb.com/manual-zh/- API 文档： http://api.mongodb.com/