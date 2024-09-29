from math import sqrt

class Figure:
    sides_count = 0
    def __init__(self, _color, _sides, filled = True):
        self._sides = _sides
        self._color = _color
        self.filled = filled
        #print(self._color)


    def get_color(self):
        #print(self._color)
        return list(self._color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            new_color = (r, g, b)
            self._color =new_color
            return self._color
        else:
            return self._color

    def _is_valid_sides(self, *__sides):
        if len(__sides) == self.sides_count:
            for i in range(len(__sides)):
                if type(i) != int and __sides[i] <= 0:
                    return False
            return True


    def get_sides(self):
        return list(self._sides)

    def __len__(self):
        perim = 0
        if self.sides_count == 1:
            perim = self._sides[0]
            return perim

        elif self.sides_count == 3:
            for i in self._sides:
                perim = perim + i
                return perim
        elif self.sides_count == 12:
            perim = self._sides[1] * 12
            return perim

    def set_sides(self, *new_sides):
        t = self._is_valid_sides(new_sides)
        if t is True:
            self._sides = new_sides


class Circle(Figure):
    sides_count = 1
    def __init__(self, _color, _sides):
        super().__init__(_color, _sides)
        self.__radius = self._sides / (2 * 3.14)

    def get_square(self):
        square = 2 * 3.14 * self.__radius
        return square

class Triangle(Figure):
    sides_count = 3
    def __init__(self, _color, _sides):
        super().__init__(_color, _sides)

    def get_square(self):
        p = super.__len__()
        p2 = p/2
        square = sqrt(p2)
        return square

class Cube(Figure):
    sides_count = 12
    def __init__(self, _color, _sides):
        sides_count = 12
        super().__init__(_color, _sides)

        if type(_sides) == int:
            sl = []
            for x in range(12):
                sl.append(_sides)
                self._sides = sl
        elif len(_sides) == sides_count:
            sl = []
            for x in range(12):
                sl.append(_sides)
                self._sides = sl
        else:
            self._sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_volume(self):
        volume = 0
        volume = self._sides[0] ** 3
        return volume

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











