from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydata_jy',
    version='1.0.0',
    description='PyData Location List',
    long_description=long_description,
    url='https://github.com/takezyou/pydata',
    author='jseo',
    author_email='sjy950462@gmail.com',
    license='MIT',
    install_requires=['beautifulsoup4', 'lxml'],
    keywords='pydata_jy',
    packages=find_packages,
    entry_points={
        "console_scripts": [
            "pydata_jy=pydata_jy.__init__:main",
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)