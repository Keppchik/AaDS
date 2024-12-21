# Лабораторная работа №7: Динамическое программирование №1

Студент ИТМО, Кретов Иван Алексеевич 466353
### Навигация

- [ ] [Задача 1 - Обмен монет](task1)
- [ ] [Задача 3 - Редакционное расстояние](task3)
- [ ] [Задача 5 - Наибольшая общая подпоследовательность трех последовательностей](task5)
- [ ] [Задача 7 - Шаблоны](task7)

## Описание
Лабораторная работа посвящена ознакомлению с такими понятиями, как множество, словари, хеш-таблицы и хеш-функции.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/keppchik/AaDS.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd AaDS
   ```
3. **Запуск всех задач**

   ```bash
   for script in lab7/*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```

## Тестирование
### Для запуска тестов выполните:
   ```bash
   export PYTHONPATH=$(pwd)
   pytest lab7
   ```