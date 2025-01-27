class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, rgb, *side):
        self.__color = list(rgb)
        self.side = side[0]
        self.filled = True

        if len(side) == self.sides_count:
            self.__sides = [*side]
        else:
            for i in range(0, self.sides_count):
                self.__sides.append(1)

    def __len__(self):
        return self.get_sides()[0] * self.sides_count


    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_color(self, r, g, b):
        rgb_color = [r, g, b]
        for i in rgb_color:
            if i < 0 or i > 255:
                return False
        return True

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                    if not isinstance(i, int) or not i > 1:
                        return False
                    else:
                        return True
        else:
            return False



    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = [*new_sides]


    def get_sides(self):
        return self.__sides

class Circle(Figure):
    sides_count = 1
    __radius = None

    def __len__(self):
        p = 0
        for i in self.get_sides():
            p = p + i

        return p

    def set_radius(self):
        self.__radius = self.get_sides()[0] / 2

    def get_square(self):
        self.set_radius()
        square = 3.14 * (self.__radius**2)
        return square

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]

        p = 0.5 * (a + b + c)
        square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, side):
        self.side_one = side
        self.sides = []
        for i in range(0, self.sides_count):
            self.sides.append(self.side_one)
        super().__init__(rgb, *self.sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


