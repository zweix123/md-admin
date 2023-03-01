# md-admin
一个用Python实现的Markdown项目管理工具

+ 本项目使用Python开发，使用poetry作为版本管理, 请确保您的机器上有版本足够的Python且已经安装有poetry
    >关于poetry的使用，下面会提供足够的用法，如果想系统学习，可参考本人的[笔记](https://github.com/zweix123/CS-notes/blob/master/Programing-Language/Python/poetry.md)

## Contents
- [md-admin](#md-admin)
  - [Contents](#contents)
  - [Install](#install)
  - [Use](#use)
    - [Setting](#setting)
    - [run](#run)
  - [develop](#develop)

## Install

+ 克隆仓库到本地并进入
+ 下载虚拟环境`python3 -m poetry install`

## Use

### Setting
在使用前请设置配置：文件`settings.py`中的几个常量，含义见注释和注解
```python
DIRPATH = ""  # 处理的Markdown项目目录绝对路径
DIRNAME = ""  # 处理的Markdown项目目录目录名
URLP = ""  # 图床的URL前缀
MODE = ""  # NODE(node, blog, OSS)
"""
关于常量MODE, 指的是图床下的文件结构, 我们以这样的项目结构来解释不同模式的区别   
.
|--os
|  |--file(file1.jpg, file2.jpg)
|  `--coroutine(coroutine1.jpg, coroutine.jpg)
|--DS
   |---consensus    
   |     |------PacificA()
   |     |------Raft(leader.jpg, copyset.jpg)
   `--storage
         |-----GFS(gfs.jpg)
         `-----Ceph(ceph.png)
1. note: 对于每个文章内的图片, 该文章相对项目根目录的相对路径和图片相对图床的相对路径是一致的.比如(文件后括号内为文件所用图床)    
.
|--os
|  |---file1.jpg
|  |---file2.jpg
|  |---coroutine1.jpg
|  |---coroutine.jpg
|--DS
    |---consensus
    |       |------leader.jpg
    |       |------copyset.jpg
    |---storage
            |---gfs.jpg
            |---ceph.png
2. blog: 所有图片以所属的文章为单位平铺在图床下
.
|---file
|    |----file1.jpg
|    `----file2.jpg
|---coroutine
|      |------coroutine1.jpg
|      `------coroutine2.jpg
|---PacificA
|---Raft
|    |---leader.jpg
|    `---copyset.jpg
|---GFS
|    `---gfs.jpg
`---Ceph
     `---ceph.png
3. OSS: 所有图片都平铺在图床下
.
|--file1.jpg
|--file2.jpg
|--coroutine1.jpg
|--coroutine2.jpg
|--leader.jpg
|--copyset.jpg
|--gfs.jpg
`--ceph.png

example:
DIRPATH = r"C:\Users\zweix\Documents\CS-notes"
DIRNAME = "CS-notes"
URLP = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source"
MODE = "note"
"""
```

### run
>关于poetry管理的虚拟环境的运行有两种方法
>1. 通过命令`poetry shell`进入虚拟环境，之后就像普通的Python程序一样运行
>2. 命令添加`python3 -m poetry run`前缀, 之后的部分相当于普通的Python程序一样运行
>+ 普通的的Python程序运行`Python main.py`

+ "核心命令":查看帮助:dog:
    + `python main.py --help`：即可查看命令
    + `python main.py COMMAND --help`：即可查看对应命令的标记

    >本项目的有配置文件，所有不需要参数。

## develop
