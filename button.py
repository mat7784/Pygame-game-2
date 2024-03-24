import pygame as pg


class Button:
    def __init__(self, x, y, width, height, text, font):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.base_color = pg.Color('white')
        self.hover_color = pg.Color('gray')
        self.current_color = self.base_color

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        # Draw the button rectangle
        # pg.draw.rect(screen, (255, 255, 255), self.rect)
        # Draw the button text
        text_surface = self.font.render(self.text, True, self.current_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.base_color

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


