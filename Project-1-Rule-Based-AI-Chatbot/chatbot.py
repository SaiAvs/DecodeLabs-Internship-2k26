# ===============================================================
# DecodeLabs AI Internship
# Project 1 : Rule-Based AI Chatbot
# Author : Sai
# ===============================================================

from datetime import datetime
import random
import math

# ===============================================================
# GLOBAL VARIABLES
# ===============================================================

BOT_NAME = "DecodeBot"

session_start = datetime.now()

commands_used = 0
calculator_used = 0
games_played = 0

# ===============================================================
# DATABASE
# ===============================================================

jokes = [
    "Why don't programmers like nature? Because it has too many bugs! 😂",
    "Why do Python developers wear glasses? Because they can't C. 😎",
    "Debugging is like being the detective in a crime movie where you're also the criminal.",
    "There are only 10 kinds of people. Those who understand binary and those who don't."
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Dream big. Start small. Act now.",
    "The future depends on what you do today.",
    "Every expert was once a beginner."
]

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "The first computer bug was an actual moth.",
    "Artificial Intelligence is transforming healthcare.",
    "NASA uses AI in several space missions."
]

# ===============================================================
# WELCOME
# ===============================================================

def welcome():

    print("\n" + "=" * 65)
    print("               🤖 DECODEBOT v2.0")
    print("          Rule-Based AI Chatbot")
    print("       DecodeLabs AI Internship Project")
    print("=" * 65)

    name = input("\n👤 Enter your name : ").title()

    print(f"\nWelcome {name} 👋")
    print("I'm DecodeBot.")
    print("Type 'help' to see all available commands.")

    return name


# ===============================================================
# HELP MENU
# ===============================================================

def show_help():

    print("\n" + "=" * 65)
    print("AVAILABLE COMMANDS")
    print("=" * 65)

    print("""
👋 Greetings
--------------
hello
hi
hey

📅 Information
--------------
date
time
day

😂 Entertainment
----------------
joke
quote
fact

🧮 Utilities
-------------
calculator

🎮 Games
---------
game

❓ System
----------
help
exit
""")


# ===============================================================
# DATE
# ===============================================================

def show_date():
    print("\n📅", datetime.now().strftime("%d %B %Y"))


# ===============================================================
# TIME
# ===============================================================

def show_time():
    print("\n🕒", datetime.now().strftime("%I:%M:%S %p"))


# ===============================================================
# DAY
# ===============================================================

def show_day():
    print("\n📆", datetime.now().strftime("%A"))


# ===============================================================
# JOKE
# ===============================================================

def tell_joke():
    print("\n😂", random.choice(jokes))


# ===============================================================
# QUOTE
# ===============================================================

def tell_quote():
    print("\n💡", random.choice(quotes))


# ===============================================================
# FACT
# ===============================================================

def tell_fact():
    print("\n🌍", random.choice(facts))


# ===============================================================
# CALCULATOR
# ===============================================================

def calculator():

    global calculator_used

    calculator_used += 1

    while True:

        print("\n" + "=" * 60)
        print("SMART CALCULATOR")
        print("=" * 60)

        print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Percentage
8. Square Root
9. Back
""")

        choice = input("Choose Operation : ")

        if choice == "9":
            return

        try:

            if choice == "8":

                number = float(input("Enter Number : "))
                print("Result :", math.sqrt(number))
                continue

            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))

            if choice == "1":
                print("Result :", num1 + num2)

            elif choice == "2":
                print("Result :", num1 - num2)

            elif choice == "3":
                print("Result :", num1 * num2)

            elif choice == "4":

                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print("Result :", num1 / num2)

            elif choice == "5":
                print("Result :", num1 ** num2)

            elif choice == "6":
                print("Result :", num1 % num2)

            elif choice == "7":
                print("Percentage :", (num1 / num2) * 100)

            else:
                print("Invalid Choice")

        except ValueError:
            print("Please enter valid numbers.")
# ===============================================================
# GUESS THE NUMBER GAME
# ===============================================================

def guess_game():

    global games_played

    games_played += 1

    while True:

        print("\n" + "=" * 60)
        print("🎮 GUESS THE NUMBER")
        print("=" * 60)

        print("""
Choose Difficulty

1. Easy (1 - 10)
2. Medium (1 - 50)
3. Hard (1 - 100)
4. Back
""")

        difficulty = input("Choose : ")

        if difficulty == "4":
            return

        if difficulty == "1":
            limit = 10

        elif difficulty == "2":
            limit = 50

        elif difficulty == "3":
            limit = 100

        else:
            print("Invalid Choice")
            continue

        number = random.randint(1, limit)
        attempts = 0

        print(f"\nI have selected a number between 1 and {limit}.")

        while True:

            try:

                guess = int(input("Enter Guess : "))
                attempts += 1

                if guess == number:

                    print("\n🎉 Congratulations!")
                    print(f"You guessed it in {attempts} attempts.")

                    break

                elif guess < number:
                    print("📈 Too Low")

                else:
                    print("📉 Too High")

            except ValueError:
                print("Please enter a valid number.")

        again = input("\nPlay Again? (y/n) : ").lower()

        if again != "y":
            return


# ===============================================================
# SESSION SUMMARY
# ===============================================================

def session_summary(name):

    session_end = datetime.now()

    duration = session_end - session_start

    print("\n" + "=" * 65)
    print("SESSION REPORT")
    print("=" * 65)

    print(f"👤 User               : {name}")
    print(f"🕒 Session Started    : {session_start.strftime('%I:%M:%S %p')}")
    print(f"🕒 Session Ended      : {session_end.strftime('%I:%M:%S %p')}")
    print(f"⏳ Duration           : {duration}")

    print()

    print(f"💬 Commands Used      : {commands_used}")
    print(f"🧮 Calculator Used    : {calculator_used}")
    print(f"🎮 Games Played       : {games_played}")

    print("\nThank you for using DecodeBot ❤️")
    print("=" * 65)


# ===============================================================
# MAIN PROGRAM
# ===============================================================

def main():

    global commands_used

    name = welcome()

    while True:

        user = input(f"\n{name} ➜ ").lower().strip()

        commands_used += 1

        # Greetings
        if user in ["hello", "hi", "hey"]:

            print(f"\n🤖 Hello {name}! 😊")

        # Bot Name
        elif user in ["your name", "who are you"]:

            print("\n🤖 I am DecodeBot.")
            print("A Rule-Based AI Chatbot built using Python.")

        # How are you
        elif user == "how are you":

            print("\n🤖 I'm doing great!")
            print("Hope you're having a wonderful day. 😊")

        # Date
        elif user == "date":
            show_date()

        # Time
        elif user == "time":
            show_time()

        # Day
        elif user == "day":
            show_day()

        # Joke
        elif user == "joke":
            tell_joke()

        # Quote
        elif user == "quote":
            tell_quote()

        # Fact
        elif user == "fact":
            tell_fact()

        # Calculator
        elif user == "calculator":
            calculator()

        # Game
        elif user in ["game", "guess", "guess number"]:
            guess_game()

        # Help
        elif user == "help":
            show_help()

        # Exit
        elif user in ["exit", "bye", "quit"]:

            session_summary(name)

            print("\n👋 Goodbye!")
            break

        # Unknown Command
        else:

            print("\n❌ Command Not Found.")
            print("Type 'help' to view available commands.")


# ===============================================================
# PROGRAM START
# ===============================================================

if __name__ == "__main__":

    main()