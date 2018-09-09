# -*- encoding: utf-8 -*-

__author__ = 'laye'
__version__ = "0.0.1"
__copyright__ = ""
__licence__ = "The MIT License"

from setuptools import setup, find_packages

setup(
      name='mendola', 
      version='0.0.1',
      description='some useful python algorithms.',
      author='Laye', 
      author_email='wuch84@126.com',
      url='https://github.com/vocky',
      include_package_data=True,
      zip_safe=False,
      packages=find_packages(),
      install_requires=['bitstring',
                        'enum34'
                        ],
     )
