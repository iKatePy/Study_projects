# prfjdhb
# fdjfhndkjf
# dfdd  ctrl/
'''import sys

x = 10
y = 3.14
z = "Hello, world!"

print("Размер переменной x (int):", sys.getsizeof(x), "байт")
print("Размер переменной y (float):", sys.getsizeof(y), "байт")
print("Размер переменной z (str):", sys.getsizeof(z), "байт")


file = open('my_first_file.txt', 'w')
file.write("I'll be back\nJustice delivered\nWe zooming")
with open('my_first_file.txt', 'r') as file:
    content = file.read()
    print(content)
try:
    num = int(input('input any number:\n'))
    result = 1/num
    print(result)
except ZeroDivisionError:
    print("plz pick not null")
except ValueError:
    print('plz pick a number')'''
import sys

'''import os
current_dir = os.getcwd()
print(f"my directory is {current_dir}")

file = open('my_first_file.txt', 'r')
line = file.readline()
while line:
    print(line.strip())  # strip() убирает лишние пробелы и символы перевода строки
    line = file.readline()
file.close()
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open('output.txt', 'w')
file.writelines(lines)
file.close()

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)'''
import sys
a = sys.platform
print(a)