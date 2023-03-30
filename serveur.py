HOST = '127.0.0.1'
PORT = 50000

import socket, sys, threading
 
class ThreadClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):

        nom = self.name
        while 1:
            try:
                msgClient = self.connexion.recv(1024).decode()
            except :
                print('Disconnect')
                break
            if msgClient.upper() == "FIN" or msgClient =="":
                break

            msg = (nom + "%" + msgClient)
            print(msg)
            for cle in conn_client:
                if cle != nom:
                    conn_client[cle].send(msg.encode())
                    

        self.connexion.close()
        del conn_client[nom]
        print ("Client %s déconnecté." % nom)


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print ("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

conn_client = {}
while 1:    
    connexion, adresse = mySocket.accept()

    th = ThreadClient(connexion)
    th.start()

    it = th.name
    conn_client[it] = connexion
    print ("Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1]))

    connexion.send("Serveur % Vous êtes connecté. Envoyez vos messages.".encode())