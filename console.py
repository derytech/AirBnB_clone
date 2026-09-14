#!/usr/bin/python3
"""Defines the command interpreter for the AirBnB clone."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def precmd(self, line):
        """Remove unnecessary spaces before processing a command."""
        return line.strip()

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        obj = self.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances or instances of a specific class."""
        args = shlex.split(arg)
        objects = storage.all()

        if args:
            class_name = args[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            print([
                str(obj)
                for obj in objects.values()
                if obj.__class__.__name__ == class_name
            ])
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Update an instance with a new attribute value."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        obj = objects[key]

        if hasattr(obj, attribute_name):
            attribute_type = type(getattr(obj, attribute_name))

            if attribute_type is int:
                attribute_value = int(attribute_value)
            elif attribute_type is float:
                attribute_value = float(attribute_value)
            elif attribute_type is str:
                attribute_value = str(attribute_value)

        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
