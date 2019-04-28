# leetcode

[![LICENSE](https://img.shields.io/github/license/seekplum/leetcode.svg)](https://github.com/seekplum/leetcode/blob/master/LICENSE)[![travis-ci](https://travis-ci.org/seekplum/leetcode.svg?branch=master)](https://travis-ci.org/seekplum/leetcode)[![coveralls](https://coveralls.io/repos/github/seekplum/leetcode/badge.svg?branch=master)](https://coveralls.io/github/seekplum/leetcode?branch=master) [![pypi version](https://img.shields.io/pypi/v/leetcode.svg)](https://pypi.python.org/pypi/leetcode) [![pyversions](https://img.shields.io/pypi/pyversions/leetcode.svg)](https://pypi.python.org/pypi/leetcode)

## 项目的git hooks

由于钩子文件无法提交到 `.git` 中，所以在第一次clone项目中需要执行以下命令，把钩子放到指定位置

```bash
cp -r hooks/* .git/hooks/
```

## 题库

* [英文官网](https://leetcode.com/problemset/all/)
* [中文题库](https://leetcode-cn.com/problemset/all/)

## 源码

源码目录在 `src` 目录下

## 测试文件

针对每个源码文件会有对应的测试文件在 `tests` 目录下

## 依赖管理
通过 `pipenv` 对项目依赖的三方库进行管理

## 目录结构


```text
➜  tree -L 1 -a
.
├── .bumpversion.cfg    # `bumpversion`工具的配置文件，用于自动更新版本
├── .env                # 环境变量配置,`不会提交到gitlab中`
├── .gitignore          # 维护git仓库需要忽略文件
├── .gitlab-ci.yml      # gitlab ci的配置文件
├── .pylintrc           # pylint 配置文件
├── CHANGELOG.md        # 记录模块的变化
├── MANIFEST.in         # 打包时添加文件或移除文件等的配置
├── Pipfile             # python依赖包版本文件
├── Pipfile.lock        # 根据Pipfile生成的版本锁文件
├── README.md           # 项目自述文件
├── VERSION             # 项目版本文件
├── bin                 # 项目二进制程序
├── docs                # 项目文档
├── leetcode          # 核心代码模块
├── setup.cfg           # 安装配置文件
├── setup.py            # 安装脚本
├── tasks.py            # 任务执行脚本
└── tests               # 单元测试目录

```

## 安装环境依赖

1.安装pipenv

```bash
pip install pipenv
```

2.安装项目依赖环境

```bash
pipenv --two install --deploy # py2
pipenv --three install --deploy # py3
```

## 运行单元测试

首先需要进入我们安装的虚拟环境

```bash
pipenv shell
```

### 第一种

```bash
inv coverage
```

### 第二种

```bash
inv unittest
```

## 检查Python代码规范

```bash
inv check
```

## 详细文档

见[项目文档目录](docs/README.md)
