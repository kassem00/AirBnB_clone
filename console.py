#!/usr/bin/python3
""" command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd main class """

    def do_quit(self, arg):
        """ quit function """
        return True
    
    def do_EOF(self, arg):
        """ quit function """
        print("")
        return True
    
    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """ do nothing if user enter empty line """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
