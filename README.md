# Практика по Алгоритмам и Cтруктурам Данных ИТМО 

## Студент ИТМО,  Кретов Иван Алексеевич 466353

### Навигация

- [ ] [Лабораторная №0. Введение](lab0)
- [ ] [Лабораторная №1. Сортировка вставками, выбором, пузырьковая](lab1)
- [ ] [Лабораторная №2. Сортировка слиянием. Метод декомпозиции](lab2)
- [ ] [Лабораторная №3. Быстрая сортировка, сортировка за линейное время](lab3)
- [ ] [Лабораторная работа №4: Стек, очередь, связанный список](lab4)

### Цели и задачи

- Изучить основные функции и методы python
- Научиться создавать алгоритмы
- Освоить работу с структурами данных
- Понять основы работы с Git

### Технологии и инструменты

- **Git** — система контроля версий
- **GitHub** — платформа для хостинга репозиториев
- **Python** — язык программирования
- **PyCharm** - среда разработки для написания кода 

### Инструкция по запуску

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/keppchik/AaDS.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd AaDS
   ```
3. **Запуск всех лабараторных**

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


4. **Запуск всех тестов**

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


