# Python-Version: Python 3.9

import csv
import os
import random


def read_csv(path):
    """CSV-Datei lesen.
    Quiz-Fragen werden in einer verschachtelten Liste gespeichert.
    Format: list_questions = [Frage, [Antwort 1, Antwort 2, ..., Antwort 4], korrekte Antwort]
    ----
    Parameter:
    path = Pfad zur csv-Datei
    ----
    Rückgabewert:
    list_questions = Liste mit Fragen und Antworten"""

    list_questions = []
    with open(path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            question = row[0], row[1:5], row[5]
            list_questions.append(question)
    return list_questions


def capitals_quiz(list_questions):
    """Die Quizfragen aus der Liste werden dem Benutzer nacheinander gestellt.
    Der Benutzer kann aus 4 Antwortmöglichkeiten auswählen.
    Nachdem alle Fragen beantwortet wurden, bekommt der Benutzer ein Ergebnis.
    ---
    Parameter:
    list_question = Verschachtelte Listen aus der Funktion read_csv
    ---
    Rückgabewert:
    string: Ergebnis → richtige Antworten von allen Antworten
                     → richtige Antworten dividiert durch alle Antworten
    """
    print("Welcome to the 'Capitals of Europe'-Quiz!")
    # Variablen fürs Endergebnis erstellen
    score = 0
    max_score = len(list_questions)
    # Damit die Fragen nicht immer in derselben Reihenfolge kommen
    random.shuffle(list_questions)

    for element in list_questions:
        # Frage wird gestellt
        print(f"What is the capital of {element[0]}?")
        # Antwortmöglichkeiten werden angezeigt
        for el in range(0, 4):
            print(f"[{el + 1}]: {element[1][el]}")
        # Falls der Benutzer eine ungültige Eingabe macht, wird die Frage wiederholt.
        user_input_1 = False
        while user_input_1 is False:
            try:
                user_answer = int(input("Answer? "))
                if 1 <= user_answer <= 4:
                    user_input_1 = True
                else:
                    print("Input a number from 1 to 4.")
            except ValueError:
                print("Input the number next to the correct answer.")
        # Feedback, ob die Frage richtig beantwortet wurde
        # Falls die Frage falsch beantwortet wurde, wird die richtige Antwort ausgegeben.
        if int(element[2]) == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!")
            print(f"The correct answer was {element[1][int(element[2]) - 1]}.\n")

    return print(f"Correct Answers: {score}/{max_score}\nScore: {score / max_score:.2f}\n")


# Pfad zur csv-Datei anlegen
path_folder = os.path.dirname(__file__)
name_csv = "quiz_all_questions.csv"
path_csv = os.path.join(path_folder, name_csv)

# Schleife um nach Beendigung das Quiz nochmal zu starten
play_quiz = True
while play_quiz is True:
    capitals_quiz(read_csv(path_csv))
    # Wenn eine ungültige Eingabe gemacht wird, kann sie wiederholt werden.
    while True:
        user_input_2 = input("Do you want to try again? [y/n]\n")
        if user_input_2.lower() == "j":
            break
        elif user_input_2.lower() == "n":
            play_quiz = False
            print("Quiz fertig.")
            break
        else:
            print("Repeat the input. 'y' for yes. 'n' for no.\n")
