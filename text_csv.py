answers = [{'key': 'privet', 'answer': 'i tebe privet'},
          {'key': 'kak dela', 'answer': 'kuchshe vseh'},
          {'key': 'poka', 'answer': 'uvidimsya'}]


import csv

with open('answers.csv', 'w', encoding='utf-8') as f:
    fields = ['key', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    print(writer)
    for user in answers:
        writer.writerow(user)
    print(writer)

# вопрос кодировки,все делает, но выдает абру кадабру
