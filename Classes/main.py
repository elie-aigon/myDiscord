from Settings import *
from App import App

pygame.init()
date = datetime.datetime.now()
app = App()

def Send(socket, msg):
		socket.send((app.cg.username + "%" + date.strftime('%d') + "/" + date.strftime('%m') + "/" + date.strftime('%Y') + "-" + date.strftime('%H') + ":" + date.strftime('%M') +"%" + msg).encode("utf-8"))

def Recep(socket):
    while True:
        requet = socket.recv(500).decode()
        print(requet)
        if requet != "":
            app.cg.new_msg_others(requet)

PORT = 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client.connect((HOST, PORT))
except socket.error:
	print("Socket Error")
	sys.exit()

exchange = [Thread(target= Recep, args=[client])]

for i in exchange:
	i.start()

while app.state != 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Send(client, "")
            client.close()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in range(31, 126):
                if app.state == 1:
                    app.cg.current_line_input.append(chr(event.key))
            if event.key == pygame.K_RETURN:
                if app.state == 1:
                    Send(client, "".join(app.cg.current_line_input))
                    app.cg.new_msg_self()
            if event.key == pygame.K_BACKSPACE:
                if app.state == 1:
                    app.cg.current_line_input =  app.cg.current_line_input[:-1]
            if event.key == pygame.K_SPACE:
                app.cg.messages_list[0].set_rect_pos(-50)

    app.render()
    pygame.display.update()