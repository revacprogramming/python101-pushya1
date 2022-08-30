

class Menu(dict):
    """fill in class definition here"""
    def __missing__(self,key):
        value = self[key]=type(self)
        return value


class Order(dict):
    """fill in class definition here"""
    


class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
