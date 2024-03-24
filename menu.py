import pygame as pg
import Settings
from button import Button
from game_state import GameState
from game_play import GamePlay


class MainMenu(GameState):
    def __init__(self, screen, state_manager):
        self.screen = screen
        self.font = pg.font.Font(None, Settings.FONT_SIZE)
        self.buttons = self.create_menu_buttons()
        self.state_manager = state_manager

    def create_menu_buttons(self):
        menu_items = ['Exit', 'Options', 'Start Game']
        buttons = []
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, 'white')
            item_width, item_height = text.get_size()
            x = self.screen.get_width() // 2 - item_width // 2
            y = self.screen.get_height() // 2 - i * (item_height + 50)  # Space between buttons
            button = Button(x, y, item_width, item_height, item, self.font)
            buttons.append(button)
        return buttons

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
            for button in self.buttons:
                if button.is_clicked(event.pos):
                    self.handle_menu_action(button.text)

    def handle_menu_action(self, action):
        if action == 'Start Game':
            if 'GamePlay' not in self.state_manager.states:
                self.state_manager.add_state('GamePlay', GamePlay(self.screen, self.state_manager))
            self.state_manager.change_state('GamePlay')
        elif action == 'Options':
            if 'Options' not in self.state_manager.states:
                self.state_manager.add_state('Options', GamePlay(self.screen, self.state_manager))
            self.state_manager.change_state('Options')
        elif action == 'Exit':
            pg.quit()
            self.state_manager.stop()

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        for button in self.buttons:
            button.update(mouse_pos)

    def draw(self, screen):
        self.screen.fill(Settings.MENU_BG)
        for button in self.buttons:
            button.draw(self.screen)
