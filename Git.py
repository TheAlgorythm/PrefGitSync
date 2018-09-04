import subprocess


class Git:

    class GitError(Exception):
        def __init__(self, error):
            self._error = error

        def getError(self):
            return self._error

    _path = ""

    def getPath(self):
        return self._path

    def setPath(self, value):
        self._path = value

    def check_exists(self):
        try:
            subprocess.check_output(['git', '--version'])
            return True
        except (OSError, subprocess.CalledProcessError):
            return False

    def check_exists_with_error(self):
        if not self.check_exists():
            assert Git.GitError("git not found, please run and fix './fips diag tools'")
        return True

    def execute(self, cmd):
        self.check_exists_with_error()
        try:
            subprocess.check_call(cmd, cwd=self.getPath(), shell=True)
        except subprocess.CalledProcessError as e:
            assert Git.GitError("'{}' failed with '{}: {}'".format(cmd, e.returncode, e.output))

    def init(self):
        self.execute('git init')

    def pull(self):
        self.execute('git pull')

    def stageModified(self):
        self.execute('git add -u')

    def commit(self, msg):
        self.execute('git commit --allow-empty -m "{}"'.format(msg))

    def push(self, remote, branch):
        self.execute('git push {} {}'.format(remote, branch))
