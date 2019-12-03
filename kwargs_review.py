def dict_builder(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# even though it's building a dictionary, we send the arguments in Keyword Arguments format:
dict_builder(City = 'Portland', Population = 1000000)  # <----- CONTRAST THIS...


# the normal format for building a dictionary looks totally different:

my_dict = {'City': 'Portland', 'Population': 1000000}  #<-----  ...WITH THIS

for key, value in my_dict.items():
    print(key, value)

# even though the results are exactly the same

