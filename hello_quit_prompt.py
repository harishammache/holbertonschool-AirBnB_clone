import cmd

class MonShell(cmd.Cmd):#appelle la bibliothèque cmd afin de creer facilement des interfaces en ligne de commande interactive
    """Interface en ligne de commande personnalisée"""

    prompt = "SHELL Jeremy Haris> "

    def do_hello(self, arg):#lorsque l'utilisateur entre dans le programme et affiche "hello", Bonjour, s'affiche
        """Affiche un message de salutation."""
        print("Bonjour,", arg)

    def do_quit(self, arg):#lorsque l'utilisateur quitte le programme avec "quit", Au revoir s'affiche
        """Quitter le programme."""
        print("Au revoir !")
        return True

if __name__ == "__main__":
    MonShell().cmdloop() #boucle qui attend les commandes de l'utilisateur et les execute en appelant les méthode approprié
