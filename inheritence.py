# child class / sub class - inherits from Parent class
# but don't think of it as 'smaller' or 'less than' parent - that's wrong!
# it actually has all the attributes and behaviors of the parent,
# pluse MORE; it adds to and extends the functionality of the
# parent. or it can just be more 'specialized' than the parent class is.
# so it can be parent +more, or parent(specialized), etc.

# main goal is reusing code / not repeating yourself.

# inheritence: the ability to extend a class to make a new class.

 class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

# need inheritence example here


