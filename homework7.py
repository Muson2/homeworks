#1 задание
square = lambda a: a*a
print(square(5))

#2 задание
names = ["иван", "мария", "алексей", "ольга"]
name = list(map(lambda a: a.capitalize(), names))
print(name)

#3 задание
def sum_all(*args): 
    return sum(args)
print(sum_all(1,2,3,4,5))
print(sum_all(10, 20))

#4 задание
def print_person_info(**kwargs):
    for i, v in kwargs.items():
        print(f"{i}: {v}")

print_person_info(name="Иван", age=25, city="Москва")

#5 задание
def full_info(*args, **kwargs):
    role = ["Роль", "Дополнительные данные"]
    
    print(f"{role[0]}: {args[0]}")
    print(f"{role[1]}: {args[1], args[2]}")
       
    print("Дополнительные параметры:")
    for i, v in kwargs.items():
        print(f"{i}: {v}")

full_info("Разработчик", "Python", "Django", name="Иван", experience=5)