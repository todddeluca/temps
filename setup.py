
import os
from setuptools import setup, find_packages

def version(modfile):
    '''
    Parse version from module without importing or evaluating the code.
    The module should define a __version__ variable like __version__ = '2.0.1'.
    '''
    import re
    with open(modfile) as fh:
        for line in fh:
            m = re.search(r"^__version__ = '([^']+)'$", line)
            if m:
                return m.group(1)
    raise Exception('No __version__ string found in {fn}'.format(fn=modfile))


setup(
    name = 'temps',
    version = version('temps.py'),
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

