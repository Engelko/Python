HELP = '''Команды
● help - напечатать справку по программе.
● add - добавить задачу в список (название задачи запрашиваем у пользователя).
● show - напечатать все добавленные задачи'''
tasks = []
today = []
tomorrow = []
other = []


while True:
  command = input("Введите команду:")
  if command == "help":
    print(HELP)
  elif command == "add":
    task = input("Введите задачу: ")
    date = input("Введите дату: ")
    tasks.append(task)
    if date == "Сегодня":
      today.append(task)
    elif date == "Завтра":
      tomorrow.append(task)
    else:
      other.append(task) 
    print("Задача",task, "добавлена на", date , "!")
  elif command == "show":
    print(tasks)
  elif command == "today":
    print("На Сегодня у наc", today)
  elif command == "tomorrow":
    print("На Завтра у наc", tomorrow)
  elif command == "other":
    print("В перспективе у наc", other)
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная команда! Введите help для списка доступных команд")
