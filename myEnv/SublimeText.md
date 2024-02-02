# 备用场景
## 预览Markdown文档
cmd+shift+p > Markdown Preview > PreviewBrowser

# 插件
`安装`
Preferences > Package Control > Install Package > Dracula Color Scheme

`主题应用`
Preferences > Theme > Dracula Color Scheme

`插件-系统安装时补充`
- 主题：ayu, Dracula Color Scheme
- 图标：A file icon
- MarkdownPreview

# 快捷键
## Mac
- 打开Package Control: ctrl+shift+p/cmd+shift+p
- 记住上次打开的文件夹：cmd+q(不能直接关闭软件).

## Windows
### Choose
- 用`ctrl+d`来连续选择多个相同单元；
- `shift+`右键拖动；
- 选择括号内的内容: `ctrl+shift+m`；
- 光标移动至括号内结束或开始的位置：`ctrl+m`；
- 选择当前文件所有匹配项: `alt+f3`；
- 选择整行：`ctrl+L`；

### Line and Indentation
- 移动行，`ctrl+shift+arrow`
- 复制行或选中项: `ctrl+shift+d`
- 删除行，`ctrl+shift+k`
- 单行剪辑或选中项: `ctrl+x`
- 同时移动，`ctrl+[/]`
- 多个行对齐，Edit/Line/reindent
- 对齐粘贴，`ctrl+shift+v`
- 在上一行插入行：`ctrl+shift+enter`
- 在下一行插入行：`ctrl+enter`

### 其他
- 大写和小写: 大写`ctrl+k+u`、小写`ctrl+k+l`
- 注释选中项/行: `ctrl+/`
- 选中代码，折叠/展开代码：`ctrl+shift+[ / ]`
- 展开所有折叠行：`ctrl+k+0`

# Tips
## Goto Anything
- 将文件夹导入sublime text
- ctrl+p
- m@bar，文件之间导航
- T@Fri，文件内导航
- T:16，导航到具体的行
- See unsaved changes
- 同时打开多个文件
- Save a project

## Command Palette
- 打开Command Palette, `Ctrl+shift+p`
- 大写-排序

## Package Manager
- 1 打开Package Manager
- 2 安装包，`ctrl+shift+p`==>install package==>color hightlighter

## Snippets
- **Make snippets second nature**
- Tools/Developer/New Snippet

```xml
<snippet>
	<content><![CDATA[
--data des
select

from
    
where
    1=1
    and 
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>select</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>source.sql</scope>
</snippet>
```

## Emmet
- Snippet Engine

## Create our own snippet
- sql语言 myselect.sublime-snippet

## Key Bindings
- `{"keys": ["ctrl+shift+i"], "commands": "reindent"}`
- View/Console⇒`sublime.log_commands(True)`，查看动作的对象。

