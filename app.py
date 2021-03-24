#######################################################################
# Author: Gage Miller                                                 #
# Date Created: 2021-03-23                                            #
# Description: Conversation Bot; have a conversation with a computer! #
#######################################################################

""" Write a program that has a conversation with the user. The program must ask for both strings and numbers as input.
The program must ask for at least 4 different inputs from the user. The program must reuse at least 3 inputs in what
it displays on the screen. The program must perform some form of arithmetic operation on the numbers the user inputs."""

# Importing all from models.py
from models import *


def menu():
    """The menu function gets information from the user,
    and has the program logic built in it as well."""

    # We ask for the users name, and age, then save it to the variables name, and age.
    name = input(
        "Welcome to the Conversation Bot!"
        "\nI'm Bot, what's your name?"
        "\nEnter Name: ").title()

    age = input(
        f"Hello {name}! How old are you?"
        f"\nEnter age: ")

    # This block of code checks if age was entered correctly,
    # if not, the program will ask for age again.
    while True:
        try:
            int(age)
            break
        except ValueError:
            print("That's not right! Enter a number.")
            age = input(f"\nEnter age: ")

    # Here, we give the user their options
    # for the guessing game logic found after the print statement.
    print(
        f"{age}? Interesting."
        f"\nI'd like to guess your birth month."
        f"\nI'm going to guess in number format."
        f"\nIf I am to high, press (h)."
        f"\nIf I am to low, press (l)."
        f"\nIf I guess correctly press (w)!")

    # A dictionary where key == month in int format, and value == month in string format.
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    # This is a binary search algorithm that
    # will guess a number between the variables high, and low.
    high = 13
    low = 0

    while True:
        rand = (high + low) // 2
        print(f"My guess is {rand} for {months[rand]}.")

        user_response = input("How did I do?"
                              "\nanswer> ").lower()

        if user_response == "h":
            high = rand
        elif user_response == "l":
            low = rand
        elif user_response == "w":
            print("That wasn't so hard!")
            break
        else:
            print("Hmmm, i'm not sure what that means.")

    # We create an instance of the User class using the information from the variables name, age, and rand.
    user = User(name=name, age=age, birth_month=rand)

    # This block displays user information using the User class.
    # This is also the logic to end the program.
    quit_program = input(
        f"\nWell {user.name}, I will always remember you as of {user.created_date}."
        f"\nI'm glad you let me guess your birth month of {months[user.birth_month]},"
        f"\nI know at the age of {user.age}, you've grown out of playing games,"
        f"\nSo press (q) to quit."
        f"\n=> ").lower()

    # A while loop to check if the user hit "q" to quit the program.
    while True:
        if quit_program == "q":
            print("Goodbye!")
            break
        else:
            quit_program = input("Just hit (q)!")


# This code executes the menu function.
if __name__ == "__main__":
    menu()
