from random import randint

name = input("Hi! What is your name?")

guess_number = 1
month_number = randint(1, 12)
year_number = randint(1924, 2004)

print("Guess 1:", name, "were you born in",
     month_number, "/", year_number, "?")

response = input("yes or no?")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")

# Guess 2

month_number = randint(1, 12)
year_number = randint(1924, 2004)

print("Guess 2:", name, "were you born in",
    month_number, "/", year_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")

# Guess 3

month_number = randint(1, 12)
year_number = randint(1924, 2004)

print("Guess 3:", name, "were you born in",
    month_number, "/", year_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")

# Guess 4

month_number = randint(1, 12)
year_number = randint(1924, 2004)

print("Guess 4:", name, "were you born in",
    month_number, "/", year_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")

# Guess 5

month_number = randint(1, 12)
year_number = randint(1924, 2004)

print("Guess 5:", name, "were you born in",
    month_number, "/", year_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("I dont wanna do this anymore!")
