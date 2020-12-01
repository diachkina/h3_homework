import uuid
from simple_logger import logger


class Review:
    def __init__(self, customer, text, mark):
        self.id = uuid.uuid4()
        self.text = text
        self.customer = customer
        self.mark = mark
        self.status = "Moderation"
        self.log = logger
        self.log.info(f'Review ok')

    def __str__(self):
        return f"Your review ({self.text}). " \
               f"It's status is '{self.status}', mark {self.mark}."

    def __repr__(self):
        return f"{self.text}"


if __name__ == '__main__':
    from customer import Customer

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                  "guido@python.org", "09-09-1968")
    r1 = Review(customer=c1, text='Bananas are yummy', mark=5)
