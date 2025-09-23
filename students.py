import csv

# Хранилище студентов
students = {}

# --- Функции ---
# Добавить студента
def add_student():

    name = input("Введите имя: ")
    if name in students:
        print("Студент с таким именем уже есть.")
        return
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Возраст должен быть числом.")
        return
    grades_str = input("Введите оценки через пробел: ")
    try:
        grades = [int(x) for x in grades_str.split()]
    except ValueError:
        print("Оценки должны быть числами.")
        return
    students[name] = {"age": age, "grades": grades}
    print("Студент добавлен.")


# Показать всех студентов
def show_all():

    if not students:
        print("Список пуст.")
        return
    for name, info in students.items():
        print(f"{name}: возраст {info['age']}, оценки {info['grades']}")

# Найти студента по имени
def find_student():

    name = input("Введите имя для поиска: ")
    for key, value in students.items():
        if key == name:
            print(f"Найден: {key}, возраст {value['age']}, оценки {value['grades']}")
            break
    else:  # выполнится, если цикл завершился без break
        print("Студент не найден.")

# Удалить студента
def delete_student():

    name = input("Введите имя студента для удаления: ")
    if name in students:
        del students[name]
        print("Студент удалён.")
    else:
        print("Такого студента нет.")

# Добавить новую оценку студенту
def add_grade():
    
    name = input("Введите имя студента: ")
    if name not in students:
        print("Такого студента нет.")
        return
    try:
        grade = int(input("Введите новую оценку: "))
    except ValueError:
        print("Оценка должна быть числом.")
        return
    students[name]["grades"].append(grade)
    print("Оценка добавлена.")

# Вывести студентов старше определённого возраста
def show_older():
    
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Возраст должен быть числом.")
        return
    for name, info in students.items():
        if info["age"] > age:
            print(f"{name}: возраст {info['age']}, оценки {info['grades']}")

# Показать студентов с оценкой выше порога
def show_by_grade():
    
    try:
        threshold = int(input("Введите порог: "))
    except ValueError:
        print("Порог должен быть числом.")
        return
    for name, info in students.items():
        if any(g > threshold for g in info["grades"]):
            print(f"{name}: {info['grades']}")

# Экспортировать студентов в CSV
def export_csv():
    
    try:
        with open("students.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            for name, info in students.items():
                grades_str = ",".join(map(str, info["grades"]))
                writer.writerow([name, info["age"], grades_str])
    except Exception as e:
        print("Ошибка при сохранении:", e)
    else:
        print("Экспорт успешно завершён.")
    finally:
        print("Операция экспорта завершена.")  

# Импортировать студентов из CSV
def import_csv():
   
    try:
        with open("students.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                try:
                    name = row[0]
                    age = int(row[1])
                    grades = [int(x) for x in row[2].split(",")]
                    students[name] = {"age": age, "grades": grades}
                except Exception:
                    print("Ошибка чтения строки:", row)
    except FileNotFoundError:
        print("Файл students.csv не найден.")
    else:
        print("Импорт завершён.")

# --- Меню ---
def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента по имени")
        print("4. Удалить студента")
        print("5. Добавить новую оценку студенту")
        print("6. Список студентов старше возраста")
        print("7. Студенты с оценкой выше порога")
        print("8. Экспорт в CSV")
        print("9. Импорт из CSV")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            find_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            add_grade()
        elif choice == "6":
            show_older()
        elif choice == "7":
            show_by_grade()
        elif choice == "8":
            export_csv()
        elif choice == "9":
            import_csv()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# --- Запуск ---
menu()
