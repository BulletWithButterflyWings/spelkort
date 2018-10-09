import random 
rätt=1
list=[]  

print("Hej och välkommen till mitt spelprogram!") 
print("Nu måste du gissa ett tal, och hoppas att det är rätt! ") 
number=random.randint(1,10)
while rätt !=0: 
    guess= input("Gissa ett tal mellan 1-10 : ")
  
    list.append(guess)
    print(number) 
    if int(guess) == number : 
        print("Du gissade rätt!") 
        rätt = 0 
    else: 
        print("Du gissade fel, försök igen!") 

   
    print("Detta är dina gissningar",list) 