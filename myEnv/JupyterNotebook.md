# 简介
> Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——Jupyter Notebook官方介绍

# 执行shell命令
```python
! pip install package_name        # 以符号!开始
! pip install --upgrade seaborn   # 更新包

print(sns.__version__)            # 查看包的版本
```

# 插件Nbextentions安装
```shell
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge jupyter_nbextensions_configurator
```

# 在JupyterNotebook中运行脚本
```python
%run 'Python文件的绝对路径'
```

# Markdown在文中设置链接并定位
```markdown
[添加链接的正文](#自定义索引词)
<a id=自定义索引词>跳转提示</a>
```

- “自定义索引词”最好是英文，较长的词可以用下划线连接。
- “a标签”出现在想要被跳转到的文章位置，html标签除了单标签外均要符合“有头（`<a>`）必有尾（`</a>`）”的原则。头尾之间的“跳转提示”是可有可无的。
- “a标签”中的“id”值即是为正文中添加链接时设定的“自定义索引值”，这里通过“id”的值实现从正文的链接跳转至指定位置的功能。