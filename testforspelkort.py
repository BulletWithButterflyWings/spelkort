import random
rätt=1

print("Hej och välkommen till mitt spelprogram!") #
print("Nu måste du gissa ett tal, och hoppas att det är rätt! ") #
 
 
while rätt !=0: 
    guess= input("Gissa ett tal mellan 1-5 : ")
    number=random.randint(1,5) #
    print(number) #
    if int(guess) == number : #
        print("Du gissade rätt!") #
        rätt = 0 #
    else: #
        print("Du gissade fel, försök igen!") #
        