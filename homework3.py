# 1 задание

time = int(input("Ведите время(от 0 до 23): "))

if time <= 5 and time >= 0:
    print("Сейчас ночь")
elif time <= 12 and time >= 6:
    print("Сейчас утро")
elif time <= 18 and time >= 13:
    print("Сейчас день")
elif time <= 23 and time >= 19:
    print("Сейчас вечер")
else:
    print("Введите число от 0 до 23, вы ввели время неправильно")

# 2 задание

year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
    print("Год который вы ввели является високосным")
else :
    print("Год который вы ввели не является високосным")

# 3 задание

num = int(input("Введите число любое: "))
if num <0:
    print("Ваше число отрицательное")
elif num == 0:
    print("Ваше число это 0")
elif num >0:
    print("Ваше число положительное")

# 4 задание

grade = int(input("Введите ваши баллы(оценку): "))

if grade >= 0 and grade <= 60:
    print("Неудовлетворительно (F)")
elif grade >= 61 and grade <= 69:
    print("Плохо (D)")
elif grade >= 70 and grade <= 79:
    print("Удовлетворительно (C)")
elif grade >= 80 and grade <= 89:
    print("Хорошо (B)")
elif grade >= 90 and grade <= 100:
    print("Отлично (A)")
else:
    print("Ошибка! Оцнека должна быть от 0 до 100")


#5 задание
vyborsydby = input("Вы стоите на развилке. Куда пойдете? (налево, направо, прямо): ")
if "налево" in vyborsydby:
    print("Вы нашли сундук с золотом") 
elif "направо" in vyborsydby:
    print("Вы встретили дракона! Спасайся!") 
elif "прямо" in vyborsydby:
    print("Вы попали в лабиринт. Найдите выход!") 
else:
    print("Вы не сделали выбор, остались на месте")
    