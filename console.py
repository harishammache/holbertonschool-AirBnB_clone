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
        Prints the string representation of an instance based on the class name and id.
    
        Args:
            arg (str): The string containing the class name and id separated by a space.
        
        Prints an error message if the class name is missing, if the class doesn't exist,
        if the instance ID is missing, or if no instance is found with the given ID.
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
        list_arg = arg.split()
        obj = storage.all()
        if not list_arg:
            print("** class name missing **")
        elif list_arg[0]




if __name__ == '__main__':
    HBNBCommand().cmdloop()
