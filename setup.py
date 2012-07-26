from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

import pypack


setup(
    name='python-package-template',
    version=pypack.__version__,
    author='Gary Wilson Jr.',
    author_email='gary@thegarywilson.com',
    packages=['pypack'],
    entry_points={
        'console_scripts': [
            'pypack = pypack.commands:pypack_command',
        ],
    },
    include_package_data = True,
    url=pypack.__url__,
    license='MIT',
    description=("Provides a command to easily create a standard Python"
                 " package layout (i.e. package directory, README file,"
                 " setup.py, etc.)."),
    long_description=open('README.rst').read(),
)
