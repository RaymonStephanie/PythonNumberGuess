import random
n = random.randrange(0,9)
num = int(input("Guess a number. "))
while(num != n) :
    if num < n :
        num = int(input("Nah, guess something a bit higher. "))
    elif num > n :
        num = int(input("Nah, guess something a bit lower. "))
print("Yay! You got it.")
