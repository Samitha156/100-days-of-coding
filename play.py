def add(*args):
    c = 0
    for n in args:
        c += n
    return c


sum = add(2,5,6,5)
print(sum)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, mul=5)

class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.make = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)