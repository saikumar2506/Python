secret_number=6
guess_count=0
guess_limit=4
print("You have only 4 Guesses")
print("Hint: The number is in between 1 to 10")
while guess_count < guess_limit:
    guess=int(input("Make a Guess of the Number: "))
    guess_count += 1
    if guess == secret_number:
        print('Congratulations,you Win')
        break
else:
    print("Sorry,you have Failed!")