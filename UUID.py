import uuid

uuid_random = uuid.uuid4() #permet de creer un UUID aléatoire en format uuid.UUID
uuid_str = str(uuid_random) #transforme le type de UUID en str
print("UUID aléatoire (version 4) :", uuid_str) #affiche le UUID
print("UUID aléatoire (version 4) :", type(uuid_str)) #affiche le type de UUID
