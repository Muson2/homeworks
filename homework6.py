#Банк: Снятие денег
def withdraw_money(balance, amount):
    try:
        balance = int(input("Введите баланс: "))
        amount = int(input("Введите сумму снятия: "))
        if balance < amount:
            raise ValueError ("Недостаточно средств/Некорректная сумма")
        if balance >= amount:
            new_balance = (balance - amount)
            print(f"Ваш оставшийся балаланс: {new_balance}")
    except ValueError as a:
        print(f"Ошибка! {a}")
withdraw_money(0, 0)

#Генератор паролей
import random
import string
def generate_password(lenght):
    try:
        if lenght > 6:
            password = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(lenght)])
            print("Ваш пароль:", password)
        elif lenght < 6:
            raise ValueError("Пароль слишком короткий")
    except ValueError as b:
        print(f"Ошибка! {b}")

generate_password(4)
generate_password(8)

#Конвертер валют
def convert_currency(amount, rate):
    try:
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        elif amount > 0:
            sum = amount * rate
            print(f"{sum} рублей")
    except ValueError as c:
        print(f"Ошибка! {c}")
    
convert_currency(100, 87)
convert_currency(-5, 87)

#Проверка списка на числа
def validate_numbers(numbers = []):
    try:
        if all(isinstance(x, (int, float)) for x in numbers):
            print(numbers)
        else:
            raise ValueError("Список содержит не числовые значения!")
    except ValueError as d:
        print(f"Ошибка! {d}")

validate_numbers([1,2,3,4])
validate_numbers([1,"abc",3])

#Конвертер температуры
def convert_temperature(temp, scale):
    try:
        if scale == "C":
            print(temp * 9/5 + 32)
        elif scale == "F":
            print((temp - 32) * 5/9)
        else:
            raise ValueError("Неккоректная шкала температуры")
    except ValueError as e:
        print(f"ОШибка! {e}")

convert_temperature(100, "C")
convert_temperature(32, "F")
convert_temperature(25, "X")

#Умный банк
def registration():
    name = input("Добро пожаловать в банк! Введите ваше имя: ")

def vybor_deystviya():
    registration()
    try:
        schet = int(input("Введите ваш баланс: "))
        while True:
            print("""Выберите действие:
1: Проверить баланс
2. Пополнить счет
3. Снять деньги
4. Перевести деньги
5. Выйти
""")
            vybor = input("Введите номер операции: ")
            if vybor == "1":
                print("Ваш баланс", schet)
            elif vybor == "2":
                schetDobavit = int(input("Введите сумму для пополнения: "))
                if schetDobavit < 0:
                    raise ZeroDivisionError("Нельзя пополнить счет отрицательной суммой")
                else:
                    schet = schetDobavit + schet
                    print("Ваш баланс", schet)
            elif vybor == "3":
                schetSnat = int(input("Выберите сумму для снятия: "))
                if schetSnat > schet:
                    raise ValueError("Недостаточно средств!")
                else:
                    schet = schet - schetSnat
                    print(f"Вы сняли {schetSnat}. У вас осталось {schet} сом")
            elif vybor == "4":
                schetPerevod = int(input("Выберите сумму для перевода: "))
                perevodChel = input("Введите имя человека к которому нужно перевести: ")
                if schetPerevod > schet:
                    raise ValueError("Недостаточно средств!")
                else:
                    schet = schet - schetPerevod
                    print(f"Вы перевли {schetPerevod} сомов {perevodChel}. У вас осталось {schet} сом")
            elif vybor == "5":
                print("Спасибо за использование банка! До свидания!")
                break
            else:
                print("Введите цифру от 1 до 5!")
    except ZeroDivisionError as q:
        print(f"Ошбка! {q}")
    except ValueError as w:
        print(w)

vybor_deystviya()
