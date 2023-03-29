from Settings import *

class MsgOthers:
    def __init__(self, surface, message, name):
        self.surface = surface
        self.lines = []
        if len(message) > 45:
            line = []
            for word in message.split():
                line.append(word)
                if len(" ".join(line)) >= 44:
                    line = line[:-1]
                    self.lines.append(" ".join(line))
                    line = [word]
                    i = 1
            self.lines.append(" ".join(line))
        else:
            self.lines.append(message)
        print(self.lines)
        self.rect = pygame.Rect(0, 350 -(20 * len(self.lines)), 300, 50)
        self.name = name
        self.name_aff = font_mid.render(self.name, True, white)
        self.create_message()
        
    def create_message(self):
        self.lines_aff = []
        for line in self.lines:
            self.line = font_small.render("".join(line), True, white)
            self.lines_aff.append(self.line)

    def set_rect_pos(self, offset):
        self.offset += offset
        self.rect = pygame.Rect(300, 400 -(20 * len(self.lines)) - self.offset, 300, 50)

    def render_self(self):
        pygame.draw.rect(self.surface, grey, self.rect)
        self.surface.blit(self.name_aff, (10, self.rect.y))
        y = 0
        for line in self.lines_aff:
            self.surface.blit(line, (self.rect.x + 10, self.rect.y + 20 + y))
            y += 13