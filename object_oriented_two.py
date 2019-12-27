# purpose of Constructor is to set up instance variables
# to have the proper initial values when the object is created
# (attribute values).

# constructor is optional; that's why in previous example
# (object_oriented_one) we didn't even have one.

class PartyAnimal():
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1 # increments instance attribute, not class x! (class x remains at 0)
        print('So far', self.x)

    # destructor
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()

print(an.x)             # result is 2
print(PartyAnimal.x)    # result is 0


