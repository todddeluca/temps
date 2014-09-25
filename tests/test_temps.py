import temps
import os
import tempfile
import contextlib


@contextlib.contextmanager
def environ_cm(var, val):
    '''
    Set an environment variable to a specific value temporarily.
    When done, if there was a preexisting value, reset it to that.
    Otherwise, delete the temporary env var.
    '''
    existing = os.environ.get(var)
    try:
        os.environ[var] = val
        yield
    finally:
        if existing is None:
            del os.environ[var]
        else:
            os.environ[var] = existing


def test_tmpfile():
    with temps.tmpfile() as path:
        assert not os.path.exists(path)
        with open(path, 'w') as fh:
            fh.write('test')
        assert os.path.exists(path)
    assert not os.path.exists(path)


def test_tmpdir():
    path = None
    with temps.tmpdir() as td:
        assert os.path.isdir(td)
        path = os.path.join(td, 'test')
        with open(path, 'w') as fh:
            fh.write('test')
        assert os.path.exists(path)
    assert not os.path.exists(path)
    assert not os.path.exists(td)


def test_tmppath():
    path = temps.tmppath()
    assert not os.path.exists(path)
    try:
        os.mkdir(path)
    finally:
        if os.path.isdir(path):
            os.rmdir(path)


def test_temps_env_var_fallback():
    '''
    Test that temps uses `gettempdir` when given no TEMPS_DIR env var
    '''
    with environ_cm('TEMPS_DIR', ''):
        print 'test_pure_fallback'
        print temps._set_temps_dir()
        print tempfile.gettempdir()
        assert temps._set_temps_dir() == tempfile.gettempdir()


def test_temps_env_var_override():
    '''
    Test that temps uses the env var TEMPS_DIR when it is set.
    '''
    d = '/temps_test_tmp_2'
    with environ_cm('TEMPS_DIR', d):
        print 'test_temps_env_var'
        print temps._set_temps_dir()
        print d
        assert temps._set_temps_dir() == d

