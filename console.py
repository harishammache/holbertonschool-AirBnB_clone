#!/usr/bin/python3
"""Module for HBNBCommand(cmd.Cmd)"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """class HBNBcommand inherit cmd"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create an instances of the specified class,
        save it to the JSON file, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg not in globals():
                print("** class doesn't exist **")
                return
            obj = globals()[arg]()
            obj.save()
            print(obj.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an
        instances based on the class name and id.

        Args:
            arg (str): The string containing the class name and
            id separated by a space.

        Prints an error message if the class name is missing,
        if the class doesn't exist,
        if the instances ID is missing,
        or if no instances is found with the given ID.
        """
        list_arg = arg.split()
        obj = storage.all()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = list_arg[0], list_arg[1]
            if "{}.{}".format(class_name, instance_id) not in obj:
                print("** no instance found **")
            else:
                print(obj["{}.{}".format(class_name, instance_id)])

    def do_destroy(self, arg):
        """
        Deletes an instances based on the class name and id and
        saves the change into the JSON file.

        Args:
            arg (str): The string containing the class name and
            id separated by a space.

        Prints an error message if the class name is missing,
        if the class doesn't exist,
        if the instances ID is missing,
        or if no instances is found with the given ID.
        """
        list_arg = arg.split()
        obj = storage.all()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = list_arg[0], list_arg[1]
            if "{}.{}".format(class_name, instance_id) not in obj:
                print("** no instance found **")
            else:
                del obj["{}.{}".format(class_name, instance_id)]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of instances stored,
        optionally filtered by class name.

        This command supports printing all stored instances,
        or filtering them to only print instances
        of a specific class. The output is formatted as a list of strings
        where each string is the
        string representation of an instance.

        Args:
            arg (str): A string containing the class name whose
            instances are to be printed.
            This argument is optional;
            if omitted, instances of all classes will be printed.

        Usage:
            - To print all instances: `all`
            - To print instances of a specific class: `all ClassName`

        If a class name is provided and it doesn't exist,
        an error message is printed.
        """
        obj = storage.all()
        if arg:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            else:
                instances = [str(obj) for obj in obj.values() if
                             type(obj).__name__ == args[0]]
        else:
            instances = [str(obj) for obj in obj.values()]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instances's attribute based on the class name and id.
        This update will also persist to the JSON file used for storage.

        Args:
            arg (str): A string that should include the class name,
            instances id, attribute name,
            and the new value for the attribute, all separated by spaces.

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        This method will print an error message if:
        - The class name is missing.
        - The provided class name does not exist.
        - The instances ID is missing.
        - No instances with the given ID was found.
        - The attribute name is missing.
        - The value for the attribute is missing.

        Note:
        - 'id', 'created_at', and 'updated_at' attributes cannot be updated.
        - Only string, integer, and float attribute types are
        supported for update.
        """
        list_arg = shlex.split(arg)
        obj = storage.all()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            class_name = list_arg[0]
            instance_id = list_arg[1]
            key = f"{class_name}.{instance_id}"
            if key not in obj:
                print("** no instance found **")
            elif len(list_arg) < 3:
                print("** attribute name missing **")
            elif len(list_arg) < 4:
                print("** value missing **")
            else:
                attribute_name = list_arg[2]
                attribute_value = list_arg[3]
                if attribute_name not in ['id', 'created_at', 'updated_at']:
                    if hasattr(obj[key], attribute_name):
                        existing_type = type(getattr(obj[key], attribute_name))
                        if existing_type in [int, float, str]:
                            attribute_value = existing_type(attribute_value)
                setattr(obj[key], attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
