# 内部Bug清单

本文档仅面向团队内部，用于记录测试遇到的bug和修复进度



## Web

### Bug

- [x] 创建活动仍然有“加入是否需要审核”项

- [x] 搜索功能没有完成

- [x] 不能修改正在进行和已经结束的活动，会显示“开始时间不能早于当前时间”

- [x] 除了第一个活动，其他活动的编辑都点不开

- [x] 批量删除活动，实际上管理端和小程序端这些活动被删除, 但是会显示“部分活动未删除，请重新尝试”的窗口

- [x] 批量删除评论，实际上管理端和小程序端这些评论被删除, 但是会显示“部分评论未删除，请重新尝试”的窗口

- [x] 批量删除反馈，实际上管理端和小程序端这些反馈被删除, 但是会显示“部分反馈未删除，请重新尝试”的窗口

- [x] 添加组织成功后，提示框“确定”按钮点击无反应

- [x] 组织审核、评论管理、反馈管理页面的刷新按钮只有最上面一点能点到

- [x] 创建组织后没有管理员

- [x] 可以在博雅和个人版块下创建组织

- [x] 部分活动种类显示为undefined，编辑页一直在加载

- [x] 活动编辑页面有日历消失问题

  



### 体验项

- [x] 各个列表以时间倒序排列更好
- [x] 创建活动时，板块的下拉项的测试选项需删除
- [ ] 添加成功活动后，“信息输入”窗口没有自动关闭
- [x] 评论列表没有区分活动开始前和开始后的评论（建议把活动开始前的评分由“空白的五个星”换为“活动开始前的评论无评分”，以示区分）
- [x] 反馈管理，顶栏将“用户”改为“用户id”



## 小程序

### Bug

- [x] 用户反馈界面下错误显示“组织基本信息”
- [x] 创建组织后提示显示不完整。
- [x] 关注博雅版块后在“关注”页面没有博雅（组织和活动列表都没有）
- [x] ~~当评论过长，再次打开编辑，之前的评论显示不全~~（存疑）
- [x] 日程-活动列表：用活动名无法搜索到报名的活动
- [x] 社团，学生会，志愿下的活动没有显示“id”
- [x] 活动编辑页面，将类别选择为新建类别后再选择原有的类别，新类别的输入框不会消失
- [x] 无法删除活动（报错在accessPolicy的317行）
- [x] 用户提交验证按钮没反应
- [x] 用户参与活动取消未收到通知
- [ ] 



### 体验项

- [x] ~~首页“推荐”、“地图”的点击范围较小~~（不是bug是feature）
- [x] 组织信息编辑报错提醒简陋
- [x] 组织成员管理界面，组织名建议用不同样式标出
- [x] 未报名的活动不应能评论
- [ ] 



## 后端

### Bug

- [ ] 



### 体验项

- [ ] 
- [ ] 

