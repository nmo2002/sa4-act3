number = 10

print("I'm thinking of a number...")
guess = str(input("What number am I thinking of? "))

if int(guess) > int(number):
    print("Too high")
if int(guess) < int(number):
    print("Too low")


while guess != str(number):
    guess = str(input("Try again: "))
    if int(guess) > int(number):
        print("Too high")
    if int(guess) < int(number):
        print("Too low")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")


if guess == str(number):
   print("Congratulations! You guessed the right number.")
else:
   print(f"Sorry! The number was {number}.")

