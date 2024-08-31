from project.tools.validation import *
class Cloth:
    def __init__(self, id, name, size, price, quantity):
        self.id = id
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Cloth(id={self.id}, name='{self.name}', size='{self.size}', price={self.price}, quantity={self.quantity})"

    def update_quantity(self, new_quantity):
        try:
            if new_quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            self.quantity = new_quantity
        except ValueError as e:
            return str(e)

    def update_price(self, new_price):
        try:
            if new_price < 0:
                raise ValueError("Price cannot be negative.")
            self.price = new_price
        except ValueError as e:
            return str(e)

    def view(self):
        try:
            return f"ID: {self.id}, Name: {self.name}, Size: {self.size}, Price: {self.price}, Quantity: {self.quantity}"
        except Exception as e:
            return f"Error viewing cloth details: {str(e)}"

    def buy(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount to buy must be greater than zero.")
            if amount > self.quantity:
                raise ValueError("Not enough stock available.")
            self.quantity -= amount
            return f"{amount} units of {self.name} bought. Remaining quantity: {self.quantity}"
        except ValueError as e:
            return str(e)

    def remove(self):
        try:
            self.quantity = 0
            return f"{self.name} has been removed from stock."
        except Exception as e:
            return f"Error removing cloth: {str(e)}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name_validator(name)

    @property
    def quantity(self):
        return self._quantity()

    @quantity.setter
    def quantity(self, quantity):
        self._name = quantity_validator(quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price_validator(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size_validator(size)


