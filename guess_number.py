number = 10
limit = 10

print("I'm thinking of a number...")
guess = str(input("What number am I thinking of? "))

if int(guess) > int(number):
    print("Too high")
if int(guess) < int(number):
    print("Too low")
    
print(f'{limit-1} guesses remaining')

while guess != str(number) and limit != 0:
    limit -= 1
    guess = str(input("Try again: "))
    if int(guess) > int(number):
        print("Too high")
    if int(guess) < int(number):
        print("Too low")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
    print(f'{limit-1} guesses remaining')


if guess == str(number):
   print("Congratulations! You guessed the right number.")
else:
   print(f"Sorry! The number was {number}.")

