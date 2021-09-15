class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        result = 2 * Circle.__pi * self.radius
        return result

    def calculate_area(self):
        result = Circle.__pi * (self.radius ** 2)
        return result

    def calculate_area_of_sector(self, angle):
        result = Circle.calculate_area(self) * (angle / 360)
        return result
