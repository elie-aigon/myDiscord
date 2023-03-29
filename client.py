import socket, pygame
from threading import Thread


def Send(socket):
	while True:
		msg = input(">>>")
		if msg.upper() == "FIN":
			client.close()
			break
		socket.send(msg.encode("utf-8"))

def Recep(socket):
	while True:
		requet = socket.recv(500)
		print( ">" + requet.decode("utf-8"))


HOST = "127.0.0.1"
PORT = 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client.connect((HOST, PORT))
	# print("Connecté au serveur")
except socket.error:
	print("Socket Error")
	sys.exit()

exchange = [Thread(target=Send, args=[client]), Thread(target= Recep, args=[client])]

for i in exchange:
	i.start()

for i in exchange:
	i.join()




client.close()