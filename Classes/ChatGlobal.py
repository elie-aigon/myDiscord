from Settings import *
from MsgOthers import MsgOthers
from MsgSelf import MsgSelf

class ChatGlobal:
    def __init__(self, surface):
        self.surface = surface
        # input setup
        self.current_line_input = []
        self.lines_input = []
        # msg setup
        self.messages_list = []
        
        self.laod_ressources()

    def laod_ressources(self):
        self.rect_online = pygame.Rect(600, 0, 200, 500)
        self.rect_input = pygame.Rect(20, 440, 550, 50)


    def render_self(self):
        # loading
        self.current_line_input_aff = font_small.render("".join(self.current_line_input), True, white)
        self.wrap_input_msg()

        # drawing
        self.surface.fill(grey)
        for msg in self.messages_list:
            msg.render_self()
        pygame.draw.rect(self.surface, grey_black, self.rect_online)
        pygame.draw.rect(self.surface, grey_white, self.rect_input, border_radius=20)

        if len(self.lines_input) > 0:
            y = 0
            for line in self.lines_input:
                self.line_aff = font_small.render("".join(line), True, white)
                self.surface.blit(self.line_aff, (self.rect_input.x + 15, self.rect_input.y + 25 - (self.line_aff.get_height()//2) + y))
                y += 30
        
        self.surface.blit(self.current_line_input_aff, (self.rect_input.x + 15, 465 - self.current_line_input_aff.get_height()//2 - 3))
    
    def wrap_input_msg(self):
        if self.current_line_input_aff.get_width() >= self.rect_input.width - 40:
            self.rect_input.y -= 30
            self.rect_input.height += 30
            self.lines_input.append(self.current_line_input)
            self.current_line_input = []

    def reset_input_text(self):
        self.current_line_input = []
        self.lines_input = []
        
    def new_msg_self(self):
        if self.current_line_input != []:
            self.lines_input.append(self.current_line_input)
            self.msg_string = ""
            for element in self.lines_input:
                self.msg_string = self.msg_string + "".join(element)
            if len(self.messages_list) > 0:
                for i, msg in enumerate(self.messages_list):
                    msg.set_rect_pos(50)
            self.messages_list.append(MsgSelf(self.surface, self.msg_string, "elie"))
            self.reset_input_text()
