# Лабораторная работа №4: Стек, очередь, связанный список

Студент ИТМО, Кретов Иван Алексеевич 466353
## Вариант 10
### Навигация

- [ ] [Задача 2 - Очередь](task2)
- [ ] [Задача 3 - Скобочная последовательность. Версия 1](task3)
- [ ] [Задача 6 - Очерель с минимумом](task6)
- [ ] [Задача 10 - Поликлиника](task9)
- [ ] [Задача 10 - Очередь в пекарню](task10)
- [ ] [Задача 13 - Реализация стека, очереди и связанных списков](task13)

## Описание
Лабораторная работа посвящена разбору элементарных структур данных, таких как стек, очередь и связанный список.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/keppchik/AaDS.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd AaDS/lab3
   ```
3. **Запуск всех задач**

   Для terminal
   ```bash
   for script in lab*/*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```
   Для cmd
   ```bash
   set PYTHONPATH=%cd%
   for /f "delims=" %f in ('dir /s /b *.py ^| findstr "\\src\\"') do python "%f"
   ```
   Для PowerShell
   ```bash
   $env:PYTHONPATH = (Get-Location).Path
   Get-ChildItem -Recurse -Filter *.py -Path lab*/*/src | ForEach-Object { python $_.FullName }
   ```

## Тестирование
### Для запуска тестов выполните:

 Для terminal
   ```bash
   for script in lab*/*/tests/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```
   Для cmd
   ```bash
   set PYTHONPATH=%cd%
   for /f "delims=" %f in ('dir /s /b *.py ^| findstr "\\tests\\"') do python "%f"
   ```
   Для PowerShell
   ```bash
   $env:PYTHONPATH = (Get-Location).Path
   Get-ChildItem -Recurse -Filter *.py -Path lab*/*/tests | ForEach-Object { python $_.FullName }
   ```
