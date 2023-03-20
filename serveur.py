import socket
import select

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.O.O.1", 5000
serveur.bind(host, port)
serveur.listen(4)
client_online = True
socket_obj = [serveur]

print("welcome")
while client_online:
    
	liste_lu, liste_acce_Ecrit, exception = select.select(socket_obj, [], socket_obj)

	for obj in liste_lu:

		if obj is serveur:
			client, adresse = serveur.accept()
			print(f"l'object client socket: {client} - adresse: {adresse}")
			socket_obj.append(client)

		else:
			donnees_recus = obj.recv(128).decode("utf-8")
			if donnees_recus:
				print(donnees_recus)

			else:
				socket_obj.remove(socket_obj)
				print("1 participant est deconnecte")
				print(f"{len(socket_objs) - 1} participants restants")
