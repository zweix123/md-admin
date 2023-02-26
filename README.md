# md-admin
一个用Python实现的Markdown项目管理工具

+ 本项目使用Python开发，使用poetry作为版本管理, 请确保您的机器上有版本足够的Python且已经安装有poetry
    >关于poetry的使用，下面会提供足够的用法，如果想系统学习，可参考本人的[笔记](https://github.com/zweix123/CS-notes/blob/master/Programing-Language/Python/poetry.md)

## Install

+ 克隆仓库到本地并进入
+ 下载虚拟环境`python3 -m poetry init`

## Use

### Setting
在使用前请设置配置：文件`settings.py`中, 下面介绍其中的选项
```python
DIRPATH = ""  # 处理的Markdown项目文件绝对路径
URLP = ""  # 图床的URL前缀
MODE = ""  # NODE have OSS，node, blog, OSS
```
+ `DIRPATH`: 即为程序所管理的Markdown项目的根目录的绝对路径
+ `URLP`: 和图床相关，无论你使用什么作为图床，其中的图片一定有一个共有的前缀，请填写在这里
+ `MODE`: 和图床相关，有不同的组织图床的方式
    + `OSS`: 所有的图片都在一个路径下
    + `blog`: 在图床的根目录以各个文章的文章名创建目录，这个文章的图床在对应名字的路径下
    + `note`: 一种有组织的文件结构, 每个文件中使用的图片在图床下有和其文章到根目录同样的相对路径前缀

    >后续如果有机会会更仔细的描述这方面

### CMMAND

查看帮助
```python
python main.py  # poetry虚拟环境下
python3 -m poetry run python main.py -h  # 普通环境
```

+ `cnt`：统计字数
+ `perl`：按配置中的路径和模式批量修改图床
+ `table`：批量生成或更新目录, 是同方言`[TOC]\n`(要求必须在每行的开始并且后面有`\n`)
    >注意这里的TOC不是类似Typora和VSCode的软件内的功能，而是真的文本替换

### develop

我不清楚项目的文件结构是否合理, 但我个人认为比较有规律，适合扩展，如果有时间，我会仔细描述一下。