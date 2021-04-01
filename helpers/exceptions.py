class UserNotFoundException(Exception):

    def __init__(self, message):
        self.message = message


class ItemAlreadyExistInCart(Exception):

    def __init__(self, message):
        self.message = message
