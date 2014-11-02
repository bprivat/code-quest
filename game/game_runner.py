import pyglet


class GameRunner(pyglet.event.EventDispatcher):

    def __init__(self, dungeon, player):
        self.dungeon = dungeon
        self.player = player
        self.win = pyglet.window.Window()

        self.win.on_key_press = self.on_key_press

    def run(self):
        print("Playing dungeon {} with player {}".format(self.dungeon, self.player))
        pyglet.app.run()
        print("DONE")

    def on_key_press(self, symbol, modifiers):
        self.win.close()
        print("key pressed")

