class rectangle:
    sides = 4
    corners = 4

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Modify(self):
       length = int(input('What is the length of your rectangle?'))
       self.length = length
       width = int(input('What is the width of your rectangle?'))
       self.width = width

    def clac_area(self):
        area = self.length*self.width
        print(f'the area of your rectangle is {area} cm sqr')

rect1 = rectangle(1,2)

rect1.Modify()
rect1.clac_area()

/


class circle:

    
    def __init__(self, radius):
        self.radius = radius

    def Modify(self):
        radius = int(input('What is the radius of your circle?'))
        self.radius = radius

    def clac_circarea(self):
        pi = 22/7
        area = pi*self.radius**2
        circ = pi*self.radius*2

        print(f'the circumference of your circle is {circ} cm and the area of your circle is {area} cm sqr ')

circle1 = circle(21)

circle1.Modify()
circle1.clac_circarea()


