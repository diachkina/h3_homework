import uuid
from user import User
from simple_logger import logger
from order import Order
from customer import Customer
from item import Item
from review import Review


class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.log = logger
        self.log.info(f'Admin ok')

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)
            self.log.info(f'Admin updated supply')

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)
            self.log.info(f'Admin updated orders')

    def check_order(self, order):
        # print(f"Checking order {order.id}")
        self.log.info(f'Admin is checking orders')
        if not order.status == 'New':
            self.log.info(f"Admin say 'new order'")
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                self.log.info(f"Admin say 'order is confirmed'")
                return order
        order.status = 'On hold'
        self.log.info(f"Admin say 'order on hold'")
        return order

    def check_review(self, review):
        self.log.info(f'Admin is checking review')
        if review.mark >= 4:
            review.status = "Published"
            self.log.info(f"Admin say 'review is published'")
            return review
        review.status = "Moderation"
        self.log.info(f"Admin say 'review is bad. Delete it!'")
        return review


admin1 = Administrator("iamgod", "iamthelaw", "memyself@heavens.com")
c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum",
              "000-112-35-8", "guido@python.org", "09-09-1968")
item1 = Item("Banana", "Better than ever before", 799.0,
             ("Golden", "Fresh Green"))
o1 = Order(customer=c1, item=item1, amount=1)
r1 = Review('Guido', 'Bananas are yummy', 3)
admin1.check_order(o1)
admin1.check_review(r1)
