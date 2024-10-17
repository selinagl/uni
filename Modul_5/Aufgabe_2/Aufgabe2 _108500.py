"""https://www.w3schools.com/python/ref_random_shuffle.asp
https://docs.python.org/3/library/os.path.html"""

# Python-Version: Python 3.9
import csv
import os
import random

# Pfad für csv anlegen
path_folder = os.path.dirname(__file__)
name_csv = "quiz_questions.csv"
path_csv = os.path.join(path_folder, name_csv)


def read_csv(path):
    """CSV-Datei lesen.
    Quiz_Fragen werden in einer verschachtelten Liste gespeichert."""
    list_questions = []
    with open(path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            question = row[0], row[1:5], row[5]
            list_questions.append(question)
    return list_questions


def capitals_quiz(list_questions):
    """
    """
    score = 0
    max_score = len(list_questions)
    random.shuffle(list_questions)

    for element in list_questions:
        print(element[0])
        for el in range(0, 4):
            print(f"[{el + 1}]: {element[1][el]}")
        user_input_1 = False
        while user_input_1 is False:
            try:
                user_answer = int(input("Answer? "))
                if 1 <= user_answer <= 4:
                    user_input_1 = True
                else:
                    print("Input a number from 1 to 4.")
            except ValueError:
                print("Enter the number next to the correct answer.")

        if int(element[2]) == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!")
            print(f"Correct answer is {element[1][int(element[2]) - 1]}.\n")

    result = score / max_score

    return print(f"Quiz finished.\nCorrect Answers: {score}/{max_score}\nScore: {result:.2f}")


capitals_quiz(read_csv(path_csv))

play_quiz = True
while play_quiz is True:
    user_input_2 = input("Play again? [y/n]")
    if user_input_2 == "y":
        capitals_quiz(read_csv(path_csv))
    elif user_input_2 == "n":
        play_quiz = False
    else:
        print("Repeat the input. 'y' for yes. 'n' for no.")
