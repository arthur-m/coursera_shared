class PartyAnimal():
    x = 0

    def party(self):   # self refers to the class instance (object)
        self.x += 1
        print('So far {}'.format(self.x))


an = PartyAnimal()

an.party()
an.party()
an.party()

# note:
# calling   an.party()      instance, method

# is identical to calling the class, its method, and giving
# the instance as the argument:

# PartyAnimal.party(an)

# because when you do an.party(), what is actually being
# called is party(self), where self is the instance, an.



