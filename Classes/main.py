from Settings import *
from Appli import Appli

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


adresseIP = "127.0.0.1"
port = 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client.connect((adresseIP, port))
	print("Connecté au serveur")
except socket.error:
	print("Socket Error")
	sys.exit()

exchange = [Thread(target=Send, args=[client]), Thread(target= Recep, args=[client])]

for i in exchange:
	i.start()

pygame.init()

screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption("My Discord")

appli = Appli(screen)((((()))))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in range(31, 126):
                if appli.state == 1:
                    appli.cg.current_line_input.append(chr(event.key))
            if event.key == pygame.K_RETURN:
                if appli.state == 1:
                    appli.cg.new_msg_self()
            if event.key == pygame.K_BACKSPACE:
                if appli.state == 1:
                    appli.cg.current_line_input =  appli.cg.current_line_input[:-1]
            if event.key == pygame.K_SPACE:
                appli.cg.messages_list[0].set_rect_pos(-50)

    appli.render()
    pygame.display.update()

for i in exchange:
	i.join()

client.close()