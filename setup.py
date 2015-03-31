from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='querySalt',
    version=0.002,
    packages = find_packages( ),
    include_package_data=True,
    install_requires=['requests'],
    url='http://github.com/depill/querySalt',
    license='LGPL',
    author='David Fannar Gunnarsson',
    author_email='david@madpuffin.com',
    description='Simple service to Query Salt API'
)
