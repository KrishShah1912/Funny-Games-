import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
# here random is used so that computer can choose any one and start the game so first import random
youstr = input("Enter your choice : ")
youDict = {"s":1 , "w" : -1 , "g" : 0}
revDict= {1:"snake", -1:"water" , 0:"gun"}
you = youDict[youstr]

print(f"Computer opt for {revDict[computer]} and you opt for {revDict[you]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == -1 and you == 0):
        print("you lose")

    elif(computer==-1 and you == 1):
        print("you win")

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer==1 and you == -1):
        print("you lose")

    elif(computer == 0 and you ==1):
        print("you lose")

    elif(computer == 0 and you == -1):
        print("you win")

    else:
        print("something went wrong")

# The below logic will work on the basis of two number like, (computer-you)

# Here i am going to write 4 lines code which will not have readapdivity but works same beocz of logic

# if((computer - you)== -1 or (computer-you) == 2):
    # print("you lose")
# else:
    # print("You win ")