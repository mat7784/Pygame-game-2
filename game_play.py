import pygame as pg
import Settings
from button import Button
from game_state import GameState
from BG_manager import BackgroundManager


class GamePlay(GameState):
    def __init__(self, screen, state_manager):
        # Initialize the gameplay state
        self.screen = screen
        self.font = pg.font.Font(None, Settings.FONT_SIZE)
        self.state_manager = state_manager
        self.background_manager = BackgroundManager()
        self.background_manager.set_color(Settings.PLAY_BG)
        self.pause_button = Button(Settings.size[0] - Settings.Button_sizeX - 40, 10, Settings.Button_sizeX, Settings.Button_sizeY, 'Pause', self.font)

    def update(self):
        # Update game logic
        self.pause_button.update(pg.mouse.get_pos())

    def draw(self, screen):
        self.background_manager.draw(screen)
        self.pause_button.draw(screen)

    def handle_event(self, event):
        # Handle player input specific to the gameplay
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.pause_button.is_clicked(event.pos):
                if 'PauseMenu' not in self.state_manager.states:
                    self.state_manager.add_state('PauseMenu', GamePlay(self.screen, self.state_manager))
                self.state_manager.change_state('PauseMenu')
