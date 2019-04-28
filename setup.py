#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1.0'

setup(
    author="seekplum",
    author_email='1131909224m@sina.cn',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    description="leetcode",
    install_requires=[

    ],
    scripts=[

    ],
    setup_requires=[

    ],
    include_package_data=True,
    name='leetcode',
    namespace_packages=['leetcode'],
    packages=find_packages(exclude=['tests', 'docs']),
    version=version,
    entry_points={
        'console_scripts': [
        ],
    }
)
