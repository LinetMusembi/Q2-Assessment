#1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# input....Length of the story,the moral lesson in the story,and the age group the story is intended for.
# outout....the story,storyteller and a translator.
# Process...create a class Story,give it attributes length,lesson and age.Create different methods.

class Story:
    def __init__(self, title, content, length, intended_age_group):
        self.title = title
        self.content = content
        self.length = length
        self.intended_age_group = intended_age_group

class StoryTeller:
    def __init__(self, name, culture):
        self.name = name
        self.culture = culture

class Translator:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def translate(self, story, target_language):
        pass(self,story,target_language)

# # 2.**African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# input....ingredients,preparation-time,cooking-method,nutritional-information
# Output...subclasses for(MoroccanRecipe,EthiopianRecipe and NigerianRecipe),each with its own properties 
# and methods.
# Process...create main class known as Recipe,create sub classes for MoroccanRecipe,EthiopianRecipe and NigerianRecipe
# and add properties and methods to it.

class Recipe:
   def __init__(self, ingredients, time, method, nutrition):
       self.ingredients = ingredients
       self.time = time
       self.method = method
       self.nutrition = nutrition
class MoroccanRecipe:
    def __init__(self, food,nutrients):
        self.food = food
        self.nutrients = nutrients
class EthiopianRecipe:
    def __init__(self.requirements,amount,time) 


# #**Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance. 

# Input....diet,lifespan
# Output..species,predators,others prey
# Process...create a class known as Migration with the followming attributes..diet,lifespan,migration patterns

class Species:
    def __init__(self, diet, lifespan):
        self.diet = diet
        self.lifespan = lifespan

class Predator(Species):
    def __init__(self, diet, lifespan, hunting_method):
        super().__init__(diet, lifespan)
        self.hunting_method = hunting_method

class Prey(Species):
    def __init__(self, diet, lifespan, running_speed):
        super().__init__(diet, lifespan)
        self.running_speed = running_speed


# # **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
                

#Input...lineup,schedule,stage arrangements
# Output..artist,performance and stage
# Process...

# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

# Input...create a class called Product with the following attributes..name,price,quantity
# create Product objects
# calculate total value


class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_value(self):
    return self.price * self.quantity


product1 = Product("Product 1", 10, 2)
product2 = Product("Product 2", 15, 3)


total_value = product1.calculate_value() + product2.calculate_value()

print("Total value of all products:", total_value)
    
# # Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

# input...create a class called Student with the following attributes..name,age and grades

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
    
    def has_passed(self):
        return self.calculate_average_grade() >= 60
    
# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.   
# 
# # Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.  
# 
# First,I will create a class called FlightBooking,then create a dictionary of flight_ids,another dictionary
# of passenger_ids and lastly a list of booking objects. 
# create different methods such as search_flights,reserve_seats,get passenger_information and booking_confirmation
# def search_flights I will pass in attributes destination and date 
class FlightBooking:
    def __init__(self):
        self.flights = {} 
        self.passengers = {}
        self.bookings = []
        
    def search_flights(self, destination, date):
        matching_flights = []
        for flight_id, flight in self.flights.items():
            if flight.destination == destination and flight.date == date:
                matching_flights.append(flight)
        return matching_flights
        
    def reserve_seats(self, flight_id, passenger_id, num_seats):
        if flight_id not in self.flights:
            return ("Such flight does not exist")
        flight = self.flights[flight_id]
        if not flight.has_available_seats(num_seats):
            return ("There are no available seats")
        if passenger_id not in self.passengers:
            self.passengers[passenger_id] = passenger(passenger_id)
        passenger = self.passengers[passenger_id]
        booking = booking(flight_id, passenger_id, num_seats)
        flight.reserve_seats(num_seats)
        passenger.add_booking(booking)
        self.bookings.append(booking)
        
    def get_passenger_info(self, passenger_id):
        if passenger_id not in self.passengers:
            return ("This passenger does not exist")
        passenger = self.passengers[passenger_id]
        return passenger.get_info()
    
    def generate_booking_confirmation(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return str(booking)
        return("Such booking is not available")




            