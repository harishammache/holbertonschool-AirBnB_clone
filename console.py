#!/usr/bin/python3
"""Module for HBNBCommand(cmd.Cmd)"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
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
        """Create an instance of the specified class, save it to the JSON file,
        and print the id."""
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
        instance based on the class name and id.

        Args:
            arg (str): The string containing the class name and
            id separated by a space.

        Prints an error message if the class name is missing,
        if the class doesn't exist,
        if the instance ID is missing,
        or if no instance is found with the given ID.
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
        Deletes an instance based on the class name and id and
        saves the change into the JSON file.

        Args:
            arg (str): The string containing the class name and
            id separated by a space.

        Prints an error message if the class name is missing,
        if the class doesn't exist,
        if the instance ID is missing,
        or if no instance is found with the given ID.
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

    def do_update(self, arg):
        """
        Updates an instance's attribute based on the class name and id.
        This update will also persist to the JSON file used for storage.

        Args:
            arg (str): A string that should include the class name,
            instance id, attribute name,
            and the new value for the attribute, all separated by spaces.

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        This method will print an error message if:
        - The class name is missing.
        - The provided class name does not exist.
        - The instance ID is missing.
        - No instance with the given ID was found.
        - The attribute name is missing.
        - The value for the attribute is missing.

        Note:
        - 'id', 'created_at', and 'updated_at' attributes cannot be updated.
        - Only string, integer, and float attribute types are
        supported for update.
        """
        list_arg = arg.split()
        obj = storage.all()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        elif len(list_arg) < 3:
            print("** attribute name missing **")
        elif not len(list_arg) < 4:
            print("** value missing **")
        else:
            class_name = list_arg[0]
            instance_id = list_arg[1]
            attribute_name = list_arg[2]
            attribute_value = str(list_arg[3])
            key = f"{class_name}.{instance_id}"
            if key not in obj:
                print("** no instance found **")
            else:
                setattr(obj[key], attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
