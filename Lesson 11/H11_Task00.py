# Задача 0
# Реализовать программу подсчета площади, периметра, объема геометрических фигур
# (треугольник, прямоугольник, квадрат, трапеция, окружность).
# Если одна из фигур не поддерживает вычисление одного из свойств,
# в программе должно быть вызвано исключение с человеко-читабельным сообщением и корректно обработано.
import math
import sys


class Triangle:

    def __init__(self, side_a, side_b, side_c):
        # Should make a condition that max side is lower than sum of two other sides
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        p_half = self.perimeter() / 2
        return math.sqrt(p_half * (p_half - self.side_a) * (p_half - self.side_b) * (p_half - self.side_c))


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4

    def square(self):
        return self.side ** 2


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def square(self):
        return self.side_a * self.side_b


class Trapeze:
    def __init__(self, angle_a, angle_b, base_ab, height):
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.base_ab = base_ab
        self.height = height
        self.side_a = self.height / math.sin(self.angle_a)
        self.side_b = self.height / math.sin(self.angle_b)
        self.base = self.base_ab - self.height * (1 / math.tan(self.angle_a) + 1 / math.tan(self.angle_b))

    def perimeter(self):
        return self.base + self.side_a + self.base_ab + self.side_b

    def square(self):
        return (self.base + self.base_ab) * self.height / 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 6.28

    def square(self):
        return (self.radius ** 2) * 3.14


def check_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def create_shape():
    shape_dict = {1: ['Triangle', 3, 'SideA', 'SideB', 'SideC'],
                  2: ['Square', 1, 'Side'],
                  3: ['Rectangle', 2, 'SideA', 'SideB'],
                  4: ['Trapeze', 4, 'AngleA', 'AngleB', 'BaseAB', 'Height'],
                  5: ['Circle', 1, 'Radius']}
    shape_args = []
    while True:
        shape_id = input('Choose shape to create:\n1-Triangle 2-Square 3-Rectangle 4-Trapeze 5-Circle:')
        if shape_id in ('1', '2', '3', '4', '5'):
            # Getting class name(shape) from the dictionary.
            shape = shape_dict.get(int(shape_id))[0]
            # Getting number of arguments(num_of_args) for the shape from the dictionary.
            num_of_args = shape_dict.get(int(shape_id))[1]
            print('Shape to build is {} and number of arguments is {}.'.format(shape, num_of_args))
            break
        else:
            print('Wrong shape id!!!')
    i = 0
    # Filling in the list of arguments(shape_args) for the shape according to number of arguments required.
    while i < num_of_args:
        arg = input('Enter value for {}:'.format(shape_dict.get(int(shape_id))[i + 2]))
        if check_int(arg) and int(arg) > 0:
            shape_args.append(int(arg))
            i += 1
        else:
            print('Wrong Value!!')
    # Checking if it is possible to create shape(relevant for Triangle and Trapeze) using entered parameters.
    if shape == 'Triangle':
        if (sum(shape_args) - max(shape_args)) - max(shape_args) <= 0:
            print('Triangle with such parameters cannot be created!!')
            return False
    elif shape == 'Trapeze':
        if (shape_args[2] - shape_args[3] * (1 / math.tan(shape_args[0]) + 1 / math.tan(shape_args[1]))) <= 0:
            print('Trapeze with such parameters cannot be created!!')
            return False
    # Creating the corresponding instance(shape instance) using class name(shape) and the list of arguments(shape_args).
    print('{} is created using the following parameters: {}'.format(shape, shape_args))
    shape_class = getattr(sys.modules[__name__], shape)
    shape_instance = shape_class(*shape_args)
    return shape_instance


def calculation(shape_inst):
    while True:
        property_to_calc = input('Choose property to calculate:\n1-Perimeter 2-Square 3-Volume:')
        if property_to_calc in ('1', '2', '3'):
            if property_to_calc == '1':
                print('Perimeter:', shape_inst.perimeter())
                break
            elif property_to_calc == '2':
                print('Square:', shape_inst.square())
                break
            else:
                try:
                    print('Volume:', shape_inst.volume())
                    break
                except AttributeError:
                    print('Volume is not supported method!')
        else:
            print('Wrong selection')


def main():
    my_shape = create_shape()
    if my_shape:
        calculation(my_shape)


if __name__ == main():
    main()
