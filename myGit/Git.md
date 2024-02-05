# Q
为什么有的文件并不能被添加？

# 连接GitHub/GitLab
## 账户信息

```shell
#设置用户名
git config --global user.name 'TY02'
#设置邮箱
git config --global user.email 'ty02@gmail.com'
#检查信息
git config --list    # 通过q退出; vim退出:q
```

## 连接GitHub-为GitHub添加SSH keys   
- 进入：cd ~/.ssh   
- 生成ssh密钥：ssh-keygen -t rsa -C "email@xxx.com"   
- 忽略密码输入   
- 添加ssh: ssh-add ~/.ssh/id_rsa   
- 官网设置新的key, 查看key: vim ~/.ssh/id_rsa.pub   

## 连接GitLab-为GitLab添加SSH keys    
- 打开git Bash，并输入：ssh-keygen -t rsa -C "user_test@user.test"，其中 "user_test@user.test"为自己的账号    
- 之后一直按enter键（密码可空可设置）   
- 然后在git的安装目录下找到.ssh文件，用文本编辑器打开id_rsa.pub,并将内容全部复制到GitLab中SSH Keys中Add an SSH Key中。   

## 同时连接Gitlab和GitHub-不再生效
```shell
# 连接GitHub
git config -- user.email 'github_user_name@xxxx.com'
git config -- user.name 'github_user_name'

# 连接GitLab
git config -- user.email 'gitlab_user_name@xxxx.com'
git config -- user.name 'gitlab_user_name'
```
# Git操作
## 创建-克隆
``` shell
# 克隆
git clone https://github.com/ThomasYounger02/DataScience.git
```
## 创建-本地
``` shell
# 本地创建
## 创建文件夹
mkdir file_folder
cd file_folder

## 初始化git
git init        # .git存储所有信息

## git remote add 用于创建一个 origin 简写名，指向 GitHub 上的项目。
git remote add origin https://github.com/richardkalehoff/RichardsFantasticProject.git

## 验证是否已经正确添加了远程仓库
git remote -v
```

## 常用操作
```shell
## 文件操作
cd file_path                 # 进入文件
cd . 
cd ..
ls                           # 文件列表

touch
cat
vim

## 状态
git status

## 添加
git add README.md               # 添加文件
git add file_folder/            # 添加整个文件夹及内容
git add *.file_type             # 添加目录中所有此文件类型的文件
git add all                     # 添加全量文件
git add *                       # 添加全量文件
git add -A                      # 删除的文件--本地文件删除后，用该命令同步

git rm READ.md                  # 删除文件 

## 提交
git commit -m 'docs' -m 'add README file'        # 提交文件

## 同步
git push        # 将本地仓库的内容同步至远程仓库
```

# comment 书写标准
## 类型1-如何写comment
```markdown
feat: Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequenses of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

## 类型2
简化后的版本

# 备用信息
`首页`
- [GitHub](https://github.com/)
- [GitHub](https://github.com/)
- [DiDi](git@git.xiaojukeji.com:{name}/ivoryshark.git)
- [Ant](gitlab.alibaba-inc.com)