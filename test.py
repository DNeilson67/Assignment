import random

randomint = random.randint(1,100)
print(randomint)

print("GACHA")

guess = False

while guess == False:
    inputint = int(input("Insert 1-100:"))
    if inputint < randomint:
        print("Too high")
    elif inputint > randomint:
        print("Too low")
    elif inputint == randomint:
        print("congrats")
        guess = True



