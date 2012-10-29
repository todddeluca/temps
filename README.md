
## Introduction

`temps` is a python module containing context managers for creating and
cleaning up temporary files and directories.

This package is _alpha_ and its API is not stable.

Why do I never use the `tempfile` module?

- I am responsible for removing files and dirs tempfile creates, which creates
  lots of boilerplate whenever I use it.
- There is no context manager for temp dirs.
- When using `mkstemp()`, I get an open file descriptor, not a file object,
  that I have to close.
- The context manager for temp files contains statements like this
  from the tempfile docs: "Whether the name can be used to open the file a
  second time, while the named temporary file is still open, varies across
  platforms"
- I do not get to choose the file perms of files and dirs I create.

What do I like about this module?

- It has a context manager for creating a temp dir and another for temp files.
- The context manager cleans up the dir or file upon context exit, not upon file
  closure.
- No ambiguity about whether you can or cannot open a file twice.
- You can set the permissions of the temp file or dir to what you want.
- It is very clear what the implementation is:
    - directories are created and the path is returned.
    - files are not created, since you'll want to do that in a `with
      open(filename) ...` statement, and the path is returned.
    - directories and files are cleaned up by the context managers.
    - file and dir names are generated using the uuid module, which presumably
      will avoid race conditions.


## Contribute

Feel free to make a pull request on github.


## Requirements

- Probably Python 2.7 (since that is the only version it has been tested with.)


## Installation


### Install from pypi.python.org

Download and install using pip:

    pip install temps


### Install from github.com

Using github, one can clone and install a specific version of the package:

    cd ~
    git clone git@github.com:todddeluca/temps.git
    cd temps
    python setup.py install


## Usage

Creating a working dir for subprocesses:

    with temps.tmpdir() as workdir:
        with open(os.path.join(workdir, 'datafile'), 'wb') as fh:
            fh.write(data)
        subprocess.call('compute.sh {}'.format(workdir), shell=True)
        with open(os.path.join(workdir, 'outfile')) as fh:
            print fh.read()

Creating a temp file for a transform and upload:

    with temps.tmpfile() as transformed_path:
        transform(input_path, transformed_path)
        upload(transformed_path, destination)

The default values when parameters are not specified, are stored in variables
that are set using environment variables if available or a default value
otherwise.  Here is a table listing the variable, the environment variable 
checked, and the default value:

    Variable, ENV_VAR, Default
    TEMPS_DIR, TEMPS_DIR, os.cwd()
    TEMPS_PREFIX, TEMPS_PREFIX, ''
    TEMPS_SUFFIX, TEMPS_SUFFIX, ''
    TEMPS_MODE, TEMPS_MODE, '0777'




