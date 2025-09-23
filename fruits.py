# Спросить у пользователя строку с фруктами через запятую
fruits = input("Введите фрукты через запятую: ")

# В список и убираем пробелы
fruits_list = [f.strip() for f in fruits.split(",")]

# все фрукты начинались с заглавной буквы
fruits_list = [f.capitalize() for f in fruits_list]

# Убираем повторы с set
del_fruits = set(fruits_list)

# В алфавитном порядке
sorted_fruits = sorted(del_fruits)
print("\nВ алфавитном порядке:", sorted_fruits)

# Словарь сколько раз встречался
fruit_count = {}
for f in fruits_list:
    fruit_count[f] = fruit_count.get(f, 0) + 1
print("\nСловарь сколько раз встречался:", fruit_count)

# Самый популярный фрукт
most_popular = max(fruit_count, key=fruit_count.get)
print("Самый популярный фрукт:", most_popular)

# Кортеж из уникальных фруктов
fruits_kortech = tuple(del_fruits)
print("\nКортеж фруктов:", fruits_kortech)

# Проверка на Banana, Mango, Pineapple
check_fruits = ["Banana", "Mango", "Pineapple"]
for cf in check_fruits:
    if cf in del_fruits:
        print(cf, "есть в списке")
    else:
        print(cf, "нет в списке")        

# Вывод N фруктов
N = int(input("\nВведите число N: "))
print("Первые", N, "фруктов в алфавитном порядке:", sorted_fruits[:N])
