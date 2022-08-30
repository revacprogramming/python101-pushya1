

# class Menu:
#     """fill in class definition here"""
#      di = dict()
#     def add(self,name,cost):
#         self.di[name]=cost
#     def __add__()
#     def show(self):
#         for every in self.di:
#             print(every,',',self.di[every])



# m = Menu()  # Menu is a class
# m.add("idly", 10)
# m.add("vada", 20)

# m.show()
#===========================================================================================================================================

# class Menu:
#     """fill in class definition here"""



# m = Menu()
# m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

# print(m)  # should print the menu properly

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Menu:
    
    def __init__(self):
        di={}
    def __add__(self,key,value):
        self.di[key]=value
    def __str__(self):
        string = ""
        for k,v in self.di.items():
            string+=f'{k} {v} \n'
        return string




# class Menu:
#     """fill in class definition here"""
#     di = dict()
#     def __add__(self,t):
#         self.di[t[0]]=t[1]
#         return self.di

# m = Menu()
# m = m + ("idly", 10) #+ ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)
# print(m)  # should print the menu properly
