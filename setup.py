'''A helper library for SQLAlchemy (particularly for automap and reflection)

See:
https://github.com/jhannah01/sqlenv
'''

import os.path
import codecs
import pkg_resources
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = None

from sqlenv import __version__ as sqlenv_version

setup(
    name='sqlenv',
    version=sqlenv_version,
    description='A helper library for SQLAlchemy (particularly for automap and reflection)',
    long_description=long_description,
    url='https://github.com/jhannah01/sqlenv',
    license='GNU',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='sa sqlalchemy sqlenv saenv sahelper',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'sqlalchemy',
        'MySQL-Python'
    ],
)

