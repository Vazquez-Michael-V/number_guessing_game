import random
     
x = random.randint(1, 5)
#print(x) Hide answer.

user_guess = (input("Guess a number from 1 to 5. Type 'quit' to exit the game.\n"))

while True: 

    #Quit and nonsense input.
    if user_guess.lower() == 'quit':
        print("\nGame over.")
        break
    elif user_guess.isnumeric() == False and user_guess.lower != 'quit':
        user_guess = input("Please type an integer, or 'quit' to end the game.\n")

    #Check the range of the guess.
    elif int(user_guess) not in range(1, 6):
        user_guess = input("Guess must be an integer from 1 to 5.\n")

    #Gives hints, to guess higher or lower. 
    elif int(user_guess) < x:
        user_guess = input("Guess a higher integer.\n")                      
    elif int(user_guess) > x:        
        user_guess = input("Guess a lower integer.\n")
                
    #Winning condition.    
    elif int(user_guess) == x:
        print("\nWinner winner, chicken dinner!")
        break



   
    

   

    