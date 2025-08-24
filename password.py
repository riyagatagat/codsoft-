
import random
length = int(input("enter the length of password"))
alpha = ['A',"B","C","D","E","F","G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']   
spl = ["!",'@','#','$','*']
if length >= 6:
    password = []   
    for i in range(length):
        choose = random.choice([alpha, num, spl])  
        password.append(random.choice(choose))
    print("Generated password:", "".join(password))
else
print("the length of password should be greater than 6")
