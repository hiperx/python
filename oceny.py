#! /usr/bin/env python3
import csv

data = []

with open('lista.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    for row in reader:
        if row[3] not in reader:
            przedmiot={"nazwa": row[3], "ocena": [], "waga": [], "srednia": 0}
            data.append(przedmiot)
        print(data)
        
print(type(data))
print(data)

with open('lista.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)


for i in data:
    srednia = 0.0
    ocenka_sum = 0.0
    sumka_wag = 0.0
    #print("Przedmiot : "+i)
    print("Srnednia: "+str(srednia))
    print("\n\n")

   for row in reader:
        print("row : ",row)
        if  i == row[3]:
            ocena = float(row[1])
            waga = float(row[2])
            ocenka_sum = float(ocenka_sum) + (ocena*waga)
            sumka_wag = sumka_wag + waga
            print("ocena :"+ str(ocenka_sum)+ " sumka_wag : "+ str(sumka_wag))


srednia = ocenka_sum / sumka_wag
print("przedmiot : "+row[3]+"srednia : "+ str(round(srednia, 2)))
print("row : ", row)


