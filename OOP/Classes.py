# classes

class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Reference
        self.model = model

    def moves(self):
        print("Move Along...")

    def get_make_model(self):
        print(f"I'm a {self.model} {self.make}")


my_car = Vehicle(make='Tesla', model='USA')

my_car.get_make_model()
my_car.moves()


class Aeroplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies a long...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles Along...")


class GolfCart(Vehicle):
    pass


aeroplane = Aeroplane('Cessna', 'USA', 'N-12345')
truck = Truck('Mack', 'Pinnacle')
golfcart = GolfCart('Yamaha', 'GC100')

truck.moves()
golfcart.moves()
print(f"I'm a {aeroplane.make} {aeroplane.faa_id}")
aeroplane.moves()

for v in (my_car, aeroplane, truck, golfcart):
    v.get_make_model()
    v.moves()
