import temps
import os
from subprocess import Popen
from subprocess import PIPE
from nose.tools import eq_
from tempfile import gettempdir
from shutil import rmtree

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

class TestTempsDir:
    def _popen(self, overrides=None):
        """
        :type override: (str, str)
        :param override: (var, val)
        """

        if not overrides:
            overrides = []

        p = Popen(
            ["env", "-i"]
            + ["=".join(xs) for xs in overrides]
            + ["python", "-c", "import temps; print temps.TEMPS_DIR;"]
            , stdout=PIPE, stderr=PIPE
        )
        out, _ = p.communicate()
        return out.strip()

    def setUp(self):
        self.tmpdir = '/tmp/foo'
        os.makedirs(self.tmpdir)
        # L{tempfile.gettempdir} checks wheter the dir is
        # readable/writable, if not it continues fallbacking

    def tearDown(self):
        rmtree(self.tmpdir)

    def test_pure_fallback(self):
        """
        Test we get the `gettempdir`s platform specific fallback when
        give no env overrides
        """
        eq_(self._popen(), gettempdir())

    def test_gettempdir_env_var(self):
        """
        Test we get an override handled by `gettempdir`
        """
        eq_(self._popen([("TMP", self.tmpdir)]), self.tmpdir)

    def test_temps_env_var(self):
        """
        Test we get an override for temps itself
        """
        v = "/foo2"
        eq_(self._popen(dict(TMP = self.tmpdir, TEMPS_DIR = v).items()), v)
