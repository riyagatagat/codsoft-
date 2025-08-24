import random
num=int(input("enter how many times u want to play the game "))
count=0
count1=0
count2=0
for i in range(num):
 print("\nRound", i + 1)

 print("choose: rock,paper or scissors")
 choose=input("enter what is u r choice")


 list=["rock","paper","scissors"]
 chosen=random.choice(list)
 print("this is computer choice",chosen)

 if(choose=="rock" and chosen=="paper")or (choose=="paper" and chosen=="scissors")or(choose=="scissors" and chosen=="rock"):
     print("computer wins")
     count=count+1
     print("score of computer",count)
     
 elif(choose==chosen):
     print("tie")
     count2=count2+1
     print(" tie score ",count2)
 else:
     print("user wins")
     count1=count1+1
     print("score of the user",count1)

