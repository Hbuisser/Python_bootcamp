import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.") 
print("Type 'exit' to end the game.")
print("Good luck!")

count = 0
bonus = 0
do = 1
x = random.randint(0, 99)
if x == 42:
    bonus = 1

print("What's your guess between 1 and 99?")
answer = input("-->")
if answer == "exit":
    print("Goodbye!")
    do = 0
else:
    answer = int(answer)

if do == 1:
    if answer == x:
        print("you won the first time!")
        count = 1
        if bonus == 1:
            print("The answer to the ultimate question of life, the universe and everything is 42. Congratulations! You got it on your first try!")

    while answer != x:
        if answer > x:
            count += 1
            print("Too high!")
        elif answer < x:
            count += 1
            print("Too low!")
        print("What's your guess between 1 and 99?")
        answer = input("-->")
        if answer == "exit":
            print("Goodbye!")
            do = 0
            break
        else:
            answer = int(answer)

    if count > 1 and do == 1:
        if answer == x and bonus == 1:
            print("The answer to the ultimate question of life, the universe and everything is 42. Congratulations! You got it on your first try!")
        elif answer == x:
            print("Congratulations, you've got it!")
            print("You won in {0} attempts!".format(count))
