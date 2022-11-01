import csv

dictionary = {}
fileReader = open('Instagram_Rai_annotation_all.csv', 'r')
reader = csv.DictReader(fileReader)

fileWriter = open('Multimodal_Gold_Standard.csv', "w", newline='', encoding='utf-8')
writer = csv.writer(fileWriter)

writer.writerow(['uri', 'tag_name'])

for row in reader:
    if row['uri'] not in dictionary:
        dictionary[row['uri']] = {'labels': []}
    dictionary[row['uri']]['labels'].append(row['tag_name'])

for key_tweet_id, value in dictionary.items():
    labelDict = {}
    for label in value['labels']:
        if label not in labelDict:
            labelDict[label] = {'count': 1}
        else:
            labelDict[label]['count'] += 1

    for key_label_name, sum in labelDict.items():
        if sum['count'] > 1:
            toWrite = [key_tweet_id, key_label_name]
            writer.writerow(toWrite)
