#!/usr/bin/python3

"""Module for the command interprator"""

import sys
import cmd
import json
import shlex
from models import storage
from models import base_model
from models import FileStorage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Command Interparator Class"""

    prompt = "(hbnb) "
    storage = FileStorage()
    storage.reload()

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handles the End Of File Charachter"""
        print()
        return True

    def do_create(self, line):
        """Create a new instance of the BaseModel and save it to JSON file"""
        if not line:
            print("** class name missing **")
            return

        class_name = line.split()[0]
        if not hasattr(base_model, class_name):
            print("** class doesn't exist **")
            return
        
        new_instance = getattr(base_model, class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance."""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class does not exist **")
        elif len(args) == 1:
            print("** insatnce id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Destroy an instance based on the class name and id."""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** clas doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key  not in storage.all():
                print("** no innsatance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Print all string represnaattion of all instance."""
        args = shlex.split(line)
        instances = HBNBCommand.storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(instance) for key, instance in instances.items()
                if instance.__class__.__name__ == class_name])

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** inastance id issing **")
        elif args[0] + "." + args[1] not in strorage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            instance = storage.all()[key]
            setattr(instance, args[2], args[3][1:-1])
            instance.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
