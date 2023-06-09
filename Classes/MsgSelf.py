from Settings import *

class MsgSelf:
    def __init__(self, surface, message, name):
        self.surface = surface
        self.lines = []
        self.offset = 0
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
        self.date = datetime.datetime.now()
        self.time = font_time.render(self.date.strftime('%d') + "/" + self.date.strftime('%m') + "/" + self.date.strftime('%Y') + "-" + self.date.strftime('%H') + ":" + self.date.strftime('%M'), True, white)
        self.set_rect_pos(self.offset)
        self.name = name
        self.name_aff = font_mid.render(self.name, True, white)
        self.create_message()

    def set_rect_pos(self, offset):
        self.offset += offset
        self.rect = pygame.Rect(300, 400 -(20 * len(self.lines)) - self.offset, 300, 50)

    def create_message(self):
        self.lines_aff = []
        for line in self.lines:
            self.line = font_small.render("".join(line), True, white)
            self.lines_aff.append(self.line)

    def render_self(self):
        pygame.draw.rect(self.surface, grey, self.rect)
        self.surface.blit(self.name_aff, (self.rect.x + self.rect.width - self.name_aff.get_width() - 10, self.rect.y))
        y = 0
        for line in self.lines_aff:
            self.surface.blit(line, (self.rect.x + self.rect.width - line.get_width(), self.rect.y + 20 + y))
            y += 13
        self.surface.blit(self.time, (self.rect.x + self.rect.width - self.name_aff.get_width() - self.time.get_width() - 15, self.rect.y + 3))
