# 数据库基本表定义

## 概述

* 实体
  * 一般性的）用户、活动、组织、版块、评论

  * （请求性质的）报名活动申请、管理员申请、版块创建申请，…………TODO

* 关系

  * TODO：这里可以画个图（E-R图？）
  * 用户和加入的活动：多对多
  * ~~用户和管理的活动：多对多（个人活动直接对应，其他活动通过组织对应）~~
  * 用户和关注的组织：多对多
  * 组织管理员和管理的组织：多对多
  * 组织负责人和管理的组织：一对多
  * 用户和评论：一对多
  * 活动和组织：多对一
  * 活动和版块：多对一（在部分版块中直接对应，其他版块中通过组织对应）
  * 活动和评论：一对多
  * 评论和被回复的评论：多对一
  * 组织和版块：多对一
  * TODO：申请相关的关系





## 实体

1. 用户（继承User类）

| 属性名   | 数据类型 | 初始化方式   | 可修改 | 待讨论的问题      | 备注         |
| :------- | -------- | ------------ | ------ | ----------------- | ------------ |
| id       | id       | 自动生成     |        |                   |              |
| 昵称     | 字符串   | 微信授权登录 | √      |                   |              |
| 个性签名 | 字符串   | 用户设置     | √      |                   |              |
| 密码     | 字符串   | 用户设置     | √      | 必要性？          | 加密         |
| 学号     | 字符串   | 实名认证     |        | 必要性？          |              |
| 学院     | id       | 实名认证     |        | 必要性？          | 对应学院编号 |
| 姓名     | 字符串   | 实名认证     |        | 必要性？          |              |
| 邮箱     | 字符串   | 用户设置     |        | 必要性？验证码？× |              |
| 头像     | 图片     | 微信授权登录 | √      |                   |              |
|          |          |              |        |                   |              |
|          |          |              |        |                   |              |



2. 活动

| 属性名                 | 数据类型   | 初始化方式 | 可修改 | 待讨论的问题 | 备注                                                         |
| :--------------------- | ---------- | ---------- | ------ | ------------ | ------------------------------------------------------------ |
| id                     | id         | 自动生成   |        |              |                                                              |
| 名称                   | 字符串     | 用户设置   | √      |              |                                                              |
| 分类                   | id/字符串  | 用户设置   |        |              | 对应分类编号                                                 |
| 开始时间               | 时间       | 用户设置   | √      |              |                                                              |
| 结束时间               | 时间       | 用户设置   | √      |              |                                                              |
| 发布时间               | 时间       | 自动生成   |        |              |                                                              |
| 人数限制               | integer    | 用户设置   | √      |              |                                                              |
| 地点                   | 位置经纬度 | 用户设置   | √      |              |                                                              |
| 描述                   | 字符串     | 用户设置   | √      |              |                                                              |
| ~~报名需要审核？~~待定 | boolean    | 用户设置   | √      |              |                                                              |
| 当前人数               | integer    | 自动生成   | √      |              |                                                              |
| 是固定活动             | boolean    | 自动生成   |        |              |                                                              |
| 点赞数                 | integer    | 自动生成   | √      | 必要性？     |                                                              |
| 评论数量               | integer    | 自动生成   | √      |              |                                                              |
| 是个人/组织活动        | boolean    | 用户设置   |        |              | 固定活动时本项无意义                                         |
| 所属组织               | id         | 用户设置   |        |              | 可据此查询管理员；非组织活动时为None(-1)                     |
| 所属个人               | id         | 自动生成   |        |              | 非用户活动时为None(-1)                                       |
| 所属版块               | id         | 自动生成   |        |              | 固定活动和个人活动时为直接所属版块；组织活动时为所属组织的所属板块 |



3. 组织

| 属性名       | 数据类型 | 初始化方式 | 可修改 | 待讨论的问题 | 备注         |
| :----------- | -------- | ---------- | ------ | ------------ | ------------ |
| id           | id       | 自动生成   |        |              |              |
| 名称         | 字符串   | 用户设置   | √      |              |              |
| 描述         | 字符串   | 用户设置   | √      |              |              |
| 创建时间     | 日期     | 自动生成   |        |              |              |
| 负责人       | id       | 自动生成   | √      |              |              |
| 所属版块     | id       | 用户设置   |        |              | 对应版块编号 |
| 头像         | 图片     | 用户设置   | √      |              |              |
| ~~点赞数~~   | integer  | 自动生成   | √      | 必要性？     |              |
| ~~活动数量~~ | integer  | 自动生成   | √      |              |              |



4. 评价

| 属性名     | 数据类型 | 初始化方式 | 可修改 | 待讨论的问题 | 备注 |
| :--------- | -------- | ---------- | ------ | ------------ | ---- |
| 所属活动   | id       | 自动生成   |        |              |      |
| 所属用户   | id       | 自动生成   |        |              |      |
| 内容       | 字符串   | 用户设置   | √      |              |      |
| 发布时间   | 时间     | 自动生成   |        |              |      |
| 点赞数     | integer  | 自动生成   | √      | 必要性？     |      |
| 回复的评论 | id       | 用户设置   |        | 必要性？     |      |
| 是否置顶   | boolean  | 自动生成   | √      | 必要性？     |      |
|            |          |            |        |              |      |



5. 版块

| 属性名   | 数据类型 | 初始化方式 | 可修改 | 待讨论的问题 | 备注                 |
| :------- | -------- | ---------- | ------ | ------------ | -------------------- |
| id       | id       | 自动生成   |        |              |                      |
| 名称     | id       | 自动生成   |        |              |                      |
| 组织数量 | integer  | 自动生成   | √      |              | 对于博雅等版块无意义 |
| 活动数量 | integer  | 自动生成   | √      |              | 所有组织活动数量之和 |



6. 超级管理员

| 属性名 | 数据类型 | 初始化方式 | 可修改 | 待讨论的问题     | 备注 |
| :----- | -------- | ---------- | ------ | ---------------- | ---- |
| id     | id       | 自动生成   |        |                  |      |
| 用户名 | 字符串   | 自动生成   |        | 是否需要多用户？ |      |
| 密码   | 字符串   | 自动生成   | √      |                  | 加密 |



7. 管理员申请（？不确定 TODO）

| 组织id | 用户id | 申请理由 |
| ------ | ------ | -------- |
|        |        |          |



## 多对多关系

1. 用户—加入的活动

| 用户id | 活动id |
| ------ | ------ |
|        |        |



2. 用户—关注的组织

| 用户id | 组织id |
| ------ | ------ |
|        |        |



3. 组织管理员—管理的组织

| 用户id | 组织id | 职称   |
| ------ | ------ | ------ |
|        |        | 字符串 |



TODO 点赞 多对多关系表