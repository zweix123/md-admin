这是一个用Python实现的Markdown项目管理工具集，环境管理使用Python的第三方库poetry
>我的Python版本是3.11.1，portry库版本是1.3.2
>+ 如果您的Python版本不能运行`portry install`，可以直接修改poetry的配置文件到您机器的版本

```
.
├── cnt.py
├── perl.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── settings.py
└── zweixlib.py
```




 
# 附录
## poetry
poetry是Python的第三方库、一个包管理器。

+ 在项目中生成配置文件：`python3 -m poetry init`
    + 配置文件：简单易懂
        + `pyproject.toml`
        + `poetry.lock`
+ 进入虚拟环境中：`python3 -m poetry shell`
+ 库管理：
    + 添加库：`poetry add 库名`
    + 删除库：`poetry remove 库名`

+ 利用配置加载依赖包：`python3 -m poetry install`（下载的包是独立于本地的）
+ 运行程序：``