# ZooKeeper

![](img/ZooKeeper.png)

版本：v3.4.8

ZooKeeper 是一个分布式的，开放源码的分布式应用程序协调服务。主要是用来解决分布式应用中经常遇到的一些数据管理问题。

## ZooKeeper 后端服务

### 申请 ZooKeeper 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### ZooKeeper 仪表盘

无

### ZooKeeper 实例的环境变量举例

* BSI:

```
- name: BSI_ZOOKEEPER_ZOOKEEPERTEST_USERNAME
  value: super
- name: BSI_ZOOKEEPER_ZOOKEEPERTEST_PASSWORD
  value: 37bfee9a5d26c077e9d73f3c21460504
- name: BSI_ZOOKEEPER_ZOOKEEPERTEST_HOST
  value: sb-vjk2uvnkkwvfk-zk.service-brokers.svc.cluster.local
- name: BSI_ZOOKEEPER_ZOOKEEPERTEST_PORT
  value: "2181"
```

* JSON:

```
{
  "ZooKeeper": [
    {
      "name": "zookeeper-test", 
      "label": "", 
      "plan": "standalone", 
      "credentials": {
        "Host": "sb-vjk2uvnkkwvfk-zk.service-brokers.svc.cluster.local", 
        "Name": "", 
        "Password": "37bfee9a5d26c077e9d73f3c21460504", 
        "Port": "2181", 
        "Uri": "", 
        "Username": "super", 
        "Vhost": ""
      }
    }
  ]
}

```

## 其他文档

- 官方文档： http://zookeeper.apache.org/
- 帮助文档： https://zookeeper.apache.org/doc/r3.4.8/
- API 文档： http://zookeeper.apache.org/doc/r3.4.8/api/index.html