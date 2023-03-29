import socket, keyboard
from threading import Thread
import select

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "localhost", 50000
serveur.bind((host, port))
serveur.listen(4)
clients_online = True
socket_obj = [serveur]

print("Bienvenue dans le chat!!")

while clients_online:
	if keyboard.read_key() == "a":
		clients_online = False
	liste_read, liste_write, exception = select.select(socket_obj, [], socket_obj)

	for obj in liste_read:
		if obj is serveur:
			client, adresse = serveur.accept()
			print(f"l'object client socket:- adresse: {adresse}")
			socket_obj.append(client)
			print(socket_obj)

		else:
			datas = obj.recv(128).decode("utf-8")
			if datas:
				for x in socket_obj:
					if x != obj:
						x.send(datas.encode("utf-8"))
				

			else:
				socket_obj.remove(obj)
				print("1 participant est deconnecte")
				print(f"{len(socket_obj) - 1} participants restants")
