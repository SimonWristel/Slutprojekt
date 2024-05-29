import json
import os
import datetime
from colors import bcolors
from msvcrt import getwch

os.system('cls')

def load_questions(filename): #är en funktion
    with open(filename, 'r', encoding='utf-8') as file: #öppnar filen
        return json.load(file) #används från json filen

def save_answer(question, answer): #detta är kopplad till en log som visar allt du gör
    with open('answer_log.txt', 'a', encoding='utf-8') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #är som en sträng
        file.write(f"{timestamp}: Fråga: {question}, Svar: {answer}\n")

def main():
    questions = load_questions('questions.json')
    score = 0

    for i, question in enumerate(questions, 1):
        print(bcolors.PURPLE + f"Fråga {i}: {question['question']}")
        options = { "1": question.get('a'), "2": question.get('b'), "3": question.get('c'), "4": question.get('d')}
        
        for key, option in options.items(): #är en loop , options är värdet och key är nyckeln
            if option is not None: #om svaret blir none så hoppar den vidare i koden
                print(f"{key}. {option}")

        print(bcolors.CYAN + "Välj mellan (1-4): ", end="") #berättar att du ska svara mellan siffrorna 1-4.
        user_answer = getwch()

        correct_answer = question['key']
        os.system('cls')
        save_answer(question['question'], user_answer) #sparar resultatet

        try:
            if options[user_answer] == correct_answer: #om svaret blir rätt printar koden "Rätt" om koden blir fel printas "Fel"
                print(bcolors.GREEN + "Rätt!")
                score += 1
            else:
                print(bcolors.RED + "Fel!")
        except (ValueError, KeyError):
            print(bcolors.RED + "Invalid input. Please enter a number between 1 and 4.") #om du använder dig av något annat än siffror så printas denna. 

    print(bcolors.YELLOW + f"Du fick {score} av {len(questions)} frågor rätt.") #printar ut ditt slutresultat

if __name__ == "__main__":
    main()