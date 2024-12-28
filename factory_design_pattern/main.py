from abc import abstractmethod, ABC
from functools import reduce


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def parameter(self):
        ...


class RegularPolygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length

    def area(self):
        ...

    def parameter(self):
        return self.sides * self.side_length


class IrregularPolygon(Shape):
    def __init__(self, sides, *side_lengths):
        self.sides = sides
        self.side_lengths = side_lengths

    def area(self):
        ...

    def parameter(self):
        return sum(self.side_lengths)


class Square(RegularPolygon):
    def area(self):
        return pow(self.side_length, 2)


class Rectangle(IrregularPolygon):
    def area(self):
        result = 1
        for num in self.side_lengths:
            result = result * num
        return result

    def parameter(self):
        return sum(self.side_lengths)*2


def create_shape(number_of_sides, *side_lengths) -> Shape:
    match number_of_sides:
        case 4:
            if len(side_lengths) == 1:
                return Square(number_of_sides, side_lengths[0])
            if len(side_lengths) == 2:
                return Rectangle(number_of_sides, *side_lengths)
            else:
                raise ValueError("Shape not supported at moment")
        case _:
            raise ValueError("Shape not supported at moment")


if __name__ == "__main__":
    obj = create_shape(4, 3, 4)
    print(f"Area of {type(obj).__name__} is {obj.area()}")
    print(f"Parameter of {type(obj).__name__} is {obj.parameter()}")
