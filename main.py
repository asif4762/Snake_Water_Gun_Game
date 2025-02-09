import random
'''
1 for snake 
-1 for snake
0 for gun
'''

computer = random.choice([0,1,-1])
youstr = input("Enter your choice : ")
youDist = {"s" : 1, "w" : -1, "g" : 0}
reversDist = {1 : "Snake", -1 : "Water",  0 : "Gun"}
you = youDist[youstr]

print(f"You chose {reversDist[you]}\nComputer chose {reversDist[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong!")
