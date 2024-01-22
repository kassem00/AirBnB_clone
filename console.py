#!/usr/bin/python3
""" command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ cmd main class """
    all_class_name = ["BaseModel"]
    prompt = '(hbnb) '  # Setting the custom prompt
    def do_quit(self, arg):
        """ Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """ exit signal Quit command interpretor """
        print("")
        return True

    def do_create(self, arg:str):#done
        """ create: Creates a new instance of BaseModel """
        cl = HBNBCommand.all_class_name
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in cl:
            print("** class doesn't exist **")
        else:
            cl_id = eval(arg)().id
            print(cl_id)
            storage.save()

    def do_show(self, arg:str, arg2:str):# we stop here don't make help function 
        """ Prints the string representation of an instance based on the class name and id """
        cl = HBNBCommand.all_class_name
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in cl:
            print("** class doesn't exist **")
        else:
            cl_id = eval(arg)().id
            print(cl_id)
            storage.save()
            
    def emptyline(self):
        """ do nothing if user enter empty line """
        pass

    def help_quit(self):
        print("Quit command to exit the program")

            
    def help_EOF(self):
        print("exit signal Quit command interpretor ")

    def help_create(self):
        print("\
        create: Creates a new instance of BaseModel,\n\
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel\n\
        If the class name is missing, print ** class name missing ** (ex: $ create)\n\
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)\
        ")        

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
