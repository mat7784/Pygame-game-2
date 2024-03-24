class StateManager:
    def __init__(self):
        self.states = {}
        self.active_state = None
        self.running = True

    def add_state(self, name, state):
        self.states[name] = state

    def change_state(self, name):
        self.active_state = self.states.get(name)

    def update(self):
        if self.active_state:
            self.active_state.update()

    def draw(self, screen):
        if self.active_state:
            self.active_state.draw(screen)

    def handle_event(self, event):
        if self.active_state:
            self.active_state.handle_event(event)

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running
