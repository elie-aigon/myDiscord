from Settings import *
from ChatGlobal import ChatGlobal
from FirstScreen import FirstScreen

class App:
    def __init__(self):
        self.state = 0
        
        # database
        self.cnx = mysql.connector.connect(user= 'root', password= "root", 
                                        host='localhost', database= "mydiscord")
        self.curseur = self.cnx.cursor()


        self.root = tk.Tk()
        self.root.title("Ma fenêtre à deux onglets")
        self.root.geometry(str(windowsize[0]) + "x" + str(windowsize[1]))
        self.root.configure(bg=grey_black_hexa)
        notebook = ttk.Notebook(self.root)


        self.connexion = tk.Frame(notebook, bg=grey_black_hexa)
        self.inscription = tk.Frame(notebook, bg=grey_black_hexa)
        self.connexion.configure(bg=grey_black_hexa)
        self.inscription.configure(bg=grey_black_hexa)

        notebook.add(self.connexion, text='Connexion')
        notebook.add(self.inscription, text='Inscription')

        notebook.configure(width=windowsize[0], height=windowsize[1])

        style = ttk.Style()
        style.theme_create('my_theme', parent='alt', settings={
            'TNotebook.Tab': {
                'configure': {'background': grey_white_hexa, 'foreground': 'white'},
                'map': {'background': [('selected', grey_black_hexa)]}
            }
        })
        style.theme_use('my_theme')

        # connexion
        title = tk.Label(self.connexion, text="Se connecter", font=("Arial", 30), background=grey_black_hexa, foreground='white')
        title.pack(pady=20)

        username_aff = tk.Label(self.connexion, text="Username", background=grey_black_hexa, foreground="white")
        self.username_input = tk.Entry(self.connexion)
        username_aff.pack()
        self.username_input.pack()

        pwd_aff = tk.Label(self.connexion, text="Password", background=grey_black_hexa, foreground="white")
        self.pwd_input = tk.Entry(self.connexion, show="*")
        pwd_aff.pack()
        self.pwd_input.pack()

        connect = tk.Button(self.connexion, text="Se connecter", background=grey_white_hexa, foreground="white")

        connect.pack(pady=30)

        # inscription
        title2 = tk.Label(self.inscription, text="Créer un compte", font=("Arial", 30), background=grey_black_hexa, foreground='white')
        title2.pack(pady=20)

        username_aff2 = tk.Label(self.inscription, text="Username", background=grey_black_hexa, foreground="white")
        self.username_input2 = tk.Entry(self.inscription)
        username_aff2.pack()
        self.username_input2.pack()

        pwd_aff2 = tk.Label(self.inscription, text="Password", background=grey_black_hexa, foreground="white")
        self.pwd_input2 = tk.Entry(self.inscription, show="*")
        pwd_aff2.pack()
        self.pwd_input2.pack()

        inscript = tk.Button(self.inscription, text="S'inscrire", background=grey_white_hexa, foreground="white")
        inscript.pack(pady=30)
        notebook.pack(fill= 'both', expand=True)

        connect.configure(command= self.connect_command)
        inscript.configure(command=self.inscript_command)

        self.root.mainloop()

    # First Screen
    def message_box(self, message):
        msg_box = mbox.showinfo(message=message, parent = self.root)

    def connect_command(self):
        self.curseur.execute("SELECT username, password from users;")
        users = self.curseur.fetchall()
        for user in users:
            if self.username_input.get() in user:
                if self.pwd_input.get() == user[1]:

                    self.root.destroy()
                    print(user[0])
                    self.cg = ChatGlobal(user[0])
                    self.state = 1
                    break


    def inscript_command(self):
        if self.username_input2.get() != "" and self.pwd_input2.get() != "":
            self.curseur.execute("INSERT users(username, password, status) VALUES (%s, %s, %s);", (self.username_input2.get(), self.pwd_input2.get(), "noob",))
            self.cnx.commit()
            self.message_box("Vous êtes inscrit, vous pouvez maintenant vous connecter!")
        else:
            self.message_box("Fill all gaps")


    def render(self):
        if self.state == 1:
            self.cg.render_self()