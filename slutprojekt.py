import json
import os
import datetime
from colors import bcolors
from msvcrt import getwch


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_answer(question, answer):
    with open('answer_log.txt', 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H %m:%S")
        file.write(f"{timestamp}: Question: {question}, Answer: {answer}\n")

def main():
    questions = load_questions('questions.json')
    score = 0

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"{j}. {option}")
        print("Your answer:",end="")
        user_answer = getwch()
        correct_answer = question['answer']
        os.systemc('cls')
        save_answer(question['question'], user_answer)
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
    print(f"You got {score} out of {len(questions)} questions correct.")

    if __name__ == "__main__":
        main()
