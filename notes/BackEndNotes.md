# 后端学习笔记

[TOC]

## Django基础

Django基础学习资料： 本地打开  	 ./django基础/index.html 

### DRF

[RESTful架构详解-菜鸟教程](https://www.runoob.com/w3cnote/restful-architecture.html)

DRF学习资料： 本地打开 	./DRF资料/index.html



## Django数据库

[使用默认sqlite3创建数据库](https://blog.csdn.net/qq_39248122/article/details/88864979)

[使用MySql创建数据库](https://blog.csdn.net/u011109881/article/details/51901032)

[Django对数据库操作](https://www.runoob.com/django/django-model.html)







## TODO 2021.4.5 wjr

- [ ] 组织头像上传方式网址还是保存到服务器某个路径的文件(确定属性类别写法)；
- [x] 用mysql数据库还是sqlite3(Django自带) 
  - [x] Mysql
- [x] 活动类别扩展 
  - [x] 活动类别改成表了





# TODO

优先级：数值越小表示优先级越高。

## 基本任务

- [ ] 继续完善基本接口功能（1，需求文档里的基本功能必须实现）

## 优化前端交换体验

- [x] 设置分页Pagination（2，对于返回列表的GET请求，分页可降低前端相应时间）
- [ ] 对于列表数据增加排序功能OrderingFilter（2，按照前端需求排好序返回）

## 优化性能

- [ ] 可将已结束的活动和未开始的活动分开，已经结束的活动访问量会比较少可以减少数据库表项，提升性能（4，仅个人设想，有时间可实现，可能实际项目数据不足，不需要优化）

## 权限认证

- [ ] 操作的权限认证（认证Authentication，权限Permissions），若管理端和用户端权限认证不能合并需将部分接口拆分（3，后端操作的安全性保证，没有时间可以不实现，前端不提供接口即可）

## 消息通知

- [ ] 后端定时给小程序提供通知服务（1，需求文档里的基本功能，必须实现）

## 静态数据

- [ ] 图片储存（1，需求文档里的基本功能，必须实现）

