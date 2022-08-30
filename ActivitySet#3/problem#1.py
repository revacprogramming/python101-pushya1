#takes the co-ordiantes to a traingle
def input_of_triangle():
    n=int(input("Enter the no.of triangle you want enter"))
    li=[]
    for i in range(n):
        co_ord=input("Enter the 3 coordinates of the rectangle")
        l=co_ord.split()
        li.append(l)
    return li
#to find distance
from math import sqrt
def distance_(x1,y1,x2,y2):
    d=sqrt(((x2-x1)**2)+((y2-y1)**2))
    return d
#finds the area of the triangle
def area_of_triangle(li):
    areas=[]
    for i in li:
        d1=distance_(float(i[0]),float(i[1]),float(i[2]),float(i[3]))
        d2=distance_(float(i[0]),float(i[1]),float(i[4]),float(i[5]))
        area=d1*d2
        areas.append(area)
    return areas
#gives the list of areas of the triangle
def triangle_areas():
    
    li=input_of_triangle()
    
    areas=area_of_triangle(li)
    
    print(areas)
    return areas

triangle_areas() 