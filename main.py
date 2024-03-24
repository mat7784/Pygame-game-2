import pygame as pg
from menu import MainMenu
import Settings
from state_manager import StateManager


# Game Loop and State Management
def main():
    pg.init()
    screen = pg.display.set_mode(Settings.size)
    state_manager = StateManager()
    state_manager.add_state('MainMenu', MainMenu(screen, state_manager))
    state_manager.change_state('MainMenu')
    clock = pg.time.Clock()

    while state_manager.is_running():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                state_manager.stop()
            else:
                state_manager.handle_event(event)
        if state_manager.is_running():
            state_manager.update()
            state_manager.draw(screen)
            pg.display.flip()
            clock.tick(60)
        # print(state_manager.active_state)
    pg.quit()


if __name__ == "__main__":
    main()
