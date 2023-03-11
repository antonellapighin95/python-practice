# Simple function. Create a function colled greet()

def greet():
    print("Hello!")
    print("My name is Anto")
    print("how old are you?")

greet()

# Function with INPUTS

def greeting_with_name(name): #name is parameter
    print(f"Hello {name}!")
    print(f"My name is Anto")
    print(f"How old are you, {name}?")

greeting_with_name("Karen") #Karen is argument

def greetings (name, location):
    print(f"Hello {name}!")
    print(f"My name is Anto, I live in {location}")
    print(f"How old are you, {name}? Where do you live?")

greetings(location = "Barcelona", name = "Jazmin")

# Paiting calculator

# math module round up
import math

def paint_calc(height, width, cover):
    can_number = math.ceil(test_h*test_w/coverage)
    print(f"You'll need {can_number} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# PRIME NUMBER CALCULATOR
def prime_checker(number):
    is_prime = True

    for n in range(2,number):
        if number % n == 0:
            is_prime = False
        
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        

n = int(input("Check this number: "))
prime_checker(number=n)