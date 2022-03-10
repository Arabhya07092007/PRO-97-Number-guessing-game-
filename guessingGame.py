import random
number = random.randint(1, 9)
chance = 0


print("Number guessing game")
print("Guess a number (between 1 to 9)")

while chance < 5:
    guess = int(input("Enter your guess:"))

    if guess == number:
        print("Your guess was correct!!!")
        print("You won!!!!")
        break
    elif guess < number:
        print("your guess too low. guess a bigger nunber", guess)
    else:
        print("your guess was too high.Guess the lower number", guess)
        
    chance = chance + 1
    if  chance == 5:
        print("you lose. This is the number ", number)


#
