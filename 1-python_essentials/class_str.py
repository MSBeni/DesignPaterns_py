class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width

    def __str__(self):
        return "rectangle height and weight are {} and {} respectively".format(self.height, self.width)


area_calc = Area(4, 5)
print(area_calc.area())
# this line happen because of the __str__
print(str(area_calc))
