from cmd import Cmd
from controller import Controller
from os import path, chdir, getcwd
from re import match


class CustomShell(Cmd):
    # This will replace the init stuff, all of it will be set in the parent class, access
    # these values using self.intro, self.prompt etc
    intro = "Welcome to our custom Interpreter shell. Type help or ? to list commands.\n"
    prompt = '(Interpreter) '
    file = None
    controller = Controller()
    directory = None
    # if the init is defined then super must be used and each item attached to the object, may be better approach
    # because it is more explicit
    # def __init__(self):
    #     super().__init__()
    #     self.controller = Controller()

    def do_cd(self, line):
        """
        relative traversal through file structure, same as windows
        """
        line = line.lower()
        try:
            if self.directory is None:
                self.directory = path.realpath(path.relpath(line))
                print(self.directory)
            else:
                self.directory = path.realpath(path.relpath(path.join(self.directory, line)))
                print(self.directory)
                print("else")
        except ValueError:
            print("Not a recognised directory")

    def do_setfile(self, arg):
        """
        syntax: getfile filename
        :param arg: filename
        :return: File has been set
        """
        try:
            self.file = path.realpath(path.join(self.directory, path.relpath(arg)))
            self.controller.set_file(self.file)
            print(self.file)
            self.prompt = '(Interpreter: ' + path.basename(self.file) + ') '
        except ValueError:
            print("No path was specified, please try again")

    def do_read(self, arg):
        """read set file"""
        try:
            self.controller.read()
        except ValueError:
            print("Invalid file selection")

    def do_quit(self, arg):
        """
        Syntax: quit
        Quit from my CMD
        :return: True
        """
        print("Quitting ......")
        return True

    def do_load(self, arg):
        """
        Syntax: load
        Load the contents of a file
        :return:
        """
        self.controller.run()


if __name__ == '__main__':
    CustomShell().cmdloop()