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
Enter a command: add Kate 0790909090
Contact Kate added.
Enter a command: add-birthday Kate 18.07.2000
Contact Kate updated.
Enter a command: birthdays
Kate celebrates 2025.07.18
Enter a command: add John 098787802 
Add me name and <value> please. Error: Phone number must contain exactly 10 digits
Enter a command: add John 0987878023
Contact John updated.
Enter a command: birthdays          
There is no birthday data for some contact. Error: 'NoneType' object has no attribute 'value'
Enter a command: add-birthday John 18.07.1998
Contact John updated.
Enter a command: birthdays
Kate celebrates 2025.07.18
John celebrates 2025.07.18
Enter a command: add Kate 0786765544
Contact Kate updated.
Enter a command: all                
Info about contact. name: Kate; phones: 0790909090, 0786765544
Info about contact. name: John; phones: 0987878023
Enter a command: exit
Good bye!