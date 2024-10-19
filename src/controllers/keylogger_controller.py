class KeyloggerController:
    """Controller to manage the keylogger."""
    def __init__(self, model):
        self.model = model

    def run(self):
        self.model.start()
