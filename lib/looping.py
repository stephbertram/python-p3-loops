#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
    
# List Comprehension
def square_integers(int_list):
    squared_numbers = [num ** 2 for num in int_list]
    return squared_numbers

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

            