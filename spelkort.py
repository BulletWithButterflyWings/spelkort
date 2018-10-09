import random # Slumpar tal, mellan de tal som har angets i koden (randint).
rätt=1 # Om rätt tal anges. 
list=[] #

print("Hej och välkommen till mitt spelprogram!") # Skriver ut den text som har angivits (print).
print("Nu måste du gissa ett tal, och hoppas att det är rätt! ") # Skriver ut den text som har angivits (print).
 
number=random.randint(1,10) # Skriver ut ett slumpat nummer, mellan 1-10.
while rätt !=0: # Om rätt tal anges, så avslutas programet.
    guess= input("Gissa ett tal mellan 1-10 : ") # 
    
    list.append(guess) #
    print(number) # Självaste kommandot för slumpade tal.
    if int(guess) == number : # Ett slumpmässigt tal skrivs ut. 
        print("Du gissade rätt!") # Skriver ut (print), när rätt svar har angetts.
        rätt = 0 # Om fel tal anges.
    else: # Om inte rätt tal anges skrivs kommandot nedanför ut. 
        print("Du gissade fel, försök igen!") # Skriver ut (print), när fel svar har angetts. 

        print("Detta är alla dina tidigare gissningar",list) #