#!/usr/bin/python3
"""command line terminal"""
import cmd
import sys
import models.base_model as base


class HBNBCommand(cmd.Cmd):
    """Startin point"""

    if sys.stdin.isatty():
        prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to to exit the program"""
        return True

    def do_eof(self, arg):
        """eof for quiting"""
        if arg == "eof":
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()