import math


class Circle:
    def __init__(self,radius) :
        self.radius=radius
    def area(self) :
        A=math.pi*(self.r**2)
        return A
    def circumfrence(self):
        C=(2* math.pi,(self.r)) 
        return C 

class Square:
    def __init__(self,A):
        self.A=A
    def area(self) :
        A=(self.A*self.A)
        return A
    def perimeter(self):
        p=4*self.A
        return p
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):    
        a=(self.w*self.l)
        return a
    def per(self):
        p=2*(self.w+self.l) 
        return p   
class Sphere:
    def __init__(self,r):
        self.r=r
    def surface_area(self):
        A=4*math.pi*(self.r*self.r)
        return A
    def volume(self) :
        v=4/3* math.pi*self.r**3
        return v