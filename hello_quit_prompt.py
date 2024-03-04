import cmd

class MonShell(cmd.Cmd):
    """Interface en ligne de commande personnalisée"""

    prompt = "SHELL Jeremy Haris> "

    def do_hello(self, arg):
        """Affiche un message de salutation."""
        print("Bonjour,", arg)

    def do_quit(self, arg):
        """Quitter le programme."""
        print("Au revoir !")
        return True

if __name__ == "__main__":
    MonShell().cmdloop()
