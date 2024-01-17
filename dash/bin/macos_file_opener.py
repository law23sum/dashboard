import subprocess
import sys
from enum import Enum


class OpenOptions(Enum):
    APPLICATION = '-a'
    BUNDLE = '-b'
    TEXTEDIT = '-e'
    URL = '-u'
    ARGS = '--args'
    NEW = '-n'
    HIDE = '-j'
    BACKGROUND = '-g'
    BLOCK = '-W'
    STDIN = '--stdin'
    STDOUT = '--stdout'
    STDERR = '--stderr'
    ENV = '--env'


class MacOSFileOpener:

    @staticmethod
    def open_file_with_option(
            filename: str, option: OpenOptions, arg: str = ''
            ):
        """
        Opens a file using the specified option and argument.
        """
        subprocess.call(['open', option.value, arg, filename])

    @staticmethod
    def open_url(url: str):
        """
        Opens a URL in the default web browser.
        """
        subprocess.call(['open', OpenOptions.URL.value, url])

    @staticmethod
    def open_app_with_args(app_name: str, args: str):
        """
        Opens an application with provided arguments.
        """
        subprocess.call(
                ['open', OpenOptions.APPLICATION.value, app_name,
                 OpenOptions.ARGS.value, args]
                )


if __name__ == "__main__":
    opener = MacOSFileOpener()

    if len(sys.argv) < 4:
        print("Usage: python3 macos_file_opener.py [file|url] [option] [arg]")
    else:
        action, option, arg = sys.argv[1], sys.argv[2], sys.argv[3]

        if action == 'file':
            opener.open_file_with_option(
                option, getattr(OpenOptions, arg.upper()), ''
                )
        elif action == 'url':
            opener.open_url(option)
        elif action == 'app':
            opener.open_app_with_args(option, arg)
        else:
            print("Invalid action. Please choose 'file', 'url', or 'app'.")
