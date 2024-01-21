#!/usr/bin/python3
""" command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd main class """

    def do_quit(self, line):
        """ quit function"""
        return True
    
    def do_EOF(self, line):
        """ quit function"""
        return True
    def help_quit(self):
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
