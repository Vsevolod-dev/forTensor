from math import pi

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
    def square(self):
        p = self.perimeter()/2
        return pow(p*(p - self.a)*(p - self.b)*(p - self.c), 0.5)
        
    def perimeter(self):
        return self.a + self.b + self.c

        
class Quadrate:
    def __init__(self, e):
        self.edge = e

    def square(self):
        return self.edge * 2
        
    def perimeter(self):
        return self.edge * 4
        

class Circle:
    def __init__(self, r):
        self.radius = r
        
    def square(self):
        return self.radius * 2 * pi 
        
    def perimeter(self):
        return self.radius * 2 * pi    
        
        
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.heigh = h
        
    def square(self):
        return self.width * self.heigh
        
    def perimeter(self):
        return self.width*2 + self.heigh*2 


class Sphere(Circle):
    def square(self):
        return 4 * pi * self.radius * 2
        
    def volume(self):
        return (4 / 3) * pi * self.radius * 3

    def perimeter(self):
        print('The sphere has no perimeter')
    
    
class Cube(Quadrate):        
    def square(self):
        return 6 * self.edge * 2
        
    def volume(self):
        return self.edge * 3

    def perimeter(self):
        print('The Cube has no perimeter')


class Parallelepiped:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def square(self):
        return 2 * (self.a*self.b + self.b*self.c + self.a*self.c)
        
    def volume(self):
        return self.a * self.b * self.c
        
s1 = Sphere(5)
print(s1.perimeter())