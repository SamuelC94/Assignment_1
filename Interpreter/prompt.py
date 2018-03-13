from cmd import Cmd
from controller import Controller
from os import path, chdir, getcwd
from re import match


class Shell(Cmd):
    # This will replace the init stuff, all of it will be set in the parent class, access
    # these values using self.intro, self.prompt etc
    intro = "Welcome to our custom Interpreter shell. Type help or ? to list commands.\n"
    prompt = '(Interpreter) '
    file = None
    controller = Controller()
    directory = path.realpath(path.curdir)
    # if the init is defined then super must be used and each item attached to the object, may be better approach
    # because it is more explicit
    # def __init__(self):
    #     super().__init__()
    #     self.controller = Controller()

    # Wesley
    def do_cd(self, line):
        """
        relative traversal through file structure, same as windows
        """
        try:
            line = line.lower()
            start_path = path.realpath(path.relpath(line))
            if self.directory is None and path.isdir(start_path):
                self.directory = start_path
                print(self.directory)
            elif path.isdir(path.realpath(path.relpath(path.join(self.directory, line)))):
                self.directory = path.realpath(path.relpath(path.join(self.directory, line)))
                print(self.directory)
                print("else")
            else:
                print("Not a valid directory")
        except ValueError:
            print("Invalid command")
        except TypeError:
            print("Type of none is invalid")

    def do_load(self, arg):
        """
        syntax: getfile filename
        :param arg: filename
        :return: File has been set
        """
        try:
            self.file = path.realpath(path.join(self.directory, path.relpath(arg)))
            result = self.controller.load(self.file)
            if result:
                self.prompt = '(Interpreter: ' + path.basename(self.file) + ') '
            else:
                print("File does not exist")
        except ValueError:
            print("No path was specified, please try again")

    def do_validate(self, *args):
        """read set file"""
        try:
            self.controller.validate()
        except ValueError:
            print("Invalid file selection")
    # #the_type, filename):

    def do_graph(self, arg):
        commands = arg.split(" ")
        if commands[0] == "pie" or commands[0] == "scatter" or commands[0] == "bar":
            a_path = path.join(self.directory, commands[1] + ".html")
            self.controller.set_graph(commands[0], a_path)
            criteria = input("What are the criteria? > ")
            crit = criteria.split(" ")
            self.controller.set_criteria(crit[0], crit[1])
            keys = input("What keys to use? > ")
            a_key = keys.split(" ")
            self.controller.set_keys(a_key[0], a_key[1])
            x = input("What is the x axis called? >")
            y = input("What is the y axis called? >")
            title = input("What is the title? >")
            self.controller.draw(x, y, title)
        else:
            print("filename is invalid")



    def do_quit(self, arg):
        """
        Syntax: quit
        Quit from my CMD
        :return: True
        """
        print("Quitting ......")
        return True


if __name__ == '__main__':
    Shell().cmdloop()