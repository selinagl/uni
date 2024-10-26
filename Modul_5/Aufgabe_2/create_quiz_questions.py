import requests
import os
import csv
import random


def get_country_capital():
    """Länder mit Hauptstadt werden von API-Website bezogen.
    ------
    Rückgabewert:
    countries_dict = {Land: Hauptstadt}"""

    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    # Testet, ob Website verfügbar ist, bevor sie aufgerufen wird
    if response.status_code == 200:
        countries = response.json()

    countries_dict = {}
    for c in countries:
        country = c.get("name", {}).get("common", "N/A")
        capital = c.get("capital", ["N/A"])[0]
        countries_dict[country] = capital
    return countries_dict


def write_quiz_csv(p_csv, quiz_dict):
    """Schreibt die csv-Datei im gewünschten Format.
    Falsche Antworten werden aus dem Pool aus allen Fragen genommen.
    -----
    Parameter:
    p_csv = Pfad zur csv-Datei, in die geschrieben wird
    quiz_dict = {Land: Hauptstadt} (aus Funktion get_country_capital())
    -----
    kein Rückgabewert → Funktion schreibt gleich in csv-Datei
    """
    # Liste mit Pool an falschen Antworten erstellen
    list_wrong_answers = []
    for val in quiz_dict.values():
        list_wrong_answers.append(val)

    with open(p_csv, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        fields = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Correct Answer"]

        csv_writer.writerow(fields)
        for key, val in quiz_dict.items():
            # Liste wird so lange zufällig geordnet bis die richtige Antwort nicht in den ersten drei Stellen vorkommt
            while True:
                random.shuffle(list_wrong_answers)
                if val not in list_wrong_answers[0:3]:
                    break
            # Liste mit Antwortmöglichkeiten wird erstellt (1 richtige + 3 falsche)
            list_answers = [val, list_wrong_answers[0], list_wrong_answers[1], list_wrong_answers[2]]
            # Liste randomisiert, damit die richtige Antwort nicht immer auf 1 ist
            random.shuffle(list_answers)
            # Index der richtigen Antwort plus eins gespeichert
            right_answer = list_answers.index(val) + 1
            csv_writer.writerow([key, list_answers[0], list_answers[1], list_answers[2], list_answers[3], right_answer])

# Pfad zur csv-Datei
path_dir = os.path.dirname(__file__)
name_csv = "quiz_all_questions.csv"
path_csv = os.path.join(path_dir, name_csv)

# Funktionen ausführen
quiz_questions_dict = get_country_capital()
write_quiz_csv(path_csv, quiz_questions_dict)












