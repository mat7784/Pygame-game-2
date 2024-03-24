import pygame as pg


class BackgroundManager:
    def __init__(self):
        self.color = (0, 0, 0)  # Default background color, black
        self.image = None  # For background image, None if using color

    def set_color(self, color):
        self.color = color
        self.image = None

    def set_image(self, image_path):
        self.image = pg.image.load(image_path)

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (0, 0))
        else:
            screen.fill(self.color)
