"""
 * py-smtper OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2024 - ali sharifi
 * https://github.com/alisharify7/py-smtper
"""

from setuptools import setup, find_packages

__NAME__ = "py-smtper"
__version__ = "1.0.0"
__author__ = "ali sharify"
__author_mail__ = "alisharifyofficial@gmail.com"
__copyright__ = "ali sharify - 2024"
__license__ = "MIT"
__short_description__ = "python client library for sending smtp request (emails) easily." 


with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name=__NAME__,
    version=__version__,
    description=__short_description__,
    packages=find_packages(),
    author_email=__author_mail__,
    author=__author__,
    url="https://github.com/alisharify7/py-smtper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Environment :: Web Environment",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
    ],
    license="MIT",
    install_requires=[
    ],
    python_requires=">=3.8",
    keywords="smtp, python-email, send-email, py-smtper, py-mailer, python-smtp-email",
)