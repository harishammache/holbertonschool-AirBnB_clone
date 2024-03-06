def ma_fonction(**kwargs): #permet de passer un nombre variable d'arguments nommés(clé-valeur)
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

ma_fonction(nom='John', age=30)
ma_fonction(prenom='Alice', ville='Paris', pays='France')
ma_fonction()
