class Electronic:
    def __init__(self, name):
        self._name = name
        self._turned_on = False

    def turn_on(self):
        if not self._turned_on:
            self._turned_on = True

    def turn_of(self):
        if not self._turned_on:
            self._turned_on = False


class Smartphone(Electronic):
    ...


