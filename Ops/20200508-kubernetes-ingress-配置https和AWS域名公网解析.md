___
- FileName: kubernetes-ingress-配置https和域名公网解析.md
- Author: huangch96@qq.com
- Description: ---
- Create:2020-05-08 13:58:13
___

## 1. 什么是Ingress?

Kubernetes Ingress的概念，网络上很多文章也都说过。Ingress 其实就是解决负载均衡和虚拟主机的一些功能。传统方式我们如何实现虚拟主机和负载均衡呢，我们会使用
Nginx或者HaProxy来实现这些功能。所以说Ingress就是一个7层负载均衡器的作用，它和kubernetes service 的区别就是Service 只可以负载4层的负载均衡服务，而且
负载的对象抽象层面来说都是pod，但是Ingress 是7层的负载均衡器，进行一个虚拟主机的作用，根据url不同的path可以访问到不同的service，所以Ingress在很大一个层面
都是提供的虚拟主机的作用。同样的也在7层提供了LB的功能。本文不着重介绍Ingress和Service的实现原理，主要说一下在应用层如何配置https证书。

## 2. 创建证书secret
使用以下命令在对应namesapce建立你需要的绑定的https的证书secret文件

```bash
kubectl create secret tls SCR_NAME --key KEY-FILE --cert PEM-FILE  -n NAMESPACE
```

## 3. 创建域名的Ingress 服务

创建对应的域名的Ingress 服务
```yml
{
  "kind": "Ingress",
  "apiVersion": "extensions/v1beta1",
  "metadata": {
    "name": "SER-NAME",
    "namespace": "prod",
    "annotations": {
      "nginx.ingress.kubernetes.io/proxy-body-size": "0",
      "nginx.ingress.kubernetes.io/proxy-read-timeout": "3600",
      "nginx.ingress.kubernetes.io/proxy-send-timeout": "3600"
    }
  },
  "spec": {
    "tls": [
      {
        "hosts": [
          "FQDN-NAME"
        ],
        "secretName": "SCR_NAME"
      }
    ],
    "rules": [
      {
        "host": "FQDN",
        "http": {
          "paths": [
            {
              "path": "/PATH",
              "backend": {
                "serviceName": "SERVICE_NAME",
                "servicePort": PORT
              }
            },
            {
              "path": "/",
              "backend": {
                "serviceName": "SERVICE_NAME",
                "servicePort": PORT
              }
            }
          ]
        }
      }
    ]
  },
  "status": {
    "loadBalancer": {}
  }
}
```

## 4. 创建Ingress Service

因为需要使用公网解析域名，所以需要通过Ingress Serveice 绑定aws elb，所以在Ingress namespace 下创建一个Service，在云厂商创建公网ELB，
所以建立以下服务

```yml
kind: Service
apiVersion: v1
metadata:
  name: ingress-nginx-ext
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx-ext
    app.kubernetes.io/part-of: ingress-nginx-ext
  annotations:
    # Enable PROXY protocol
    #service.beta.kubernetes.io/aws-load-balancer-internal: "false"
    #service.beta.kubernetes.io/aws-load-balancer-internal: "0.0.0.0/0"
    service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: "tcp"
    # Ensure the ELB idle timeout is less than nginx keep-alive timeout. By default,
    # NGINX keep-alive is set to 75s. If using WebSockets, the value will need to be
    # increased to '3600' to avoid any potential issues.
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "60"
spec:
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: ingress-nginx-ext
    app.kubernetes.io/part-of: ingress-nginx-ext
  ports:
    - name: http
      port: 80
      targetPort: http
    - name: https
      port: 443
      targetPort: https
```

## 5. 进行域名解析
在对应的域名解析厂商解析域名CNAME到对应的LB
