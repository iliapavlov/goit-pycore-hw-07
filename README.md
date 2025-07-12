# 📇 Python Core Homework topic 10

Це навчальний проєкт, створений у процесі вивчення Python, використанням елементів ООП, магічних методів, та пройденого раніше матеріалу з обробки помилок за допомогою декораторів, роботи з CLI

## ▶️ Використання і перевірка

Скачай репозиторій, перейди в його папку і виконай:
```bash
python main.py
```
Приблизна робота з ботом зображена нижче:
```bash
Welcome to the assistant bot!
Enter a command: add Lola          
Add me name and <value> please. Error: not enough values to unpack (expected at least 2, got 1)
Enter a command: add Lola 0989889888
Contact Lola added.
Enter a command: add-birthday Lola 17.07.2000
Contact Lola updated.
Enter a command: birthdays
Lola celebrates 2025.07.17
Enter a command: add Kate 0989889885
Contact Kate added.
Enter a command: add-birthday Kate 16.07.2000
Contact Kate updated.
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Enter a command: add Fawn 0790909090
Contact Fawn added.
Enter a command: birthdays
There is no birthday data for some contact. Error: 'NoneType' object has no attribute 'value'
Enter a command: add Fawn 13.07.1990
Add me name and <value> please. Error: Phone number must contain exactly 10 digits
Enter a command: all                
Info about contact. name: Lola; phones: 0989889888
Info about contact. name: Kate; phones: 0989889885
Info about contact. name: Fawn; phones: 0790909090
Enter a command: add-birthday Fawn 13.07.2000
Contact Fawn updated.
Enter a command: all
Info about contact. name: Lola; phones: 0989889888
Info about contact. name: Kate; phones: 0989889885
Info about contact. name: Fawn; phones: 0790909090
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Info about contact. name: Fawn; phones: 0790909090
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Enter a command: delete Fawn
Contact 'Fawn' has been deleted
Info about contact. name: Fawn; phones: 0790909090
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Enter a command: delete Fawn
Info about contact. name: Fawn; phones: 0790909090
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Kate celebrates 2025.07.16
Fawn celebrates 2025.07.14
Fawn celebrates 2025.07.14
Enter a command: delete Fawn
Enter a command: delete Fawn
Contact 'Fawn' has been deleted
Enter a command: birthdays
Lola celebrates 2025.07.17
Kate celebrates 2025.07.16
Enter a command: all
Info about contact. name: Lola; phones: 0989889888
Info about contact. name: Kate; phones: 0989889885
Enter a command: exit
Good bye!