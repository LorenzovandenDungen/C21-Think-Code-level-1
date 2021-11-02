print("welkom bij mijn quiz")
username = input("Gebruikersnaam? : ")
print("hey",username, "\nLaten we beginnen! Met ieder goed beantwoorde vraag krijg je een punt.")

playing = True
while playing == True:
    points = 0

    print("Hoe oud ben ik?")
    Answer_1 = input("Vul hier in: ")
    if Answer_1 == "19" or Answer_1 == "19":
        print("Correct!")
        points +=1
    else:
        print("Fout!")


    print("Zijn bananen krom?")
    Answer_2 = input("Vul hier in: ")
    if Answer_2 == "ja" or Answer_1 == "Ja":
        print("Correct!")
        points +=1
    else:
        print("Fout!")


    print("is sporten gezond?")
    Answer_3 = input("Vul hier in: ")
    if Answer_3 == "ja" or Answer_1 == "Ja":
        print("Correct!")
        points +=1
    else:
        print("Fout!")

    final_Question = input("Do you want to play again")   
    if final_Question == "Yes" or final_Question == 'yes':
        playing = True
    else:
        break
print("Bedankt voor het spelen. Jouw punten zijn",points)             
