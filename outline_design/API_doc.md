# 接口说明文档



[TOC]

## 分页请求说明

对于返回的是列表的请求，可以使用分页请求的方式。

**分页请求方法：**

在列表请求的`url`加上`limit`和`offset`参数。例如：http://127.0.0.1:8000/blocks/?limit=2&offset=0

- `limit`：表示请求页的大小
- `offset`：表示请求页的开始项（第一项为0），缺省表示从第一项开始

**响应内容：**

- `count`：表示该列表的总项数
- `next`：表示后一页请求的`url`，若此页为最后一页则此项的值为`null`
- `previous`：表示前一页请求的`url`，若此页为第一页则此项的值为`null`
- `results`：表示本页内容。

例如：

```json
{
    "count": 3,
    "next": "http://127.0.0.1:8000/blocks/?limit=2&offset=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "博雅"
        },
        {
            "id": 2,
            "name": "志愿"
        }
    ]
}
```



## 用户账户

### 用户登录 POST`userLogin/`

**权限**

用户端

**说明**

验证登录信息，在数据库中取得该用户信息，取得登录凭证`token`

**Request**

URL：http://127.0.0.1:8000/userLogin/

Body：

```json
{
	'code' : "sdgajhbdsjfwbejkf", //wx.login生成的code，需后端转换成openid
}
```

**Success Response**

状态码：200

Body：

```
{
	'status' : 0, 
	'userExist' : 1, //0为新注册，1为已存在用户
    'token' : 'some random token', //服务器返回的登录凭证，缓存在本地
    'email' : 'abcdef@buaa.edu.cn' / '', //邮箱，如果还未认证邮箱则返回空串
    'id' :  'user.id', //用户的id，缓存在本地
    'avatar' : 'xxx.com', //用户头像的url
    'sign' : 'xxxxx', //个性签名
    'name' : 'xxx', //用户名
}
```

**Error Response**

注：正常小程序运行过程不会发生，因为code是自动获取的。

状态码：400

Body：

```json
{
    'status' : 1,
    'errcode' : 'xxxxx', //微信服务接口返回的error code
    'msg' : 'xxxxxx', //微信服务接口返回的错误信息
}
```



### 注册用户信息 POST`userRegister/`

**权限**

用户端

**说明**

将用户的昵称和头像注册至数据库，若login返回userExist=1则调用此接口

**Request**

URL：http://127.0.0.1:8000/userRegister/

Body：

```json
{
	'id' : "sdgajhbdsjfwbejkf", //wx.login生成的code，需后端转换成openid
	'userInfo' : {} //内容参见https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/UserInfo.html
}
```

**Success Response**

状态码：200

```json
{
	'status' : 0
    
}
```



### 发送验证码邮件 POST`sendVerify/`

**权限**

用户端

**说明**

向指定邮箱发送验证码，缓存中保存邮箱和验证码配对信息

**Request**

URL：http://127.0.0.1:8000/sendVerify/

Body：

```json
{
	"email" : "abcde@buaa.edu.cn"
}
```

**Success Response**

状态码：200

Body:

```json
{
	"status" : 0,
    "msg" : 'Email send',
}
```





### 验证码验证 POST`verify/`

**权限**

用户端

**说明**

验证用户输入的验证码是否和邮箱对应，对应则在数据库中保存用户的邮箱（以后登录则不必认证）

**Request**

URL：http://127.0.0.1:8000/verify/

Body：

```json
{
	"verifyCode" : "wzkwzk",  //验证码
    "email" : "abcde@buaa.edu.cn", //验证邮箱
    "id" : "user.id" //用户的id
}
```

**Success Response**

状态码：200

Body：

```json
{
	"status" : 0,
    "msg" : "Valid Code"
}
```

**Error Response**

状态码：400

Body：

```json
{
    "status" : 1,
    "msg" : "Invalid Code"
}
```



## 用户

### 获取所有用户 GET `users/`

**权限**

管理端

**说明**

获取所有用户的信息

**Request**

URL：http://127.0.0.1:8000/users/

Request Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "nicheng111",
        "avatar": "touxiang111",
        "email": null,
        "sign": "sign111"
    },
    {
        "id": 2,
        "name": "nicheng2",
        "avatar": "touxiang2",
        "email": null,
        "sign": "sign2"
    }
]
```

**Error Response**

无



### 获取指定用户信息 GET `users/{id}/`

**权限**

用户端，管理端

**说明**

获取编号为id的用户的信息，返回内容包括id，名称，头像地址，邮箱，个性签名

**Request**

URL：http://127.0.0.1:8000/users/1/（表示获取id=1的用户的信息）

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "name": "nicheng111",
    "avatar": "touxiang111",
    "email": null,
    "sign": "sign111"
}
```

**Error Response**

①

对应id的用户不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 删除指定用户 DELETE `users/{id}/`

**权限**

用户端，管理端

**说明**

删除编号为id的用户

**Request**

URL：http://127.0.0.1:8000/users/1/（表示删除id=1的用户）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

①

指定id用户不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 修改指定用户信息 PUT `users/{id}/`

**权限**

用户端

**说明**

用于修改编号为id的用户的昵称，个性签名 

**Request**

URL：http://127.0.0.1:8000/users/5/（修改编号为5的用户的信息）

Body：

```json
{
    "name" : "myname", //昵称name为必填字段
    "sign" : "this is my sign", //个性签名sign为选填字段
}
```

**Success Response**

状态码：200

Body：

```json
{
    "id": 6,
    "name": "myname",
    "avatar": "asdfa",
    "email": "adfasdf@qq.com",
    "sign": "this is my sign"
}
```

**Error Response**

①

request body中不包含name字段

状态码：400

Body：

```json
{
    "name": [
        "该字段是必填项。"
    ]
}
```

②

request body中name字段的值为空

状态码：400

Body：

```json
{
    "name": [
        "该字段不能为空。"
    ]
}
```

③

指定id用户不存在（正常情况下不会发生）

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



## 版块

### 获取所有版块 GET  `blocks/`

**权限**

用户端，管理端

**说明**

获取所有版块的id和名称

**Request**

URL：http://127.0.0.1:8000/blocks/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "博雅"
    },
    {
        "id": 2,
        "name": "志愿"
    },
    {
        "id": 3,
        "name": "社团"
    }
]
```

**Error Response**

无



### 新建版块 POST `blocks/`

**权限**

管理端

**说明**

创建一个新的版块

**Request**

URL：http://127.0.0.1:8000/blocks/

Body：

```json
{
    "name" : "社团" //新建版块名称
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 4, //新建版块的id
    "name": "社团" //新建版块的名称
}
```

**Error Response**

如果新的版块名称与已有版块名称重复

状态码：400

Body：

```json
{
    "name": [
        "具有 版块名称 的 block 已存在。"
    ]
}
```



### 获取指定版块 GET `blocks/{id}`

**权限**

管理端

**说明**

获取编号为id的版块的信息

**Request**

URL：http://127.0.0.1:8000/blocks/2/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "name": "博雅"
}
```

**Error Response**

①

对应id的版块不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```





### 修改指定版块信息 PUT `blocks/{id}/`

**权限**

管理端

**说明**

修改编号为id的版块

**Request**

URL：http://127.0.0.1:8000/blocks/4/（表示修改id=4的版块的名称）

Body：

```json
{
    "name" : "版块4" 
}
```

**Success Response**

状态码：200

Body：

```json
{
    "id": 4,
    "name": "版块4"
}
```

**Error Response**

①

如果修改后的版块名称与已有版块名称重复

状态码：400

Body：

```json
{
    "name": [
        "具有 版块名称 的 block 已存在。"
    ]
}
```

②

如果修改后和修改前的名称一致

状态码：400

Body：

```json
{
    "block": [
        "板块名称重复"
    ]
}
```



### 删除指定版块 DELETE `blocks/{id}/`

**权限**

管理端

**说明**

删除编号为id的版块

**Request**

URL：http://127.0.0.1:8000/blocks/4/（表示删除id=4的版块）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

对应id的版块不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



## 组织申请

### 创建组织申请 POST `organizations/applications/`

**权限**

用户端

**说明**

用户可以提交组织申请，用于向管理员申请创建一个新的组织

**Request**

URL：http://127.0.0.1:8000/organizations/applications/

Body：

```json
{
    "name" : "test组织", //必填，组织名称
    "description": "我的申请理由", //必填，申请理由
    "user": 7,	//必填，申请用户的id
    "block": 1	//必填， 申请组织所在的版块id
}
```

**Success Response**

状态码：202

Body：

```json
{
    "id": 4,                                            //组织id
    "name": "test组织",                                  //组织名称
    "description": "我的申请理由",                        //申请理由
    "pub_time": "2021-04-15T11:26:32.396852",           //申请时间
    "status": 0,                                        //审批状态（0：待审批；1：审批通过；2：审批未通过）
    "user": 7,										    //申请用户id
    "block": 1											//申请组织所在的版块id
}
```

**Error Response**

①

缺少某个必填字段，name/dsescription/user/block缺少哪个body中就会返回哪个

状态码：400

Body：

```json
{
    "description": [
        "该字段是必填项。"
    ],
    "user": [
        "该字段是必填项。"
    ],
}
```

②

name/description为空，哪个为空body就会返回哪个

状态码：400

Body:

```json
{
    "name": [
        "该字段不能为空。"
    ],
    "description": [
        "该字段不能为空。"
    ]
}
```

③

组织名与已存在的组织名重复

状态码：400

```json
{
    "name": [
        "已经存在该名称的组织。"
    ]
}
```

④

组织名与已经提交的，未经审批的组织名相同

状态码：400

```json
{
    "name": [
        "已经存在该名称组织的申请"
    ]
}
```



**注：上述错误可能同时出现在同一个Error Response Body中。**



### 获取指定用户的所有组织申请 GET `users/organizations/applications/{user_id}`
**权限**

用户端

**说明**

用于获取id=user_id的用户的所有组织申请

**Request**

URL：http://127.0.0.1:8000/users/organizations/applications/7/（表示获取id=7的用户的所有组织申请）

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "组织1",
        "description": "我想申请",
        "pub_time": "2021-04-15T11:13:11.572283",
        "status": 0,      //审批状态（0：待审批；1：审批通过；2：审批未通过）
        "user": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 2,
        "name": "组织2",
        "description": "理由",
        "pub_time": "2021-04-15T11:21:59.062922",
        "status": 0,
        "user": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "block": {
            "id": 2,
            "name": "志愿"
        }
    }
]

// 若无对应用户的组织申请则返回: 
// []
```

**Error Response**

无



### 获取指定组织申请 GET `organizations/applications/{id}`

**权限**

用户端

**说明**

获取编号为id的组织申请的信息

**Request**

URL：http://127.0.0.1:8000/organizations/applications/2/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 2,
    "user": {
        "id": 7,
        "name": "用户1",
        "avatar": null,
        "email": null,
        "sign": null
    },
    "name": "组织2",
    "description": "理由",
    "pub_time": "2021-04-15T11:21:59.062922",
    "status": 0,
    "block": {
        "id": 2,
        "name": "志愿"
    }
}
```

**Error Response**

①

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```





### 获取所有组织申请GET `organizaitons/applications/`

**权限**

管理端

**说明**

用于获取所有的组织申请

**Request**

URL：http://127.0.0.1:8000/organizations/applications/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "组织1",
        "description": "我想申请",
        "pub_time": "2021-04-15T11:13:11.572283",
        "status": 0,      //审批状态（0：待审批；1：审批通过；2：审批未通过）
        "user": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 2,
        "name": "组织2",
        "description": "理由",
        "pub_time": "2021-04-15T11:21:59.062922",
        "status": 0,
        "user": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "block": {
            "id": 2,
            "name": "志愿"
        }
    }
]

// 若无组织申请则返回: 
// []
```

**Error Response**

无



### 删除指定组织申请 DELETE `organizations/applications/{id}`

**权限**

用户端，管理端

**说明**

删除编号为id的组织申请

**Request**

URL：http://127.0.0.1:8000/organizations/applications/4/（表示删除id=4的组织申请）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

①

对应id的组织申请不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 审批组织申请PUT `organizations/applications/verifications/{id}/`

**权限**

管理端

**说明**

审核指定id的组织申请，status表示审批状态。

status=0 表示待审批，此状态的组织申请可以审批。

status=1 表示审批通过。

status=2 表示审批不通过。

批准通过后，将自动创建对应组织，并添加组织负责人为组织管理员。

**Request**

URL：http://127.0.0.1:8000/organizations/applications/verifications/4/（表示对id=4的组织申请进行审批）

Body：

```json
{
    "status": 1  //1：表示审批通过；2：表示审批不通过
}
```

**Success Response**

状态码：200

Body：

```json
{
    "status": 1
}
```

**Error Response**

①

对应id的组织申请已经被审批，即`status!=0​`（正常情况下不会发生）

状态码：400

Body：

```json
{
    "detail": [
        "该组织申请已审批。"
    ]
}
```

②

对应id的组织申请不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```

③

如果传入的`status`参数不符（正常情况下不会发生）

状态码：400

```json
{
    "status": [
        "“5” 不是合法选项。"
    ]
}
```



## 组织

### 新建组织 POST `organizations/`

**权限**

管理端

**说明**

组织申请审批通过后创建组织。

前端设计建议：

- 管理端在批准组织申请时，应先请求创建组织，创建组织成功后，再修改组织申请的审核状态。防止出现审核通过后，组织申请失败的情况。（因为组织名可能发生冲突）

**Request**

URL：http://127.0.0.1:8000/organizations/

Body：

```json
{
    "name": "新组织1",   //组织名
    "owner": 5,			//申请者的id，申请者自动成为负责人
    "block": 1			//组织所属的版块
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "name": "新组织1",
    "description": null,    //组织描述
    "create_time": "2021-04-15T14:19:18.881913",
    "avatar": null,			//组织头像
    "owner": 5,
    "block": 1
}
```

**Error Response**

①

新创建的组织名与已有组织名重复（虽然请求申请验证过了，但是在请求提交后，已有组织修改名称可能恰好与表单名称相同）。

状态码：400

Body：

```json
{
    "name": [
        "具有 组织名称 的 organization 已存在。"
    ]
}
```

②

name/block/owner字段缺失，缺少哪个body中就会返回哪个

状态码：400

Body：

```json
{
    "name": [
        "该字段是必填项。"
    ],
    "block": [
        "该字段是必填项。"
    ]
}
```



### 获取指定组织信息 GET `organizations/{id}/`

**权限**

用户端

**说明**

获取编号为id的组织的信息

**Request**

URL：http://127.0.0.1:8000/organizations/1/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "name": "新组织1",
    "description": null,
    "create_time": "2021-04-15T14:19:18.881913",
    "avatar": null,
    "owner": {
        "id": 5,
        "name": "dd",
        "avatar": "111",
        "email": "1111@qq.com",
        "sign": ""
    },
    "block": {
        "id": 1,
        "name": "博雅"
    }
}
```

**Error Response**

①

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 获取所有组织 GET  `organizations/`

**权限**

管理端

**说明**

获取所有组织的信息

**Request**

URL：http://127.0.0.1:8000/organizations/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 3,
        "owner": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "name": "333",
        "description": null,
        "create_time": "2021-04-15T15:53:14.944308",
        "avatar": null,
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 4,
        "owner": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "name": "组织5",
        "description": null,
        "create_time": "2021-04-15T16:41:33.383075",
        "avatar": null,
        "block": {
            "id": 2,
            "name": "志愿"
        }
    }
]
```

**Error Response**

无



### 获取指定版块下所有组织GET `blocks/organizations/{block_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的版块下的所有组织

**Request**

URL：http://127.0.0.1:8000/blocks/organizations/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "新组织1",
        "description": null,
        "create_time": "2021-04-15T14:19:18.881913",
        "avatar": null,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 2,
        "name": "新组织2",
        "description": "啊啊啊啊啊",
        "create_time": "2021-04-15T15:02:54.030413",
        "avatar": null,
        "owner": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]


// 若指定版块下无组织，则返回:
// []
```

**Error Response**

无



### 修改指定组织信息 PUT `organizations/{id}/`

**权限**

用户端（管理员或负责人）

**说明**

修改对应id的组织信息

**Request**

URL：http://127.0.0.1:8000/organizations/1/

Body：

```json
{
    "name": "组织名",  //必填
    "description": "组织描述", //选填
    "avatar": "组织头像url"  //选填
}
```

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "name": "组织",
    "description": "我是描述",
    "create_time": "2021-04-15T14:19:18.881913",
    "avatar": "我是图片链接",
    "owner": {
        "id": 5,
        "name": "dd",
        "avatar": "111",
        "email": "1111@qq.com",
        "sign": ""
    },
    "block": {
        "id": 1,
        "name": "博雅"
    }
}
```

**Error Response**

①

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```

②

request body中缺少name字段

状态码：400

Body：

```json
{
    "name": [
        "该字段是必填项。"
    ]
}
```

③

request body中name字段为空

Body：

```json
{
    "name": [
        "该字段不能为空。"
    ]
}
```

④

修改后的组织名name与已有组织名重复

状态码：400

Body：

```json
{
    "name": [
        "具有 组织名称 的 organization 已存在。"
    ]
}
```

### 删除指定组织 DELETE `organizations/{id}/`

**权限**

用户端（负责人），管理端

**说明**

删除编号为id的组织

**Request**

URL：http://127.0.0.1:8000/organizations/1/

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

①

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 组织负责人转让 POST `organizations/owner/{id}`

**权限**

用户端（负责人），管理端

**说明**

将编号为id的组织的负责人更改为指定用户

**Request**

URL：http://127.0.0.1:8000/organizations/owner/3/

Body：

```json
{
    "owner": 6   //用户id（未来的组织负责人）
}
```

**Success Response**

状态码：200

Body：

```json
{
    "owner": 6
}
```

**Error Response**

①

owner字段缺失

状态码：400

Body：

```json
{
    "owner": [
        "该字段是必填项。"
    ]
}
```

②

对应id的组织不存在。

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```





### 获取指定用户与指定组织的关系 POST `userOrgRelation/`

**权限**

用户端

**说明**

获取指定用户和指定组织是否已关注、是否为负责人、是否为管理员等关系

**Request**

URL：http://127.0.0.1:8000/userOrgRelation/

Body：

```json
{
    "user": 6,
    "org": 233,
}
```

**Success Response**

状态码：200

Body：

```json
{
    "isFollower" : true,
    "isOwner" : true,
    "isManager" : true
}
```

**Error Response**

①

对应id的用户不存在

状态码：404

Body：

```json
{
    "detail": "未找到用户。"
}
```

②

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到组织。"
}
```





## 用户关注

### 用户关注组织 POST `users/followed_organizations/`

**权限**

用户端

**说明**

用户关注组织

**Request**

URL：http://127.0.0.1:8000/users/followed_organizations/

Body：

```json
{
    "org": 3,   //组织id，必填
    "person": 7	//用户id，必填
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "org": 3,
    "person": 7
}
```

**Error Response**

①

对应id的组织/用户不存在。（正常情况下不会出现）

状态码：400

Body：

```json
{
    "org": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的组织id
    ],
    "person": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的用户id
    ]
}
```

②

对应id的用户已经关注对应id的组织。

状态码：400

```json
{
    "non_field_errors": [
        "已关注该组织。"
    ]
}
```



### 用户取消关注组织 DELETE `users/followed_organizations/?user=&org=`

**权限**

用户端

**说明**

对应id用户取消关注对应id组织

**Request**

URL：http://127.0.0.1:8000/users/followed_organizations/?user=7&org=3（参数在query params中，分别为用户id和组织id）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

无



### 获取指定用户关注的所有组织 GET `users/followed_organizations/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户的关注的所有组织

**Request**

URL：http://127.0.0.1:8000/users/followed_organizations/6/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "org": {
            "id": 3,
            "name": "组织",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": {
                "id": 7,
                "name": "用户1",
                "avatar": null,
                "email": null,
                "sign": null
            },
            "block": {
                "id": 1,
                "name": "博雅"
            }
        }
    },
    {
        "org": {
            "id": 4,
            "name": "组织5",
            "description": null,
            "create_time": "2021-04-15T16:41:33.383075",
            "avatar": null,
            "owner": {
                "id": 7,
                "name": "用户1",
                "avatar": null,
                "email": null,
                "sign": null
            },
            "block": {
                "id": 2,
                "name": "志愿"
            }
        }
    }
]


// 若对应id用户不存在，或无关注的组织，则返回：
// []
```

**Error Response**

无



### 获取指定用户关注的组织发布的活动 GET `users/followed_organizations/activities/{user_id}/`

**权限**

用户端

**说明**

获取编号为id的用户的关注的组织发布的活动

**Request**

URL：http://127.0.0.1:8000/users/followed_organizations/activities/6/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 2,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动11",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-19T14:19:20",
        "pub_time": "2021-04-19T14:34:29.243051",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 3,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动3",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:55:24.055133",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]


// 若对应id用户不存在，或无关注的组织，或关注的组织无活动，则返回：
// []
```

**Error Response**

无



## 组织管理

### 组织添加管理员 POST `organizations/managers/`

**权限**

用户端（负责人）

**说明**

指定组织添加指定用户为管理员

**Request**

URL：http://127.0.0.1:8000/organizations/managers/

Body：

```json
{
    "org": 3,   //组织id，必填
    "person": 5	//用户id，必填
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "org": 3,
    "person": 5
}
```

**Error Response**

①

对应id的组织/用户不存在。

状态码：400

Body：

```json
{
    "org": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的组织id
    ],
    "person": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的用户id
    ]
}
```

②

对应id的用户已经是对应id的组织的管理员。

状态码：400

```json
{
    "non_field_errors": [
        "该用户已是此组织管理员。"
    ]
}
```



### 取消组织管理员 DELETE `organizations/managers/?user=&org=`

**权限**

用户端（负责人）

**说明**

取消对应id用户的对应id组织的管理员身份

**Request**

URL：http://127.0.0.1:8000/organizations/managers/?user=7&org=3（参数在query params中，分别为用户id和组织id）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

无



### 获取指定用户管理的所有组织 GET `users/managed_organizations/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户的管理的所有组织

**Request**

URL：http://127.0.0.1:8000/users/managed_organizations/5/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "org": {
            "id": 3,
            "name": "组织",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": {
                "id": 7,
                "openid": "test_openid",
                "name": "用户1",
                "avatar": null,
                "email": null,
                "sign": null
            },
            "block": {
                "id": 1,
                "name": "博雅"
            }
        }
    },
    {
        "org": {
            "id": 4,
            "name": "组织5",
            "description": null,
            "create_time": "2021-04-15T16:41:33.383075",
            "avatar": null,
            "owner": {
                "id": 7,
                "openid": "test_openid",
                "name": "用户1",
                "avatar": null,
                "email": null,
                "sign": null
            },
            "block": {
                "id": 2,
                "name": "志愿"
            }
        }
    }
]


// 若对应id用户不存在，或无管理的组织，则返回：
// []
```

**Error Response**

无

### 获取指定组织的全部管理员 GET `organizations/managers/{id}/`

**权限**

用户端，管理端

**说明**

获取编号为id的组织的全部管理员

**Request**

URL：http://127.0.0.1:8000/organizations/managers/3/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "person": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        }
    },
    {
        "person": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        }
    }
]

// 若无对应id的组织，或对应id的组织无管理员，则返回:
// []
```

**Error Response**

无



## 活动分类

### 获取所有活动分类 GET  `activities/categories/`

**权限**

用户端，管理端

**说明**

获取所有分类的id和名称

**Request**

URL：http://127.0.0.1:8000/activities/categories/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "体育"
    },
    {
        "id": 2,
        "name": "文艺"
    },
    {
        "id": 3,
        "name": "音乐"
    }
]
```

**Error Response**

无



### 新建活动分类 POST `activities/categories/`

**权限**

管理端

**说明**

创建一个新的活动分类

**Request**

URL：http://127.0.0.1:8000/activities/categories/

Body：

```json
{
    "name" : "晚会" //新建活动分类的名称
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 4, //新建活动分类的id
    "name": "晚会" //新建活动分类的名称
}
```

**Error Response**

如果新的活动分类名称与已有活动分类名称重复

状态码：400

Body：

```json
{
    "name": [
        "具有 分类名称 的 category 已存在。"
    ]
}
```



### 修改指定活动分类信息 PUT `activities/categories/{id}/`

**权限**

管理端

**说明**

修改编号为id的活动分类

**Request**

URL：http://127.0.0.1:8000/activities/categories/4/（表示修改id=4的活动分类的名称）

Body：

```json
{
    "name" : "分类4" 
}
```

**Success Response**

状态码：200

Body：

```json
{
    "id": 4,
    "name": "分类4"
}
```

**Error Response**

①

如果修改后的活动分类名称与已有活动分类名称重复

状态码：400

Body：

```json
{
    "name": [
        "具有 分类名称 的 category 已存在。"
    ]
}
```

②

如果修改后和修改前的名称一致

状态码：400

Body：

```json
{
    "category": [
        "分类名称重复"
    ]
}
```



### 删除指定活动分类 DELETE `activities/categories/{id}/`

**权限**

管理端

**说明**

删除编号为id的活动分类

**Request**

URL：http://127.0.0.1:8000/activities/categories/4/（表示删除id=4的活动分类）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

对应id的活动分类不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



## 活动地址

### 获取所有活动地址 GET  `activities/addresses/`

**权限**

用户端，管理端

**说明**

获取所有活动地址的id、名称、经度、纬度

**Request**

URL：http://127.0.0.1:8000/activities/addresses/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "name": "篮球场",
        "longitude": "123.123000",
        "latitude": "123.123000"
    },
    {
        "id": 2,
        "name": "足球场",
        "longitude": "122.123000",
        "latitude": "123.123000"
    }
]
```

**Error Response**

无



### 新建活动地址 POST `activities/addresses/`

**权限**

用户端，管理端

**说明**

创建一个新的活动地址

**Request**

URL：http://127.0.0.1:8000/activities/addresses/

Body：

```json
{
    "name" : "篮球场",             //新建活动地址的名称，必填
    "longitude": "123.123",  //地址经度，必填
    "latitude": "123.123",   //地址纬度，必填
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 2,
    "name": "篮球场",
    "longitude": "123.123000",
    "latitude": "123.123000"
}
```

**Error Response**

①

新的活动地址名称与已有活动地址名称重复

状态码：400

Body：

```json
{
    "name": [
        "具有 地址名称 的 address 已存在。"
    ]
}
```

②

新的活动地址和已有的活动地址重复

状态码：400

Body：

```json
{
    "address": [
        "地点重复。"
    ]
}
```



### 删除指定活动地址 DELETE `activities/addresses/{id}/`

**权限**

管理端

**说明**

删除编号为id的活动地址

**Request**

URL：http://127.0.0.1:8000/activities/addresses/4/（表示删除id=4的活动地址）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

对应id的活动地址不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



## 活动

### 新建活动POST `activities/`

**权限**

用户端

**说明**

新建一个活动。

前端设计建议：

- 发布组织活动，可在组织详情界面下进行创建，此时自动获取组织（org）以及组织所在的版块（block）

- 发布个人活动，可在个人界面中进行创建，此时自动将版块（block）设为”个人“，组织（org）为空
- 地址（address）和分类（type）填的都是id，应该获取所有地址或分类给用户选择，如果没有合适的则需要先新建一个（类似淘宝的收货地址）
- 开始/结束时间请从这些格式中选择：YYYY-MM-DDThh:mm\[:ss\[.uuuuuu]][+HH:MM|-HH:MM|Z]。

**Request**

URL：http://127.0.0.1:8000/activities/

Body：

```json
{
    "name": "活动1",							   //必填，活动名称
    "begin_time": "2021-04-16T14:19:18",		//必填，活动开始时间
    "end_time": "2021-04-16T14:19:18",			//必填，活动结束时间
    "contain": 100,								//必填，活动人数限制，该值必须大于等于1
    "description": "这个是活动描述",			   //选填，活动描述
    "review": false,							//必填，加入该活动是否需要审核（true：需要；false：不需要）
    "owner": 5,									//必填，创建该活动的用户id
    "type": 1,									//选填，该活动的分类
    "org": null,								//选填，该活动的组织的id（若为个人活动则可以不填）
    "location": 1,								//必填，该活动的地址的id
    "block": 1									//必填，该活动所属的版块
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "name": "活动1",
    "begin_time": "2021-04-16T14:19:18",
    "end_time": "2021-04-16T14:19:18",
    "pub_time": "2021-04-19T14:31:05.291480",
    "contain": 100,
    "description": "这个是活动描述",
    "review": false,
    "owner": 5,
    "type": 1,
    "org": null,
    "location": 1,
    "block": 1
}
```

**Error Response**

①

新创建的活动名称与已有的活动名称重复。

状态码：400

Body：

```json
{
    "name": [
        "具有 活动名称 的 activity 已存在。"
    ]
}
```

②

必填字段缺失，缺少哪个body中就会返回哪个

状态码：400

Body：

```json
{
    "name": [
        "该字段是必填项。"
    ],
    "begin_time": [
        "该字段是必填项。"
    ],
    "end_time": [
        "该字段是必填项。"
    ],
    "contain": [
        "该字段是必填项。"
    ],
    "owner": [
        "该字段是必填项。"
    ],
    "location": [
        "该字段是必填项。"
    ],
    "block": [
        "该字段是必填项。"
    ]
}
```

③

活动人数限制（contain字段）小于1。

状态码：400

Body：

```json
{
    "contain": [
        "请确保该值大于或者等于 1。"
    ]
}
```

④

开始/结束时间格式错误

状态码：400

Body：

```json
{
    "begin_time": [
        "日期时间格式错误。请从这些格式中选择：YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]。"
    ],
    "end_time": [
        "日期时间格式错误。请从这些格式中选择：YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]。"
    ]
}
```



### 获取指定活动信息 GET `activities/{id}/`

**权限**

用户端，管理端

**说明**

获取编号为id的活动的信息

**Request**

URL：http://127.0.0.1:8000/activities/1/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "owner": {
        "id": 5,
        "name": "dd",
        "avatar": "111",
        "email": "1111@qq.com",
        "sign": ""
    },
    "name": "活动1",
    "begin_time": "2021-04-16T14:19:18",
    "end_time": "2021-04-16T14:19:18",
    "pub_time": "2021-04-19T14:31:05.291480",
    "contain": 100,
    "description": "这个是活动描述",
    "review": false,
    "type": {
        "id": 1,
        "name": "讲座"
    },
    "org": null,
    "location": {
        "id": 1,
        "name": "篮球场",
        "longitude": "123.123000",
        "latitude": "123.123000"
    },
    "block": {
        "id": 1,
        "name": "博雅"
    }
}
```

**Error Response**

①

对应id的组织不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 获取所有活动 GET  `activities/`

**权限**

管理端

**说明**

获取所有活动的信息

**Request**

URL：http://127.0.0.1:8000/activities/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 2,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动11",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-19T14:19:20",
        "pub_time": "2021-04-19T14:34:29.243051",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 3,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动3",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:55:24.055133",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无



### 修改指定活动信息 PUT `activities/{id}/`

**权限**

用户端（活动发起人）

**说明**

修改对应id的活动信息

**Request**

URL：http://127.0.0.1:8000/activities/1/

Body：

```json
{
    "name": "活动1",							   //必填，活动名称
    "begin_time": "2021-04-16T14:19:18",		//必填，活动开始时间
    "end_time": "2021-04-16T14:19:18",			//必填，活动结束时间
    "contain": 100,								//必填，活动人数限制，该值必须大于等于1
    "description": "这个是活动描述",			   //选填，活动描述
    "type": 1,									//选填，该活动的分类
    "location": 1,								//必填，该活动的地址的id
}
```

**Success Response**

状态码：200

Body：

```json
{
    "name": "活动1",						
    "begin_time": "2021-04-16T14:19:18",
    "end_time": "2021-04-16T14:19:18",	
    "contain": 100,						
    "description": "这个是活动描述",		
    "type": 1,							
    "location": 1,					
}
```

**Error Response**

①

对应id的活动不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```

②

修改后的活动名称与已有的活动名称重复。

状态码：400

Body：

```json
{
    "name": [
        "具有 活动名称 的 activity 已存在。"
    ]
}
```

③

必填字段缺失，缺少哪个body中就会返回哪个

状态码：400

Body：

```json
{
    "name": [
        "该字段是必填项。"
    ],
    "begin_time": [
        "该字段是必填项。"
    ],
    "end_time": [
        "该字段是必填项。"
    ],
    "contain": [
        "该字段是必填项。"
    ],
    "owner": [
        "该字段是必填项。"
    ],
    "location": [
        "该字段是必填项。"
    ],
    "block": [
        "该字段是必填项。"
    ]
}
```

④

活动人数限制（contain字段）小于1。

状态码：400

Body：

```json
{
    "contain": [
        "请确保该值大于或者等于 1。"
    ]
}
```

⑤

开始/结束时间格式错误

状态码：400

Body：

```json
{
    "begin_time": [
        "日期时间格式错误。请从这些格式中选择：YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]。"
    ],
    "end_time": [
        "日期时间格式错误。请从这些格式中选择：YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]。"
    ]
}
```



### 删除指定活动 DELETE `activities/{id}/`

**权限**

用户端（活动发布人），管理端

**说明**

删除编号为id的活动

**Request**

URL：http://127.0.0.1:8000/activities/1/

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

①

对应id的活动不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 获取指定组织下所有活动 GET `organizations/activities/{org_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的组织下的所有活动

**Request**

URL：http://127.0.0.1:8000/organizations/activities/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 3,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动3",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:55:24.055133",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 4,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动4",
        "begin_time": "2021-04-19T14:19:18",
        "end_time": "2021-04-19T14:19:20",
        "pub_time": "2021-04-19T15:58:53.113287",
        "contain": 12,
        "description": "这个是活动描述",
        "review": false,
        "type": null,
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]

// 若指定版块下无组织，则返回:
// []
```

**Error Response**

无

### 获得指定组织未开始活动 GET `organizations/activities/unstart/{org_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的组织下的所有开始时间大于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/organizations/activities/unstart/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 2,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act2",
        "begin_time": "2021-04-24T14:57:00",
        "end_time": "2021-04-24T18:00:00",
        "pub_time": "2021-04-22T14:57:28.504214",
        "contain": 20,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定组织进行中活动 GET `organizations/activities/cur/{org_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的组织下的所有开始时间≤当前时间≤结束时间的活动

**Request**

URL：http://127.0.0.1:8000/organizations/activities/cur/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 3,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act3",
        "begin_time": "2021-04-21T15:11:00",
        "end_time": "2021-04-23T15:11:00",
        "pub_time": "2021-04-22T15:11:26.882629",
        "contain": 1,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定组织已结束活动 GET `organizations/activities/end/{org_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的组织下的所有结束时间小于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/organizations/activities/end/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 1,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "活动1",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-21T16:26:48.607433",
        "contain": 100,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获取指定用户发布的所有活动 GET `users/released_activities/{user_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的用户发布的所有活动。（未区分个人活动和组织活动）

**Request**

URL：http://127.0.0.1:8000/users/released_activities/5/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动1",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:31:05.291480",
        "contain": 100,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 2,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动2",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:34:29.243051",
        "contain": 0,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
// 若指定用户未发布过活动，则返回:
// []
```

**Error Response**

无

### 获得指定用户发布未开始活动 GET `users/released_activities/unstart/{user_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的用户已发布所有开始时间大于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/users/released_activities/unstart/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 2,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act2",
        "begin_time": "2021-04-24T14:57:00",
        "end_time": "2021-04-24T18:00:00",
        "pub_time": "2021-04-22T14:57:28.504214",
        "contain": 20,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定用户发布进行中活动 GET `users/released_activities/cur/{user_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的用户的所有开始时间≤当前时间≤结束时间的活动

**Request**

URL：http://127.0.0.1:8000/users/released_activities/cur/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 4,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act4",
        "begin_time": "2021-04-24T06:00:00",
        "end_time": "2021-04-24T18:00:00",
        "pub_time": "2021-04-24T09:58:44.574866",
        "contain": 20,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定组织已结束活动 GET`users/released_activities/end/{user_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的用户发布的结束时间<当前时间的活动

**Request**

URL：http://127.0.0.1:8000/users/released_activities/end/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 1,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "活动1",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-21T16:26:48.607433",
        "contain": 100,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 3,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act3",
        "begin_time": "2021-04-21T15:11:00",
        "end_time": "2021-04-23T15:11:00",
        "pub_time": "2021-04-22T15:11:26.882629",
        "contain": 1,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获取指定版块下的所有活动 GET `blocks/activities/{block_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的用户发布的所有活动

**Request**

URL：http://127.0.0.1:8000/blocks/activities/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动1",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:31:05.291480",
        "contain": 100,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 2,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动2",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:34:29.243051",
        "contain": 0,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
// 若对应板块下无活动，则返回:
// []
```

**Error Response**

无

### 获得指定板块下未开始活动 GET `blocks/activities/unstart/{block_id}/`

**权限**

用户端，管理端

**说明**

获取对应id的板块所有开始时间>当前时间的活动

**Request**

URL：http://127.0.0.1:8000/blocks/activities/unstart/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 2,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act2",
        "begin_time": "2021-04-24T14:57:00",
        "end_time": "2021-04-24T18:00:00",
        "pub_time": "2021-04-22T14:57:28.504214",
        "contain": 20,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定用户发布进行中活动 GET `blocks/activities/cur/{block_id}`

**权限**

用户端，管理端

**说明**

获取对应id的板块所有开始时间≤当前时间≤结束时间的活动

**Request**

URL：http://127.0.0.1:8000/blocks/activities/cur/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 4,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act4",
        "begin_time": "2021-04-24T06:00:00",
        "end_time": "2021-04-24T18:00:00",
        "pub_time": "2021-04-24T09:58:44.574866",
        "contain": 20,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无

### 获得指定组织已结束活动 GET`blocks/activities/end/{block_id}`

**权限**

用户端，管理端

**说明**

获取对应id的板块结束时间<当前时间的活动

**Request**

URL：http://127.0.0.1:8000/blocks/activities/end/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "id": 1,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "活动1",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-21T16:26:48.607433",
        "contain": 100,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 3,
        "owner": {
            "id": 1,
            "name": "Jessica",
            "avatar": "url",
            "email": "Jessica@qq.com",
            "sign": "mio mio~"
        },
        "name": "Act3",
        "begin_time": "2021-04-21T15:11:00",
        "end_time": "2021-04-23T15:11:00",
        "pub_time": "2021-04-22T15:11:26.882629",
        "contain": 1,
        "description": null,
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 1,
            "name": "Org1",
            "description": null,
            "create_time": "2021-04-21T16:26:19.358313",
            "avatar": null,
            "owner": 1,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "Loc1",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无





### 获取指定用户与指定活动的关系 POST `userActRelation/` 

**权限**

用户端

**说明**

获取指定用户和指定活动是否已加入、是否为待审核状态、是否为发布人（即活动owner）、是否为管理员（发布人or为活动所属组织的管理员）等关系

**Request**

URL：http://127.0.0.1:8000/userActRelation/

Body：

```json
{
    "user": 6,
    "act": 233,
}
```

**Success Response**

状态码：200

Body：

```json
{
    "hasJoined" : true,
    "underReview" : false,
    "isOwner" : true,
    "isManager" : true
}
```

**Error Response**

①

对应id的用户不存在

状态码：404

Body：

```json
{
    "detail": "未找到用户。"
}
```

②

对应id的活动不存在

状态码：404

Body：

```json
{
    "detail": "未找到活动。"
}
```





## 活动参与 

### 用户加入非审核活动 POST `activities/participants/`

**权限**

用户端

**说明**

用户加入一个无需审核的活动。

**Request**

URL：http://127.0.0.1:8000/activities/participants/

Body：

```json
{
    "act": 3,
    "person": 5
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "act": 3,
    "person": 5
}
```

**Error Response**

①

对应id的活动/用户不存在。

状态码：400

Body：

```json
{
    "act": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的活动id
    ],
    "person": [
        "无效主键 “xx” － 对象不存在。" //xx为传入的用户id
    ]
}
```

②

对应id的用户已经加入对应id的活动。

状态码：400

```json
{
    "detail": [
    	"不可重复加入活动。"
    ]
}
```

③

对应id的报名人数已达人数上限

状态码：400

```json
{
	"detail": "活动人数已满。"
}
```



### 用户退出活动 DELETE `activities/participants/?user=&act=`

**权限**

用户端

**说明**

对应id用户退出对应id的活动。

**Request**

URL：http://127.0.0.1:8000/activities/participants/?person=7&act=3（参数在query params中，分别为用户id和活动id）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

无



### 获取指定用户参与的所有活动 GET `user/joined_acts/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户加入的所有活动

**Request**

URL：http://127.0.0.1:8000/users/joined_acts/5/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 3,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动3",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:55:24.055133",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 4,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动4",
        "begin_time": "2021-04-19T14:19:18",
        "end_time": "2021-04-19T14:19:20",
        "pub_time": "2021-04-19T15:58:53.113287",
        "contain": 12,
        "description": "这个是活动描述",
        "review": false,
        "type": null,
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]


// 若对应id用户不存在，或未参与任何活动，则返回：
// []
```

**Error Response**

无



### 获取指定用户参与的未开始活动 GET `user/joined_acts/unstart/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户加入的开始时间大于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/user/joined_acts/unstart/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "act": {
            "id": 2,
            "name": "Act2",
            "begin_time": "2021-04-24T14:57:00",
            "end_time": "2021-04-24T18:00:00",
            "pub_time": "2021-04-22T14:57:28.504214",
            "contain": 20,
            "description": null,
            "review": false,
            "owner": 1,
            "type": 1,
            "org": 1,
            "location": 1,
            "block": 1
        }
    }
]
```

**Error Response**

无

### 获取指定用户参与的进行中活动 GET `user/joined_acts/cur/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户加入的开始时间小于等于当前时间的活动 且结束时间大于等于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/user/joined_acts/cur/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "act": {
            "id": 3,
            "name": "Act3",
            "begin_time": "2021-04-21T15:11:00",
            "end_time": "2021-04-23T15:11:00",
            "pub_time": "2021-04-22T15:11:26.882629",
            "contain": 1,
            "description": null,
            "review": false,
            "owner": 1,
            "type": 1,
            "org": 1,
            "location": 1,
            "block": 1
        }
    }
]
```

**Error Response**

无

### 获取指定用户参与的已结束活动 GET `user/joined_acts/end/{id}/`

**权限**

用户端

**说明**

获取编号为id的用户加入的结束时间小于当前时间的活动

**Request**

URL：http://127.0.0.1:8000/user/joined_acts/end/1/

Body：无

**Success Response**

状态码：200

```json
[
    {
        "act": {
            "id": 1,
            "name": "活动1",
            "begin_time": "2021-04-16T14:19:18",
            "end_time": "2021-04-16T14:19:18",
            "pub_time": "2021-04-21T16:26:48.607433",
            "contain": 100,
            "description": "这个是活动描述",
            "review": false,
            "owner": 1,
            "type": 1,
            "org": 1,
            "location": 1,
            "block": 1
        }
    }
]
```

**Error Response**

无

### 获取指定活动的报名人数 GET `activities/joined_numbers/{id}/`

**权限**

用户端，管理端

**说明**

获取编号为id的活动的报名人数

**Request**

URL：http://127.0.0.1:8000/activities/joined_numbers/3/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "number": 1
}

//无对应活动也会返回值，返回的是0
```

**Error Response**

无



## 活动评价

### 新建活动评价 POST `activities/comments/`

**权限**

用户端

**说明**

创建一个新的活动评价

**Request**

URL：http://127.0.0.1:8000/activites/comments/

Body：

```json
{
    "content": "活动评价1",	    //选填，评价
    "score": 1,  			  //必填，打分
    "act": 3,				  //必填，活动id
    "user": 5				  //必填，用户id
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 1,
    "content": "活动评论1",
    "pub_time": "2021-04-28T14:05:42.398937",
    "score": 1.0,
    "act": 3,
    "user": 5
}
```

**Error Response**

①

缺少score/act/user字段

状态码：400

Body：

```json
{
    "score": [
        "该字段是必填项。"
    ],
    "act": [
        "该字段是必填项。"
    ],
    "user": [
        "该字段是必填项。"
    ]
}
```



### 获取指定活动评论信息 GET `activities/comments/{id}/`

**权限**

用户端

**说明**

获取编号为id的活动评论的信息

**Request**

URL：http://127.0.0.1:8000/activities/comments/1/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "user": {
        "id": 5,
        "name": "dd",
        "avatar": "111",
        "email": "1111@qq.com",
        "sign": ""
    },
    "content": "活动评论1",
    "pub_time": "2021-04-28T14:05:42.398937",
    "score": 1.0,
    "act": 3
}
```

**Error Response**

①

对应id的活动评论不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```





### 获取所有活动评价 GET  `activities/comments/`

**权限**

管理端

**说明**

获取所有活动评价

**Request**

URL：http://127.0.0.1:8000/activities/comments/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "user": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "content": "活动评论1",
        "pub_time": "2021-04-28T14:05:42.398937",
        "score": 1.0,
        "act": 3
    },
    {
        "id": 2,
        "user": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "content": "活动评论2",
        "pub_time": "2021-04-28T14:10:38.738156",
        "score": 9.0,
        "act": 3
    }
]
```

**Error Response**

无



### 获取指定活动评价 GET  `activities/{act_id}/comments/`

**权限**

用户端，管理端

**说明**

获取编号为id的活动的评价

**Request**

URL：http://127.0.0.1:8000/activities/3/comments/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 1,
        "user": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "content": "活动评论1",
        "pub_time": "2021-04-28T14:05:42.398937",
        "score": 5.0,
        "act": 3
    },
    {
        "id": 2,
        "user": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "content": "活动评论2",
        "pub_time": "2021-04-28T14:10:38.738156",
        "score": 9.0,
        "act": 3
    }
]

// 若指定id活动下无评价，或无对应id的活动，则返回:
// [] 
```

**Error Response**

无



### 修改指定活动评价 PUT `activities/comments/{id}/`

**权限**

用户端

**说明**

修改编号为id的活动评价

**Request**

URL：http://127.0.0.1:8000/activities/comments/4/

Body：

```json
{
    "content": "活动评论11",	//选填
    "score": 0   			   //必填
}
```

**Success Response**

状态码：200

Body：

```json
{
    "content": "活动评论11",
    "score": 0.0
}
```

**Error Response**

①

无对应id的活动评论

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 删除指定活动评价 DELETE `activities/comments/{id}/`

**权限**

用户端，管理端

**说明**

删除编号为id的活动评价

**Request**

URL：http://127.0.0.1:8000/feedbacks/4/（表示删除id=4的活动评价）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

对应id的活动评价不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



### 获取指定用户在指定活动发布的活动评论评价 GET  `activities/{act_id}/users/{user_id}/comments/`

**权限**

用户端

**说明**

获取编号为user_id的用户在编号为act_id的活动下发布的活动评论

**Request**

URL：http://127.0.0.1:8000/activities/3/user/5/comments/

Body：无

**Success Response**

状态码：200

Body：

```json
{
    "id": 1,
    "user": {
        "id": 5,
        "name": "dd",
        "avatar": "111",
        "email": "1111@qq.com",
        "sign": ""
    },
    "content": "活动评论11",
    "pub_time": "2021-04-28T14:05:42.398937",
    "score": 0,
    "act": 3
}
```

**Error Response**

①

若指定用户在指定活动下无评论。

状态码：404

Body：

```json
{
    "id": -1
}
```









## 个性化推荐

### 获取推荐组织 GET  `recommended/organizations/{user_id}`

**权限**

管理端

**说明**

获取推荐的组织列表

**Request**

URL：http://127.0.0.1:8000/recommended/organizations/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 3,
        "owner": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "name": "333",
        "description": null,
        "create_time": "2021-04-15T15:53:14.944308",
        "avatar": null,
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 4,
        "owner": {
            "id": 7,
            "name": "用户1",
            "avatar": null,
            "email": null,
            "sign": null
        },
        "name": "组织5",
        "description": null,
        "create_time": "2021-04-15T16:41:33.383075",
        "avatar": null,
        "block": {
            "id": 2,
            "name": "志愿"
        }
    }
]
```

**Error Response**

无



### 获取推荐活动 GET  `recommended/activities/{user_id}`

**权限**

用户端

**说明**

获取所有活动的信息

**Request**

URL：http://127.0.0.1:8000/recommended/activities/1/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 2,
        "owner": {
            "id": 5,
            "name": "dd",
            "avatar": "111",
            "email": "1111@qq.com",
            "sign": ""
        },
        "name": "活动11",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-19T14:19:20",
        "pub_time": "2021-04-19T14:34:29.243051",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": null,
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    },
    {
        "id": 3,
        "owner": {
            "id": 6,
            "name": "myname",
            "avatar": "asdfa",
            "email": "adfasdf@qq.com",
            "sign": "this is my sign"
        },
        "name": "活动3",
        "begin_time": "2021-04-16T14:19:18",
        "end_time": "2021-04-16T14:19:18",
        "pub_time": "2021-04-19T14:55:24.055133",
        "contain": 1,
        "description": "这个是活动描述",
        "review": false,
        "type": {
            "id": 1,
            "name": "讲座"
        },
        "org": {
            "id": 3,
            "name": "333",
            "description": null,
            "create_time": "2021-04-15T15:53:14.944308",
            "avatar": null,
            "owner": 7,
            "block": 1
        },
        "location": {
            "id": 1,
            "name": "篮球场",
            "longitude": "123.123000",
            "latitude": "123.123000"
        },
        "block": {
            "id": 1,
            "name": "博雅"
        }
    }
]
```

**Error Response**

无





## 用户反馈

### 获取所有用户反馈 GET  `feedbacks/`

**权限**

管理端

**说明**

获取所有用户反馈

**Request**

URL：http://127.0.0.1:8000/feedbacks/

Body：无

**Success Response**

状态码：200

Body：

```json
[
    {
        "id": 2,
        "content": "反馈内容",
        "pub_time": "2021-04-19T14:17:21.157022",
        "user": 5
    },
    {
        "id": 3,
        "content": "反馈内容1",
        "pub_time": "2021-04-19T14:22:52.621137",
        "user": 6
    }
]
```

**Error Response**

无



### 新建用户反馈 POST `feedbacks/`

**权限**

用户端

**说明**

创建一个新的用户反馈

**Request**

URL：http://127.0.0.1:8000/feedbacks/

Body：

```json
{
    "content": "反馈内容",	//用户反馈的内容
    "user": 5	//用户的id
}
```

**Success Response**

状态码：201

Body：

```json
{
    "id": 2, 
    "content": "反馈内容",
    "pub_time": "2021-04-19T14:17:21.157022",
    "user": 5
}
```

**Error Response**

①

缺少content/user字段

状态码：400

Body：

```json
{
    "content": [
        "该字段是必填项。"
    ],
    "user": [
        "该字段是必填项。"
    ]
}
```



### 删除指定用户反馈 DELETE `feedbacks/{id}/`

**权限**

管理端

**说明**

删除编号为id的用户反馈

**Request**

URL：http://127.0.0.1:8000/feedbacks/4/（表示删除id=4的用户反馈）

Body：无

**Success Response**

状态码：204

Body：无

**Error Response**

对应id的用户反馈不存在

状态码：404

Body：

```json
{
    "detail": "未找到。"
}
```



## 超级管理员

### Super User注册 `register/`

**POST request**

Body

```json
{
    "username":"Jessica",
    "password":"123456",
    "email": "wangjiarui@163.com"
}
```



### SuperUser登录 `adminLogIn/`

**POST request**

Body

```json
{
    "username":"Jessica",
    "password":"123456",
}
```

**success response**

```json
{
    "success": "true",
    "user": {
        "username": "Jessica"
    }
}
```

**Error response**

```json
{
    "success": "false",
    "mess": "Invalid User"
}
```

