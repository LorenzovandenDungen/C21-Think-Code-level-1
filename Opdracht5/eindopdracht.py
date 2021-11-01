def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Antwoorden: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("ingevuld: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Jouw score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Wil je opnieuw spelen? (ja of nee): ")
    response = response.upper()

    if response == "JA":
        return True
    else:
        return False
# -------------------------


questions = {
 "Welke kleur is een banaan?: ": "A",
 "Welke kleur is een appel: ": "B",
 "Wat is 1 + 1: ": "C",
 "Is de aarde rond?: ": "A"
}

options = [["A. Geel", "B. Blauw", "C. rood", "D. paars"],
          ["A. Blauw", "B. Rood/Groen", "C. geel", "D. zwart"],
          ["A. 4", "B. 1", "C. 2", "D. 3"],
          ["A. Ja","B. Nee", "C. soms", "D. Nee, het is vierkant"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")