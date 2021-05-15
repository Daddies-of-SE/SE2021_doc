# Git使用



## 同时关联Github与华为云

1. 登陆华为云，进入项目管理页面

2. 进入 代码-代码托管

3. 点击“设置我的SSH密钥”，添加自己的SSH公钥

   > 一般路径为~/.ssh/id_rsa.pub
   >
   > win下在命令行输入clip < id_rsa.pub将公钥复制到粘贴板

4. 回到代码托管页，选择要关联的仓库，复制其SSH地址（下文用`${ssh_url}`表示）

5. 进入本地仓库的目录

6. 输入`git remote add ${repo_name} ${ssh_url}`关联华为云上的远程仓库，其中`${repo_name}`可自行定义，是远程仓库的别称，建议定为hwcloud



关联后，push代码的指令为`git push ${repo_name} ${branch_name}`，通过`${repo_name}`选择要push到的远程仓库，`${branch_name}`选择要push的分支



注：使用`git remote -v`可以查看所有关联的远程仓库

```bash
Small@small-dell MINGW64 /d/Codes/SoftwareEngneering/Web (main)
$ git remote add hwcloud git@codehub.devcloud.cn-north-4.huaweicloud.com:ARS-FR-2_wzk101500001/web.git

Small@small-dell MINGW64 /d/Codes/SoftwareEngneering/Web (main)
$ git push hwcloud main
The authenticity of host 'codehub.devcloud.cn-north-4.huaweicloud.com (124.70.100.129)' can't be established.
RSA key fingerprint is SHA256:...... .
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'codehub.devcloud.cn-north-4.huaweicloud.com,124.70.100.129' (RSA) to the list of known hosts.
Enumerating objects: 36, done.
Counting objects: 100% (36/36), done.
Delta compression using up to 4 threads
Compressing objects: 100% (26/26), done.
Writing objects: 100% (27/27), 8.23 KiB | 702.00 KiB/s, done.
Total 27 (delta 22), reused 0 (delta 0), pack-reused 0
To codehub.devcloud.cn-north-4.huaweicloud.com:ARS-FR-2_wzk101500001/web.git
   4949838..5b98b72  main -> main

Small@small-dell MINGW64 /d/Codes/SoftwareEngneering/Web (main)
$ git remote -v
hwcloud git@codehub.devcloud.cn-north-4.huaweicloud.com:ARS-FR-2_wzk101500001/web.git (fetch)
hwcloud git@codehub.devcloud.cn-north-4.huaweicloud.com:ARS-FR-2_wzk101500001/web.git (push)
origin  git@github.com:Daddies-of-SE/ReedSailing-Web.git (fetch)
origin  git@github.com:Daddies-of-SE/ReedSailing-Web.git (push)
```

