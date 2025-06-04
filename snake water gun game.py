import random
computer=random.choice([1,-1,0])
youstr=input("enter your choice :")
youdict={"s":1,"w":-1,"g":0}
reverseddict={1:"snake", -1:"water",0:"gun"}
you=youdict[youstr]
print(f"you chose {reverseddict[you]}\n computer chose{reverseddict[computer]}")

# you2=(1,-1,0)
if(computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win") 
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0): 
        print("You win")
    elif(computer == 0 and you == -1): 
        print("you win")
    elif(computer == 0 and you == 1): 
        print("You lose")   
    else:
        print("somewthing went wrong")        
