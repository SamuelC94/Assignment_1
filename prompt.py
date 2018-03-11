from cmd import Cmd
from filehandler import run
from os import system


class Shell(Cmd):

    """
    single command processor example
    """
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    @staticmethod
    def do_quit(arg):
        """
        Syntax: quit
        Quit from my CMD
        :return: True
        """
        print("Quitting ......")
        return True

    do_q = do_quit

    @staticmethod
    def do_load(arg):
        """
        Syntax: load
        Load the contents of a file
        :return:
        """
        run()

    @staticmethod
    def do_clear(arg):
        """
        Syntax: clear
        Clear the contents of the terminal
        :return:
        """
        system('cls')

    # Sam
    @staticmethod
    def do_draw(arg):
        """
        Syntax: draw [graph name]
        :param graph_type:
        :return:
        """
        # DB handler method invoke

if __name__ == "__main__":
    prompt = Shell()
    prompt.cmdloop()
