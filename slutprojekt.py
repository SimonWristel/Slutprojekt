import json
import os
import datetime
from colors import bcolors
from msvcrt import getwch

os.system('cls')

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_answer(question, answer):
    with open('answer_log.txt', 'a', encoding='utf-8') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: Question: {question}, Answer: {answer}\n")

def main():
    questions = load_questions('questions.json')
    score = 0

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        options = { "1": question.get('a'), "2": question.get('b'), "3": question.get('c'), "4": question.get('d')}
        
        for key, option in options.items():
            if option is not None:
                print(f"{key}. {option}")

        print("Your answer (1-4): ", end="")
        user_answer = getwch()
        print(user_answer)  # Debugging line to see the captured input

        correct_answer = question['key']
        os.system('cls')
        save_answer(question['question'], user_answer)

        try:
            if options[user_answer] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        except (ValueError, KeyError):
            print("Invalid input. Please enter a number between 1 and 4.")

    print(f"You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    main()