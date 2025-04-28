# # Простая сумма, первая часть
# total_sum = 0


# for i in range(5):
#     number = float(input(f"Введите число {i + 1}: "))  
#     total_sum += number  

# print(f"Сумма введенных чисел: {total_sum}")

# #Четные числа
# num = 0


# while num <= 20:
#     if num % 2 == 0:  
#         print(num)  
#     num += 1 

# #Таблица умножения
# n = int(input("Введите число для вывода таблицы умножения: "))


# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")


# #Сумма элементов списка
# numbers = [2, 4, 6, 8, 10]


# total = 0

# for number1 in numbers:
#     total += number1  

# print("Сумма всех элементов списка:", total)


# #Обратный порядок
# values = [1, 2, 3, 4, 5]


# for val in reversed(values):
#     print(val)

# #Работа со списком 2 часть
# import random


# random_list = [random.randint(1, 100) for _ in range(5)]
# print("Исходный список:", random_list)

# random_list.pop()

# new_number = random.randint(1, 100)
# random_list.insert(0, new_number)


# print("Обновленный список:", random_list)


# #Работа с кортежем
# fruits = ("яблоко", "банан", "груша", "апельсин", "виноград")
# print("Исходный кортеж:", fruits, "нельзя менять значения в кортеже")

# # fruits[1] = "ананас"  выйдет ошибка



# #Минимум и максимум
# data = [34, 67, 12, 89, 45]


# highest = data[0]
# lowest = data[0]

# for value in data:
#     if value > highest:
#         highest = value
#     if value < lowest:
#         lowest = value


# print("Самое большое число:", highest)
# print("Самое маленькое число:", lowest)


# #Удаление дубликатов 3 часть

# original_list = [1, 2, 2, 3, 4, 4, 5]


# unique_list = []


# for item in original_list:
#     if item not in unique_list:  
#         unique_list.append(item)  


# print("Список без дубликатов:", unique_list)


# #Числа Фибоначчи

# count = int(input("Введите количество чисел последовательности Фибоначчи: "))


# first, second = 0, 1


# for _ in range(count):
#     print(first, end=" ") 
#     first, second = second, first + second  


n = int(input("Введите число больше 5: "))
first, second = 0, 1
for n2 in range(n):
    sum = second, first + second  

sum = list(sum)
sum = tuple(sum)

print(sum)
total = 0

for number1 in sum:
    total += number1  

print("Сумма всех элементов списка:", total)
