from distutils.core import setup
from setuptools import setup, find_packages
from querySalt import __get_version__

setup(
    name='querySalt',
    version=__get_version__,
    packages = find_packages( ),
    include_package_data=True,
    install_requires=['requests'],
    url='http://github.com/depill/querySalt',
    license='LGPL',
    author='David Fannar Gunnarsson',
    author_email='david@madpuffin.com',
    description='Simple service to Query Salt API'
)
