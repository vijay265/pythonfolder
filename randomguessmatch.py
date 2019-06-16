import random
a=random.randint(1,20)
b=int(input("enter a number"))
for i in range(4):
    if b<a:
        print("random no. is smaller than entered no.")
    elif b>a:
        print("random no. is greater than entered no.")
    else:
        break
print("user entered",b)
print("random no.",a)
if a==b:
    print("you win")
        

        
            


