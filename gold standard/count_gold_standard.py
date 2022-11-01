import csv

fileReader = open('Multimodal_Gold_Standard.csv', 'r')
reader = csv.DictReader(fileReader)

labels = ["Amore", "Anticipazione", "Disgusto", "Fiducia", "Gioia", "Paura", "Rabbia", "Sorpresa", "Tristezza",
          "Neutro", "Ironia", "Sarcasmo", "Offensivita", "Hate speech", "Contenitore", "Contenuto", "Incomprensibile",
          "Citazione", "Additiva", "Parallela", "Divergente"]

countDictionary = {}
for label in labels:
    countDictionary[label] = {'count': 0}

for row in reader:
    countDictionary[row['tag_name']]['count'] += 1

print(countDictionary)
