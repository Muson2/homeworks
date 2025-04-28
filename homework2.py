#1 задание
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
print("Привет, " + name, surname)

#2 задание 

birthdate = int(input("Введите год вашего рождения: "))
current_year = 2025
age = (current_year - birthdate)
print("Вам,", age, "лет")

#3 задание

fav_num = float(input("Введите ваше любимое число: "))
num = (fav_num * 3.14)
print ("Ваше любимое число умноженное на 3.14: ", num)

#4 задание

vampire = input("Вы боитесь солнца?(Да/Нет) ")
if vampire == "Да":
    print("Вы вампир!")
elif vampire == "Нет":
    print("Ты человек")

#5 задание

name1 = input("Введите ваше имя: ")
fav_num1 = input("Введите ваше любимое число: ")
random_pass = (name1 + fav_num1)
print("Вам идеально подходит пароль: ", random_pass)

#6 задание

name2 = input("Введите ваше имя: ")
aname = name2.count ("а")
print ("В вашем имени:", aname, "буквы 'а'")