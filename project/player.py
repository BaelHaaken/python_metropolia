class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            return item

        return None

    def clear_items(self):
        self.items.clear()