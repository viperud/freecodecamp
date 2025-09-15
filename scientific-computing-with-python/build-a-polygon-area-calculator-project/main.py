class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        output = (f'{self.__class__.__name__}')
        match self.__class__.__name__:
            case "Rectangle":
                output += (f'(width={self.width}, height={self.height})')
            case "Square":
                output += (f'(side={self.width})')
        return output

    def set_width(self, width):
        if isinstance(self, Square):
            self.height = width
        self.width = width

    def set_height(self, height):
        if isinstance(self, Square):
            self.width = height
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        output = ''
        for i in range(self.height):
            for j in range(self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, obj):
        if self.height < obj.height or self.width < obj.width:
            return 0
        x = int(self.height / obj.height)
        y = int(self.width / obj.width)
        return x * y


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

#Usage example
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(f'\n{"":*^24}')
#Test case 4
rect = Rectangle(3, 6)
print(rect)
#Test case 5
sq = Square(5)
print(sq)
#Test case 6
print(rect.get_area())
#Test case 7
print(sq.get_area())
#Test case 8
print(rect.get_perimeter())
#Test case 9
print(sq.get_perimeter())
#Test case 10
print(rect.get_diagonal())
#Test case 11
print(sq.get_diagonal())
#Test case 17
sq1 = Square(51)
print(sq1.get_picture())
#Test case 18
rect1 = Rectangle(15, 10)
print(rect1.get_amount_inside(sq))
#Test case 19
rect1 = Rectangle(4, 8)
print(rect1.get_amount_inside(rect))
#Test case 20
rect1 = Rectangle(2, 3)
print(rect1.get_amount_inside(rect))
print(f'{"":*^24}')