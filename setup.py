'''A helper library for SQLAlchemy (particularly for automap and reflection)

See:
https://github.com/jhannah01/sqlenv
'''

import os.path
import codecs
import pkg_resources
from setuptools import setup, find_packages

from sqlenv import __version__ as pkg_version


here = os.path.abspath(os.path.dirname(__file__))

try:
    with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = None

pkg_name = 'sqlenv'
pkg_description = 'A helper library for SQLAlchemy'
pkg_requirements = [
    'beautifultable',
    'beautifulsoup4',
    'simplejson',
    'sqlitedict',
    'sqlalchemy',
    'MySQL-Python']
pkg_keywords = 'sa sqlalchemy sqlenv saenv sahelper'
# pkg_version = '0.2'

setup(
    name=pkg_name,
    version=pkg_version,
    description=pkg_description,
    long_description=long_description,
    url='https://github.com/jhannah01/%s' % pkg_name,
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
    keywords=pkg_keywords,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', '.local']),
    install_requires=pkg_requirements
)
