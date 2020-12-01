import uuid
from simple_logger import logger


class Supply:
    def __init__(self, item, supplier, amount):
        self.id = uuid.uuid4()
        self.item = item
        self.supplier = supplier
        self.amount = amount
        self.log = logger
        self.log.info(f"Supply is done")

    def __str__(self):
        return f"{self.id}: {self.item} by {self.supplier}"

    def __repr__(self):
        return f"{self.id}: {self.amount} {self.item.title} by {self.supplier.company_name}"


if __name__ == '__main__':
    from supplier import Supplier
    from item import Item
    supplier1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                         "000-112-35-8", "crab@shack.biz")
    item1 = Item("Banana", "Better than ever before", 799.0,
                 ("Golden", "Fresh Green"))
    supplier1.add_supply(item1, 10)
