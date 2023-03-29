from Settings import *
from App import App

# client_online = True
# def Send(socket):
# 	while client_online:
# 		msg = input(">>>")
# 		if msg.upper() == "FIN":
# 			client.close()
# 			break
# 		socket.send(msg.encode("utf-8"))

# def Recep(socket):
# 	while client_online:
# 		requet = socket.recv(500)
# 		print( ">" + requet.decode("utf-8"))


# adresseIP = "127.0.0.1"
# port = 50000
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try:
# 	client.connect((adresseIP, port))
# 	print("Connecté au serveur")
# except socket.error:
# 	print("Socket Error")
# 	sys.exit()

# exchange = [Thread(target=Send, args=[client]), Thread(target= Recep, args=[client])]

# for i in exchange:
# 	i.start()

pygame.init()

app = App()

while app.state != 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # client_online = False
        if event.type == pygame.KEYDOWN:
            if event.key in range(31, 126):
                if app.state == 1:
                    app.cg.current_line_input.append(chr(event.key))
            if event.key == pygame.K_RETURN:
                if app.state == 1:
                    app.cg.new_msg_self()
                    # client_online = False
            if event.key == pygame.K_BACKSPACE:
                if app.state == 1:
                    app.cg.current_line_input =  app.cg.current_line_input[:-1]
            if event.key == pygame.K_SPACE:
                app.cg.messages_list[0].set_rect_pos(-50)

    app.render()
    pygame.display.update()
