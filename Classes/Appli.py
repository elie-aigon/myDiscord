from Settings import *
from ChatGlobal import ChatGlobal

class Appli:
    def __init__(self, surface):
        self.surface = surface
        self.state = 1
        # state
        # 0 = login screen
        # 1 = chat screen
        # 2 = priv  chat screen
        self.cg = ChatGlobal(self.surface)

    def render(self):
        self.cg.render_self()
