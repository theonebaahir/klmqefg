# character occurence
string = input("please enter your word")
char = input("please enter your character")

i = 0
count = 0
 
while (i < len(string)):
    
    
    if(string[i]== char):
         
         count = count+1
         
    i = i +1
    
    
print("the total number of times ", char ,"has occured=", count)










lower = int(input("enter a lower range"))
upper = int(input("enter a upper range"))
print("prime number between ", lower, "and", upper,"are:")

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            
        else:
            print(num)
            
            
            
            
            
            
            
            num = int(input("enter the number:"))
            
