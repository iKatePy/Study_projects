#counting words
# Define a set of stop words to exclude
'''stop_words = {'just', 'are', 'it', 'of', 'is', 'and', 'the', 'a', 'to', 'in', 'for', 'on', 'with'}

with open('file1.txt', 'r') as file:
  lines = file.readlines()
  count_all = 0
  unique_words = set()  # Use a set to store unique words

  for line in lines:
    words = line.split()  # Split the line into words
    for word in words:
      if word not in stop_words:
        count_all += 1  # Increment total word count by the number of words in the line

    # Filter out stop words and add remaining words to the unique_words set
    filtered_words = [word.strip().lower() for word in words if word.strip().lower() not in stop_words]
    unique_words.update(filtered_words)  # Add filtered words to the set

  count_unique = len(unique_words)  # The number of unique words is the size of the set
  print(words)
  print(f"Общее количество слов: {count_all}")
  print(f"Количество уникальных слов: {count_unique}")
*************************************************
with open('logs.txt', 'r') as file:
    content = file.readlines()
    error_log = list()
    for line in content:
        if line.startswith('ERROR:'):
            error_log.append(line)
    print('\n'.join(error_log))
*******************************************
def temp1(file1):
    with open(file1, 'r') as file:
        content = file.readlines()
        return content
c1 = temp1('file1.txt')
c2 = temp1('logs.txt')
c3 = temp1('my_first_file.txt')
print(c1, c2, c3, sep = '\n---\n')
****************************
import csv
sales_summary = {}
with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        amount = int(row[1])
        if product in sales_summary:
            sales_summary[product] += amount
        else:
            sales_summary[product] = amount
    print(sales_summary)
with open('contacts.txt', 'r') as file:
    content = file.readlines()
    name = input("Pls give me a name:\n")
    for line in content:
        if line.startswith(name):
            print(line)'''
'''import sys #checking what sys do I have

print(sys.executable)
x = 3
y = 10
z = -1
if (x > 2 or y < 5) and not (z >= 0 and y > 8):
    print("Condition met")
else:
    print("Condition not met")'''
import requests
response = requests.get('https://example.com')
print(response.text)

