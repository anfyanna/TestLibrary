from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PKTools',
    version='0.0.0',
    author='Anna Liu',
    author_email='sonoanna@pocket.tw',
    description='Package for Pocket python projects.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anfyanna/TestLibrary/',
    project_urls = {
    },
    license='MIT',
    packages=find_packages(), #list of packages that your package relies upon.
    install_requires=[ # these would be installed first.
        'requests',
        # 'requests',
        # 'Django<=3.2',
        # 'nanoid',
        # 'pypinyin',
        # 'PIL'
        ], 
)