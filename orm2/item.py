import uuid
from simple_logger import logger


class Item:
    def __init__(self, title, description, price, colors=("Black", )):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.price = float(price)
        self.colors = colors
        self.log = logger
        self.log.info(f'Item is ready')

    def __str__(self):
        return f"Item {self.id}: {self.title}, ${self.price}"

    def __repr__(self):
        return f"Item {self.id}: {self.title}"


if __name__ == '__main__':
    i1 = Item("Banana", "Better than ever before", 799.0, ("Golden", "Fresh Green"))
