class Venicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Бренд - {self.brand}, Модель - {self.model}, Год - {self.year}")

    def start_engine(self):
        print("Двигатель заведен")

class Car(Venicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    def info(self):
        print(f"Бренд - {self.brand}, Модель - {self.model}, Год - {self.year}, количество дверей - {self.doors}")

class Byke(Venicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type
    def info(self):
        print(f"Бренд - {self.brand}, Модель - {self.model}, Год - {self.year}, Тип мотоцикла - {self.type}")


car = Car("Toyota", "Camri", 2000, 4)
byke = Byke("Duccatti", "Newest", 2025, "Двух колестный")

car.info()
byke.info()
car.start_engine()
byke.start_engine()