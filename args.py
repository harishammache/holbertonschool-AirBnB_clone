def ma_fonction(*args):#permet de passer un nombre d'arguments à une fonction
    for arg in args:
        print("Argument :", arg)

ma_fonction(1, 2, 3)
ma_fonction('a', 'b', 'c', 'd')
ma_fonction()
