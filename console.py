#!/usr/bin/python3
""" command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd main class """

    prompt = '(hbnb) '  # Setting the custom prompt

    def do_quit(self, arg):
        """ Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """ exit signal Quit command interpretor """
        print("")
        return True
    
    def help_quit(self):
        print("Quit command to exit the program")

            
    def help_EOF(self):
        print("exit signal Quit command interpretor ")

    def emptyline(self):
        """ do nothing if user enter empty line """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
