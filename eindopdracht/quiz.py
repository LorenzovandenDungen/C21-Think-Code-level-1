print("welkom bij mijn quiz")
Gebruikersnaam = input("Gebruikersnaam? : ")
print("hey",Gebruikersnaam, "\nLaten we beginnen! Met ieder goed beantwoorde vraag krijg je een punt.")

playing = True
while playing == True:
    points = 0

    print("Hoe oud ben ik?")
    Antwoord_1 = input("Vul hier in: ")
    if Antwoord_1 == "19" or Antwoord_1 == "19":
        print("Correct!")
        points +=1
    else:
        print("Fout!")


    print("Zijn bananen krom?")
    Antwoord_2 = input("Vul hier in: ")
    if Antwoord_2 == "ja" or Antwoord_2 == "Ja":
        print("Correct!")
        points +=1
    else:
        print("Fout!")


    print("is sporten gezond?")
    Antwoord_3 = input("Vul hier in: ")
    if Antwoord_3 == "ja" or Antwoord_3 == "Ja":
        print("Correct!")
        points +=1
    else:
        print("Fout!")

    Laatste_vraag = input("Wil je opnieuw spelen?")   
    if Laatste_vraag == "Ja" or Laatste_vraag == 'ja':
        playing = True
    else:
        break
print("Bedankt voor het spelen. Jouw punten zijn",points)             
