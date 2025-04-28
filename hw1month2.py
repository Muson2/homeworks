#задание 1 класс Person
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city 

    def introduce(self):
        print(f'python \nКопироватьРедактировать \nПривет! Меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}')


person = Person("Uson", 18, "Osh")
person1 = Person("Aktan", 17, "Bishkek")
person2 = Person("Akylay", 19, "Issyk-Kol")
person.introduce()
person1.introduce()
person2.introduce()

#задание 2 класс car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"python\nКопироватьРедактировать\nАвтомобиль: {self.brand} {self.model}, {self.year} года выпуска.")
    def is_old(self):
        if self.year > 10:
            print(True)
        else:
            print(False)

car = Car("ferrari", "cool", 11)
car1 = Car("bugatti", "not cool", 5)

car.info()
car.is_old()
car1.info()
car1.is_old()

#3 задание класс банк аккаунт

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f"Ваш счет пополнен на {amount}, ваш нынешний баланс {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"С вашего счета снято {amount}, ваш нынешний баланс {self.balance}")

    def show_balance(self):
        print(f"Ваш текущий баланс {self.balance}")
    
bankacc = BankAccount("Uson", 0)
bankacc.deposit(10000)
bankacc.withdraw(1000)
bankacc.show_balance()