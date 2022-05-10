import turtle

class polygon:
    def __init__(self):
        pass
    def Square(self,side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)
        
    def pent(self,side):
        for k in range(5):
            turtle.forward(side)
            turtle.left(72)

    def hex(self,side):
        for w in range(6):
            turtle.forward(side)
            turtle.left(60)
        
    def hept(self,side):
        for j in range(7):
            turtle.forward(side)
            turtle.right(51.43)
    
    def oct(self,side):
        for j in range(8):
            turtle.forward(side)
            turtle.right(45)
        
    def non(self,side):
        for j in range(9):
            turtle.forward(side)
            turtle.right(40)

    def dec(self,side):
         for p in range(10):
            turtle.forward(side)
            turtle.right(36)
    
    def hendec(self,side):
        for p in range(11):
            turtle.forward(side)
            turtle.right(32.73)
    
    def Dodec(self,side):
        for p in range(12):
            turtle.forward(side)
            turtle.right(30)
            
class triangle:
    def __init__(self):
        pass
    def equlatiral(self,side):
        for i in range(3):
            turtle.forward(side)
            turtle.left(120 )
    def right_angle(self,side1,side2):
        turtle.forward(side1)
        turtle.left(135)
        turtle.forward(((side1**2)+(side2**2))**0.5)
        turtle.left(135)
        turtle.forward(side2)
            
SHAPE = triangle()

SHAPE.right_angle(200,300)
