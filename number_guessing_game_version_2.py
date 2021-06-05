import random

#Tell user to create range [a, b]
instructions = "Before integer guessing begins, please create interval [a, b] such that a <= b, where a => 0 and b => 0. "
instructions += "After interval is created, guess an integer x such that a <= x <= b.\n"
print(instructions)

#User creates lower bound or quits.
a = input("Type the minimum integer on the interval. ")
while True:
    if a.isnumeric() == True:
        a = int(a)
        print("Interval lower bound created.\n")
        break
    elif a.lower() == 'quit':
        print("\nGame over.")
        quit()
    else:
        a = input("ERROR! Inverval lower bound must be an integer greater than or equal to zero. \nPlease enter an integer greater than or equal to zero.\n")
        

#User creates upper bound or quits.
b = input("Type the maximum integer on the interval. ")    
while True:
    if b.isnumeric() == True:
        b = int(b)
        if a <= b:
            print("Interval upper bound created.\n")
            break
        else:
            b = input("Upper bound b must be greater than or equal to lower bound a. ")
    elif b.lower() == 'quit':
        print("\nGame over.")
        quit()
    else:
        b = input("ERROR! Inverval upper bound must be an integer greater than or equal to zero. \nPlease enter an integer greater than or equal to zero.\n")


#Create random integer.
x = random.randint(a, b)
#print(x) Hide answer.

#Create a list to store user guesses.
guesses = []

#Take user guesses, check quit condition, and check for nonsense input.
user_guess = input(f"Guess an integer from [{a}, {b}].\n")
while True:
    if user_guess.lower() == 'quit':
        print("\nGame over.")
        quit()
    elif user_guess.isnumeric() == False or int(user_guess) not in range(a, b+1):
        user_guess = input("Guess must be integer such that a <= guess <=b, where guess => 0. To exit the game, type 'quit'.\n")
    else:
        user_guess = int(user_guess)
        guesses.append(user_guess)  
         #Gives hints, to guess higher or lower.    
        if int(user_guess) < x:
            user_guess = input("Guess a higher integer.\n")
            guesses.append(user_guess)                      
        elif int(user_guess) > x:        
            user_guess = input("Guess a lower integer.\n")
            guesses.append((user_guess))
             
        #Winning condition.    
        elif int(user_guess) == x:
            print("\nWinner winner, chicken dinner!\n")
            guesses.append(int(user_guess))
            break

#Create copy of guesses list, then remove duplicates and strings from guesses copied list.
unique_guesses = guesses[:]
for g in unique_guesses:
    if unique_guesses.count(g) > 1:
        unique_guesses.remove(g)
    if isinstance(g, str) == True:
        unique_guesses.remove(g)
for i in unique_guesses:
    i = int(i)
#print(unique_guesses) Check all elements are integers.

#Show the user guesses made.
c = len(unique_guesses)
print(f"You made {c} guesses.")
print("Your guesses were:")
for u in unique_guesses:
    i = unique_guesses.index(u) + 1
    print(f"Guess {i}:  {u}")

#Basic stats on guesses made.
#Value of smallest guess, and tells user which guess was smallest.
smallest_guess = min(unique_guesses)
sg = unique_guesses.index(smallest_guess) + 1
#print("\n")
print(f"\nSmallest guess was {smallest_guess}, which was guess number {sg}.")

#Value of largest guess, and tells user which guessr was largest.
largest_guess = max(unique_guesses)
lg = unique_guesses.index(largest_guess) + 1
print(f"Largest guess was {largest_guess}, which was guess number {lg}.")