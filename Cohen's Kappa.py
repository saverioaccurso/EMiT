import pandas
import collections
from sklearn.metrics import cohen_kappa_score

Instagram_annotation = pandas.read_csv("Instagram-Rai-annotation-both.csv")

Instagram_annotation_Saverio = Instagram_annotation.loc[Instagram_annotation['email'] == "saverio.accurso@edu.unito.it"]
Instagram_annotation_Daniel = Instagram_annotation.loc[Instagram_annotation['email'] == "daniel.russo474@edu.unito.it"]

first_array_uris = []
second_array_uris = []
first_array = []
second_array = []
first_unique = []
second_unique = []

for row in Instagram_annotation_Saverio.itertuples():
    if getattr(row, 'tag_name') == "Parallela":
        first_array.append([getattr(row, 'uri'), 1])
    else:
        first_array.append([getattr(row, 'uri'), 0])
    first_array_uris.append(getattr(row, 'uri'))

first_array_uris = dict.fromkeys(first_array_uris)
first_array_uris = collections.OrderedDict(sorted(first_array_uris.items()))

for item in first_array:
    if item[1] == 1:
        first_array_uris[item[0]] = 1

for elem in first_array_uris:
    if first_array_uris[elem] == 1:
        first_unique.append(1)
    else:
        first_unique.append(0)

for row in Instagram_annotation_Daniel.itertuples():
    if getattr(row, 'tag_name') == "Parallela":
        second_array.append([getattr(row, 'uri'), 1])
    else:
        second_array.append([getattr(row, 'uri'), 0])
    second_array_uris.append(getattr(row, 'uri'))

second_array_uris = dict.fromkeys(second_array_uris)
second_array_uris = collections.OrderedDict(sorted(second_array_uris.items()))

for item in second_array:
    if item[1] == 1:
        second_array_uris[item[0]] = 1

for elem in second_array_uris:
    if second_array_uris[elem] == 1:
        second_unique.append(1)
    else:
        second_unique.append(0)

print(round(cohen_kappa_score(first_unique, second_unique), 2))
