from .settings import *

class Button:
    def __init__(self, x, y, width, height, text, text_color=WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        pg.draw.rect(win, self.text_color, (self.x, self.y, self.width, self.height), 2)

        button_font = get_font(22)
        text_surface = button_font.render(self.text, 1, self.text_color)
        win.blit(text_surface, (self.x + self.width /
                                2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, _ = pos

        if (x >= self.x and x <= self.x + self.width):
            return True

        return False