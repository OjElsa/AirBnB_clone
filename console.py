#!/usr/bin/python3

"""Module for the command interprator"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interparator Class"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
