import csv
from collections import defaultdict


przedmioty = defaultdict(list)
data = []


with open('ocenylaura.csv') as plik:

    dane = csv.reader(plik, delimiter=',')
    header = next(dane)

    for linia in dane:
        przedmioty[linia[0]].append([float(linia[1]), int(linia[2])])


for przedmiot in przedmioty:

    iloczyn = 0
    iloraz = 0

    for ocena in przedmioty[przedmiot]:
        iloczyn += ocena[0]*ocena[1]
        iloraz += ocena[1]

    srednia = iloczyn/iloraz
    data.append(srednia)

    print(przedmiot+' = '+str(round(srednia, 1)) + " ocena po zaokrgleniu : " + str(round(srednia)))

ile = len(data)

max = 0
for x in data:
    max += x 

max = max / ile
print("\n\nSrednia semestralna = " + str(round(max,2)))

