import socket
import threading, keyboard

threadsClients = []
liste_clients = []
server_live = True
def instanceServeur (client, infosClient):
    liste_clients.append(client)
    adresseIP = infosClient[0]
    port = str(infosClient[1])
    print("Instance de serveur prêt pour " + adresseIP + ":" + port)
    message = ""
    while message.upper() != "FIN":
        if keyboard.is_pressed("esc"):
            break
        message = client.recv(255).decode("utf-8")
        print("Message reçu du client " + adresseIP + ":" + port + " : " + message)
        for i in liste_clients:
            if i != client:
                i.sendall(message.encode("utf-8"))
            
    print("Connexion fermée avec " + adresseIP + ":" + port)
    client.close()

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))
serveur.listen(5)

while server_live:
    if keyboard.is_pressed("esc"):
        break
    client, infosClient = serveur.accept()
    threadsClients.append(threading.Thread(None, instanceServeur, None, (client, infosClient), {}))
    threadsClients[-1].start()
    keyboard.wait()

serveur.close()