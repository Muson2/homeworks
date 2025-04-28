class Transport:
    def move(self):
        print("Транспорт начал движение")

class Car(Transport):
    def move(self):
        print("Автомобиль едет по дороге")
        return super().move()
    def _speed(self, speed):
        self.speed = speed
    def set_speed(self):
        spd = input("Ввдите скорость транспорта: ")
        self.speed = spd
    def get_speed(self):
        print(f"Текущая скорость {self.speed}")

class Bicycle(Transport):
    def move(self):
        print("Велосипед катиться по велодорожке ")
        return super().move()
    def _speed(self, speed):
        self.speed = speed
    def set_speed(self):
        spd = input("Ввдите скорость транспорта: ")
        self.speed = spd
    def get_speed(self):
        print(f"Текущая скорость {self.speed}")

transport_list = [Car(), Bicycle()]
transport_list[0].set_speed()
transport_list[0].get_speed()
transport_list[0].move()

transport_list[1].set_speed()
transport_list[1].get_speed()
transport_list[1].move()