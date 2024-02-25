#!/usr/bin/python3
import cmd

class Mycommand(cmd.Cmd):
    prompt = "ourcommand >"
    
    def do_quit(self, arg):
        """ This will quit the program!!"""
        return True
    
    # aliasing
    do_exit = do_quit
Mycommand().cmdloop()