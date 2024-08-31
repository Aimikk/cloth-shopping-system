
import re

def name_validator(name):
    if type(name) == str and bool(re.match(r"^[\sa-zA-Z]{2,30}$", name)):
        return name
    else:
        raise ValueError("Invalid Name !")

def price_validator(price):
    if type(price) == int and price > 0:
        return price
    else:
        raise ValueError("Invalid Price !")

def quantity_validator(quantity):
    if type(quantity) == int and str and quantity >= 0 :
        return quantity
    else:
        raise ValueError("Invalid Count !")



def size_validator(size):
    if type(size) == float and size > 0 :
        return size
    else:
        raise ValueError("Invalid Size !")