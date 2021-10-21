#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
import drf_camel_case

setup(
    name="drf-camel-case",
    version=drf_camel_case.__version__,
    description="Camel case JSON support for Django REST framework with orjson.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Roland Kainrath",
    author_email="justintimedev@gmail.com",
    url="https://github.com/JITdev/drf-camel-case",
    packages=["drf_camel_case"],
    package_dir={"drf_camel_case": "drf_camel_case"},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=['orjson'],
    license="BSD",
    zip_safe=False,
    keywords="drf_camel_case, django rest framework, django",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
)
