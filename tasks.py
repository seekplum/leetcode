# -*- coding: utf-8 -*-

from invoke import task


@task
def clean(ctx):
    ctx.run("find . -name '*.pyc' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '*.pyo' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '__pycache__' -exec rm -rf {} +", echo=True)
    ctx.run("find . -name 'htmlcov' -exec rm -rf {} +", echo=True)
    ctx.run("find . -name '.coverage*' -exec rm -rf {} +", echo=True)
    ctx.run("find . -name '.cache' -exec rm -rf {} +", echo=True)
    ctx.run("find . -name '.pytest_cache' -exec rm -rf {} +", echo=True)
    ctx.run("find tests -name '*.db' -exec rm -rf {} +", echo=True)
    ctx.run("find tests -name '*.log' -exec rm -rf {} +", echo=True)


@task(clean)
def check(ctx):
    """检查代码风格"""
    ctx.run("export PYTHONPATH=`pwd`/src && pylint src tests", echo=True)


@task(clean)
def unittest(ctx):
    """运行单元测试和计算测试覆盖率"""
    ctx.run("export PYTHONPATH=`pwd`/src && pytest --cov=src tests", echo=True)


@task
def lock(ctx):
    """生成Pipfile.lock文件"""
    ctx.run("pipenv lock -v --keep-outdated", echo=True)
