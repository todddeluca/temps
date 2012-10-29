
import os
from setuptools import setup, find_packages

setup(
    name = 'temps',
    version = '0.1',
    license = 'MIT',
    description = 'Context managers for creating and cleaning up temporary directories and files.',
    long_description = open(os.path.join(os.path.dirname(__file__),
                                         'README.md')).read(),
    keywords = 'python temporary files directories context manager',
    url = 'https://github.com/todddeluca/temps',
    author = 'Todd Francis DeLuca',
    author_email = 'todddeluca@yahoo.com',
    classifiers = ['License :: OSI Approved :: MIT License',
                   'Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                  ],
    py_modules = ['temps'],
)

