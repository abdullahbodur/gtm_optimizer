import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name="optimizer",
    version="0.0.1",
    url="https://github.com/abdullahbodur/gtm_optimizer",
    author="bodur",
    author_mail="abdullahbodur.abbdr@gmail.com",
    packages=find_packages(),
    install_requires=[],
    description="A dataset optimizer for GTM Trading analyzer.",
)