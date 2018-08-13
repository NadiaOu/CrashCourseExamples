# class Restaurant():
#     """A simple Restaurant Class"""
#
#     def __init__(self,restaurant_name,cuisine_type):
#         "I will initialise here"
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print("The restaurant is now open ")
#
#
# myRestaurant =Restaurant("LemonCurdPie","Bakery")
# myRestaurant.describe_restaurant()
# myRestaurant.open_restaurant()
#
#
# my1rstRestaurant =Restaurant("ChickenLoco","Mexican")
# my1rstRestaurant.describe_restaurant()
# my1rstRestaurant.open_restaurant()
#
#
# my2ndRestaurant =Restaurant("Sougamo","Chinese")
# my2ndRestaurant.describe_restaurant()
# my2ndRestaurant.open_restaurant()


# class User():
#
#     def __init__(self,first_name, last_name, age, gender, stupid):
#         "I will initialise here"
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age=age
#         self.gender= gender
#         self.stupid =stupid
#
#     def describe_user(self):
#         print("the name is " + self.first_name.title() +" " + self.last_name.title() +" , "+ self.age.title() + self.gender.title() +"and he is"+ self.stupid.title())
#
#     def greet_user(self):
#         print("Hello " + self.first_name.title())
#
# myUser = User("Leonidas" ,"Peponis", "12", "Male", "YEs")
#
# myUser.describe_user()


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
