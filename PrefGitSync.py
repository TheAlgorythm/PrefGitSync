import sublime
import sublime_plugin
from .Git import Git


class PrefGitSyncUpdateCommand(sublime_plugin.ApplicationCommand):

    def run(args):
        git = Git()
        userPath = sublime.packages_path() + "/User"
        git.setPath(userPath)
        try:
            git.pull()
        except Git.GitError as e:
            print(e.getError())
            sublime.error_message("Error:\nPlease open console")


class PrefGitSyncSaveCommand(sublime_plugin.ApplicationCommand):

    def run(args):
        try:
            git = Git()
            userPath = sublime.packages_path() + "/User"
            git.setPath(userPath)
            git.stageModified()
            git.commit("save")
            git.push("origin", "master")
        except Git.GitError as e:
            print(e.getError())
            sublime.error_message("Error:\nPlease open console")


class PrefGitSyncInitCommand(sublime_plugin.ApplicationCommand):

    def run(args):
        git = Git()
        userPath = sublime.packages_path() + "/User"
        git.setPath(userPath)
        try:
            git.init()
        except Git.GitError as e:
            print(e.getError())
            sublime.error_message("Error:\nPlease open console")
