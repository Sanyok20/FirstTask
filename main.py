import math

class Money:
    def __init__(self, whole = 0, cents = 0, currency="UAH"):
        self.currency = currency
        self.whole = 0
        self.cents = 0
        self.set_values(whole, cents)

    def set_values(self, whole, cents):
        total = whole * 100 + cents
        if total < 0:
            total = 0
        self.whole = total // 100
        self.cents = total % 100

    def display(self):
        print(f"{self.whole}.{self.cents:02d} {self.currency}")

    def __str__(self):
        return f"{self.whole}.{self.cents:02d} {self.currency}"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def decrease_price(self, amount):
        total = self.price.whole * 100 + self.price.cents - round(amount * 100)
        if total < 0:
            total = 0
        self.set_price(total)

    def set_price(self, total):
        self.price.set_values(total // 100, total % 100)

    def display(self):
        print(f"{self.name}: {self.price}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __add__(self, value):
        r = self.radius + value
        if r < 0:
            r = 0
        return Circle(r)

    def __sub__(self, value):
        r = self.radius - value
        if r < 0:
            r = 0
        return Circle(r)

    def __iadd__(self, value):
        self.radius += value
        if self.radius < 0:
            self.radius = 0
        return self

    def __isub__(self, value):
        self.radius -= value
        if self.radius < 0:
            self.radius = 0
        return self

    def __str__(self):
        return f"Circle(r={self.radius}, L={self.length():.2f})"

class Airplane:
    def __init__(self, plane_type, max_passengers, passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.passengers = 0
        if passengers > max_passengers:
            self.passengers = max_passengers
        elif passengers > 0:
            self.passengers = passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, count):
        p = self.passengers + count
        if p > self.max_passengers:
            p = self.max_passengers
        if p < 0:
            p = 0
        return Airplane(self.plane_type, self.max_passengers, p)

    def __sub__(self, count):
        p = self.passengers - count
        if p > self.max_passengers:
            p = self.max_passengers
        if p < 0:
            p = 0
        return Airplane(self.plane_type, self.max_passengers, p)

    def __iadd__(self, count):
        self.passengers += count
        if self.passengers > self.max_passengers:
            self.passengers = self.max_passengers
        if self.passengers < 0:
            self.passengers = 0
        return self

    def __isub__(self, count):
        self.passengers -= count
        if self.passengers > self.max_passengers:
            self.passengers = self.max_passengers
        if self.passengers < 0:
            self.passengers = 0
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __str__(self):
        return f"Airplane({self.plane_type}, {self.passengers}/{self.max_passengers})"

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"Flat(area={self.area}, price={self.price})"

m = Money(120, 50, "UAH")
prod = Product("Навушники", m)
prod.display()
prod.decrease_price(20.25)
prod.display()

c1 = Circle(5)
c2 = Circle(8)
print(c1 == Circle(5), c2 > c1)
c1 += 3
print(c1)

a1 = Airplane("Boeing 737", 180, 100)
a2 = Airplane("Airbus A320", 190, 120)
print(a1 == a2, a2 > a1)
a1 += 20
print(a1)

f1 = Flat(60, 80000)
f2 = Flat(60, 90000)
print(f1 == f2, f1 != f2, f2 > f1)