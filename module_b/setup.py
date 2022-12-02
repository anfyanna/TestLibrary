import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='module_b',
    version='0.0.0',
    author='Anna Liu',
    author_email='sonoanna@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anfyanna/TestLibrary/module_b',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=[
        'module_b',
        # 'pklib.constants',
        # 'pklib.utils',
        # 'pklib.constants.banks'
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