from statsmodels.stats.inter_rater import fleiss_kappa
# riferimento bibliografico: Fleiss, Joseph L. 1971. “Measuring Nominal Scale Agreement among Many Raters.” Psychological Bulletin 76 (5): 378-82. https://doi.org/10.1037/h0031619.
import csv

dictionary = {}

file_comments = open('Commenti_Rai_annotation_all.csv', 'r')
reader = csv.DictReader(file_comments)

# file_subcomments = open('Commenti_Rai_annotation_subset.csv', 'r')
# reader = csv.DictReader(file_subcomments)

# file_multimodal = open('Instagram_Rai_annotation_all.csv', 'r')
# reader = csv.DictReader(file_multimodal)

for row in reader:
    if row['uri'] not in dictionary:
        dictionary[row['uri']] = {'labels': []}
    dictionary[row['uri']]['labels'].append(row['tag_name'])

table = []

for key_tweet_id, value in dictionary.items():
    labels = [0, 0]
    for label in value['labels']:
        if label == "Amore":
            labels[0] += 1

    labels = [labels[0], 3 - labels[0]]
    print(value['labels'], labels)
    table.append(labels)

print(round(fleiss_kappa(table), 2))
