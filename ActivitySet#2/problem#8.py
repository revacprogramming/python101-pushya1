
class Menu(dict):
    
    def __missing__(self,key):
        value = self[key]=type(self)
        return value
    
    


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)