#Заднания по set

#Удаление дубликатов
numbers = [2,3,4,2,3,2,3,4,2,3]
print(set(numbers))

#Общие элементы 
n1 = {1,2,3,2,3,2}
n2 = {1,2,3,1,4,2}
print(n1 & n2)

#Разность множеств
num1 = {1,2,3,10,11,12}
num2 = {1,2,3,4,5,6,7}
print(num1 - num2)

#Объединение множеств
number1 = {1,2,3,4,5}
number2 = {5,6,7,8,9}
number3 = {9,10,11,12,13}
print(number1 | number2 | number3)

#Частота слов
stroka = ["Hi,", "my", "name", "is", "Uson.", "Uson", "ye", "thats", "my", "name", "is"]
print(set(stroka))

#Задание по Frozenset
frozen = input("Введите строку: ")
print(frozenset(frozen))

#Пересечение множеств
froz1 = frozenset("hello, im fine")
froz2 = frozenset("hi, hello, how are you")
print(froz1 & froz2)

#Хешируемость frozenset
dict2 = {
    "frozenset" : "множество",
    frozenset : "так использовать?"
}
print(dict2)

#Разница frozenset
fr1 = frozenset("hihi im fine are you fine too")
fr2 = frozenset("hihi")
print(fr1 - fr2)

#Преобразование set → frozenset
se1 = {2,3,2,3,2,3,2,3}
print(frozenset(se1))

#Задания по dict (словарь)
#Подсчет символов
word = "just a random workds"  
char_count = {}  

for char in word:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  

print(char_count)

#Словарь квадратов
dicti1 = {
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25,
    6 : 36,
    7 : 49,
    8 : 64,
    9 : 81,
    10 : 100
}
print(dicti1)

# Обратный словарь
text = "hello world"  
positions = {}  

for idx, char1 in enumerate(text):
    if char1 in positions:
        positions[char1].append(idx)  
    else:
        positions[char1] = [idx]  

print(positions)

# Объединение словарей
dicti1 = {
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25,
    6 : 36,
    7 : 49,
    8 : 64,
    9 : 81,
    10 : 100
}
dicti2 = {
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25,
    6 : 36,
    7 : 49,
    8 : 64,
    9 : 81,
    10 : 100
}
for key, value in dicti2.items():
    if key in dicti1:
        dicti1[key] += value  
    else:
        dicti1[key] = value

print(dicti1)

