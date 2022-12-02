import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PKConstants',
    version='0.0.0',
    author='Anna Liu',
    author_email='sonoanna@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anfyanna/TestLibrary/PKConstants',
    project_urls = {
    },
    license='MIT',
    packages=[
        'pk_constants',
        'pk_constants.constants',
        ], #list of packages that your package relies upon.
    install_requires=[ # these would be installed first.
        # 'after_response',
        # 'requests',
        # 'Django<=3.2',
        # 'nanoid',
        # 'pypinyin',
        # 'PIL'
        ], 
)