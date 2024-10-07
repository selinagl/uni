import csv

path_csv = r"C:\Users\selin\OneDrive\Desktop\Uni Daten\Modul 5\Aufgabe 2\quiz_questions.csv"
liste_fragen = []

with open(path_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        frage = row[0], row[1:5], row[5]
        liste_fragen.append(frage)
