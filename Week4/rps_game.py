#Question 4.3
import numpy as np

def play():
    moves = ['R','P','S']
    print ("R --> Rock, P --> Paper, S --> Scissors")
    user = input("Enter R, P or S:").upper()
    
    if user not in moves:
        print("Invalid input, Try again!")
        return
    comp_idx = np.random.randint(0, 3)
    computer = moves[comp_idx]
    print (f"You : {user} | Computer : {computer}")
    
    if user == computer:
        print("Tie!")
    elif (user,computer in [('R','S'),('P','R'),('S','P')]):
        print("You WIN!")
    else:
        print("Computerm WINS!")
play()
