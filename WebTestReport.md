# 一苇以航—Web端 测试报告

## 版本历史

| 版本 | 作者 | 更新日期 | 更新说明 |
| ---- | ---- | -------- | -------- |
|      |      |          |          |
|      |      |          |          |



## 目录

[TOC]

## 1 引言

### 1.1 标识

标题：《一苇以航—Web端 测试报告》。

### 1.2 文档概述

本文档为一苇以航Web端的测试报告，用于描述Web端的测试情况并记录测试结果。

### 1.3 项目概述

#### 1.3.1 被测软件概述

a) 被测软件名称为“一苇以航”，为北航师生提供活动发布和社交平台。

b) 被测软件主要由用户管理、版块管理、组织管理、活动管理、评论管理、反馈管理等页面构成。

被测软件的功能主要包括：被测软件的功能主要包括：登录、删除用户、审核组织审批、编辑和删除组织、编辑和删除活动、删除评论、查看和删除用户反馈等。

c) 被测软件为网页，可以运行在现代主流浏览器上。

#### 1.3.2 评测任务概述

| 序号 | 被测对象 | 测试级别 | 测试场地           |
| ---- | -------- | -------- | ------------------ |
| 1    | 登录界面 | 功能测试 | 软件评测方仿真环境 |
| 2    | 用户管理 | 功能测试 | 软件评测方仿真环境 |
| 3    | 版块管理 | 功能测试 | 软件评测方仿真环境 |
| 4    | 组织管理 | 功能测试 | 软件评测方仿真环境 |
| 5    | 活动管理 | 功能测试 | 软件评测方仿真环境 |
| 6    | 评论管理 | 功能测试 | 软件评测方仿真环境 |
| 7    | 反馈管理 | 功能测试 | 软件评测方仿真环境 |





## 2 参考文献

| 作者           | 文档名称                 | 单位         | 日期    |
| -------------- | ------------------------ | ------------ | ------- |
| 马瑞芳，王会燃 | 计算机软件测试方法的研究 | 西安交通大学 | 2003-12 |



## 3 术语

| 缩写、术语                          | 解释                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| 版块(Forum)                         | 活动的顶层分类，例如博雅、社团活动、志愿等，由超级管理员设定，无法随意添加或修改 |
| 组织(Organization, ORG)             | 从属于版块，由用户创建、经过审核后发布，创建者自动成为组织管理员 |
| 活动(Activity, ACT)                 | 从属于组织（社团、学生会等版块下）或版块（博雅、演出等官方版块，以及*个人版块*），由组织/个人发布 |
| 固定活动(Official Activity, OA)     | 具有（一定的）官方性质的活动，例如博雅、演出等，由超级管理员通过爬虫等渠道获取并更新至活动列表，不归特定组织所有 |
| 非固定活动(Unofficial Activity, UA) | 包括*组织活动*（由组织管理员代表组织发布）及*个人活动*（由个人发布），例如社团活动、约球约自习等 |



## 4 测试资源

### 4.1 测试环境

| 软件环境                         | 硬件环境           |
| -------------------------------- | ------------------ |
| Safari 14.0.3; Mac OS 11.2.3     | MacBook Pro 2020   |
| Chrome 90.0.4430.212 ;Windows 10 | LENOVO ideapad 300 |

### 4.2 测试工具

无



## 5 测试总结

### 5.1 测试时间

2021年5月16日至2021年5月26日。

### 5.2 测试人员

乐洋、开聚实、王肇凯。

### 5.3 测试执行情况

TODO

### 5.4 测试结果

共TODO个测试用例，TODO个已通过，TODO未通过，TODO个待完成。

### 5.5 未执行测试用例的原因说明

TODO



## 6 评估与建议

TODO



## 7 测试记录

### 7.0 模板

| 测试目的     |              |
| ------------ | ------------ |
| **用例**     | **测试结果** |
|              |              |
|              |              |
| **测试结论** |              |

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">开聚实</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>


### 

### 7.1 登录页面

#### 7.1.1 管理登录

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试管理员登录功能</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td>1</td>
        <td>正常登录</td>
        <td>输入正确用户名与密码</td>
        <td>登录成功，跳转到首页</td>
        <td>登录成功，跳转到首页</td>
        <td>无</td>
    </tr>
    <tr>
        <td>2</td>
        <td>空用户名</td>
        <td>不输入用户名</td>
        <td>登录失败，提示“必填项不能为空”</td>
        <td>登录失败，提示“必填项不能为空”</td>
        <td>无</td>
    </tr>
    <tr>
        <td>3</td>
        <td>错误用户名</td>
        <td>输入错误用户名</td>
        <td>登录失败，提示“用户名或密码错误”</td>
        <td>登录失败，提示“用户名或密码错误”</td>
        <td>无</td>
    </tr>
    <tr>
        <td>4</td>
        <td>空密码</td>
        <td>不输入密码</td>
        <td>登录失败，提示“必填项不能为空”</td>
        <td>登录失败，提示“必填项不能为空”</td>
        <td>无</td>
    </tr>
    <tr>
        <td>5</td>
        <td>错误密码</td>
        <td>输入错误密码</td>
        <td>登录失败，提示“用户名或密码错误”</td>
        <td>登录失败，提示“用户名或密码错误”</td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">开聚实</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>
### 

### 7.2 用户管理页面

#### 7.2.1

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">开聚实</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>





### 7.3 版块管理页面





### 7.4 组织管理页面



### 7.5 活动管理页面

#### 7.5.1 查看活动列表

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>


#### 7.5.2 搜索活动

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.5.3 添加活动

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.5.4 编辑活动

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.5.5 删除活动

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.5.6 批量删除活动

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>




### 7.6 评论管理页面

#### 7.6.1 查看评论列表

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.6.2 搜索评论

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.6.3 查看评论详情

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.6.4 删除评论

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.6.5 批量删除评论

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>




### 7.7 反馈管理页面

#### 7.7.1 查看反馈列表

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.7.2 搜索反馈

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.7.3 查看反馈详情

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.7.4 删除反馈

<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>

#### 7.7.5 批量删除反馈



<table>
    <tr>
        <th>测试目的</th>
        <td colspan="5">测试XXXX</td>
    </tr>
    <tr>
        <th>前提条件</th>
        <td colspan="5">无</td>
    </tr>
    <tr>
        <th>参考信息</th>
        <td colspan="2">无</td>
        <th>特殊说明</th>
        <td colspan="2">无</td>
    </tr>
    <tr>
        <th>用例编号</th>
        <th>用例说明</th>
        <th>输入/操作</th>
        <th>期望结果</th>
        <th>测试结果</th>
        <th>备注</th>
    </tr>
    <!-- >想插入更多行请复制以下内容</-->
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>无</td>
    </tr>
    <!-- >想插入更多行请复制以上内容</-->
    <tr>
        <th>测试结论</th>
        <td colspan="5">通过</td>
    </tr>
    <tr>
        <th>测试人员</th>
        <td colspan="2">乐洋</td>
        <th>测试日期</th>
        <td colspan="2">2021/5/23</td>
    </tr>
</table>