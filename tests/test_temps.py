


import temps
import os

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


