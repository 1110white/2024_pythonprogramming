from point import Point

class Rectangle:
    
    def __init__(self, lt_x1, lt_y1, rb_x2, rb_y2):
        self.__lt = Point(lt_x, lt_y)
        self.__rb = Point(rb_x, rb_y)
        
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt.toString()}이고', end='')
        print(f'우측 하단 꼭지점이 {self.__rb.toString}인 사각형입니다.')

    def getWidth(self):
        return self._rb.getX() - self.__ltgetX()

    def getHeight(self):
        ltx, lty = self.__lt.get()
        rbx, rby = self.__rb.get()
        return rby - lty

    def getArea(self):
        return self.getWidth() * self.getHeight()
        
    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
