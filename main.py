import matplotlib.pyplot as plt
import csv
import functools

with open('data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  header = next(reader)
  data = []
  
  for row in reader:
    iterable = zip(header, row)
    countryDict = {key : value for key, value in iterable}
    data.append(countryDict)
    
Benignos = list(filter(lambda item: item['diagnosis'] == 'B',data))
NumBenignos = int((len(Benignos)))

Malignos = list(filter(lambda item: item['diagnosis'] == 'M',data))
NumMalignos = int((len(Malignos)))

Identificacion = input('digite su numero de id =>')
result = list(filter(lambda item: item['id'] == Identificacion,data))
print("el resultado de su diagnostico es:   ", result[0]['diagnosis'])

#GRAFICA 
labels = ['Numero_Benignos', 'Numero_Malignos']
values = [NumBenignos, NumMalignos]

fig, ax = plt.subplots()
ax.pie(values, labels=labels)
ax.axis('equal')
plt.show()


