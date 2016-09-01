# RabbitMQ

![](img/RabbitMQ.png)

版本：v3.6.1

RabbitMQ 是流行的开源消息队列系统。用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗。

## RabbitMQ 后端服务

### 申请 RabbitMQ 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### RabbitMQ 仪表盘

![](img/RabbitMQ_Dashboard.png)


### RabbitMQ 实例环境变量举例

- BSI:

```
- name: BSI_RABBITMQ_RABBITMQTEST_URI  value: amqp://W61WK5VKpdI:7883eb598bf004063139148012847586@sb-rhcoe4ny3rxlo-rbbtmq.service-brokers.svc.cluster.local:5672- name: BSI_RABBITMQ_RABBITMQTEST_USERNAME  value: W61WK5VKpdI- name: BSI_RABBITMQ_RABBITMQTEST_PASSWORD  value: 7883eb598bf004063139148012847586- name: BSI_RABBITMQ_RABBITMQTEST_HOST  value: sb-rhcoe4ny3rxlo-rbbtmq.service-brokers.svc.cluster.local- name: BSI_RABBITMQ_RABBITMQTEST_PORT  value: "5672"
```

- JSON:

```
{
  "RabbitMQ": [
    {
      "name": "rabbitmq-test", 
      "label": "", 
      "plan": "standalone", 
      "credentials": {
        "Host": "sb-rhcoe4ny3rxlo-rbbtmq.service-brokers.svc.cluster.local", 
        "Name": "", 
        "Password": "7883eb598bf004063139148012847586", 
        "Port": "5672", 
        "Uri": "amqp://W61WK5VKpdI:7883eb598bf004063139148012847586@sb-rhcoe4ny3rxlo-rbbtmq.service-brokers.svc.cluster.local:5672", 
        "Username": "W61WK5VKpdI", 
        "Vhost": ""
      }
    }
  ]
}
```

### 使用 RabbitMQ 实例

- 使用 RabbitMQ 实例与服务绑定返回的 BSI_RABBITMQ_RABBITMQTEST_URI、BSI_RABBITMQ_RABBITMQTEST_USERNAME 和 BSI_RABBITMQ_RABBITMQTEST_PASSWORD 连接 RabbitMQ。

## 其他文档

- 官方文档： http://www.rabbitmq.com/
- 帮助文档： http://www.rabbitmq.com/documentation.html
- 官方教程： http://www.rabbitmq.com/getstarted.html
- API 文档： http://www.rabbitmq.com/releases/rabbitmq-java-client/v3.6.5/rabbitmq-java-client-javadoc-3.6.5/

