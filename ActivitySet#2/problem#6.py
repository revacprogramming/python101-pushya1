

class Menu:
    """fill in class definition here"""
    """fill in class definition here"""
    di = dict()
    def add(self,name,cost):
        self.di[name]=cost
    def show(self):
        for every in self.di:
            print(every,',',self.di[every])



m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
