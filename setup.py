from setuptools import setup

setup(
    name = 'mypackage',
    version = '0.1.0',
    author = 'Lathan Gregg',
    author_email = 'uua9gw@virginia.edu',
    packages = ['mypackage'],
    license = 'LICENSE.txt',
    description = 'An awesome package that does something',
    long_description = open('README.md').read(),
    install_requires = [
        "pytest",
        "numpy",
        "pandas"
    ]
)