from Settings import *
from User import User
class StatusUsers:
    def __init__(self, surface):
        self.surface = surface

        self.pos = (700, 100)

        self.online = font_big.render("Online", True, green)
        self.offline = font_big.render("Offline", True, grey_white)

    def render_self(self):
        self.update_users_list()
        self.surface.blit(self.online, (self.pos[0] - self.online.get_width()//2, self.pos[1]))
        self.surface.blit(self.offline, (self.pos[0] - self.offline.get_width()//2, self.pos[1] + 150))
        y_online = 30
        for user in self.online_users:
            self.name = font_mid.render(user.username, True, green)
            self.surface.blit(self.name, (self.pos[0], self.pos[1] + y_online))
            y_online += self.name.get_height()

        y_offline = 180
        for user in self.offline_users:
            self.name = font_mid.render(user.username, True, grey_white)
            self.surface.blit(self.name, (self.pos[0] - 80, self.pos[1] + y_offline))
            y_offline += self.name.get_height()

    def gen_users_list(self):
        self.online_users = []
        self.offline_users = []
        for user in self.users_list:
            if user.is_online == 1:
                self.online_users.append(user)
            else:
                self.offline_users.append(user)

    def update_users_list(self):
        self.cnx = mysql.connector.connect(user= 'public', password= "root", 
                host=HOST, database= "mydiscord")
        self.curseur = self.cnx.cursor()
        self.curseur.execute("SELECT * FROM users;")
        self.results = self.curseur.fetchall()
        self.users_list = []
        for user in self.results:
            self.users_list.append(User(user[1], user[2], user[3], user[4]))
        self.gen_users_list()