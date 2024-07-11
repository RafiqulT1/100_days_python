
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)

# add(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", seats=4, color="red")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)