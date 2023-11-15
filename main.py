'''a = open('hello.txt', 'w')
a.write('Hello!!!')
a.close()'''

'''a = open('hello.txt', 'r')
print(a.read())
a.close()'''

'''with open('hello.txt', 'r') as b:
    print(b.read())'''

'''with open('hello.txt', 'w') as b:
    b.write('Another Love Ooo My Tears Can You Stone!!!')'''

'''for i in range(5):
    with open('hello.txt', 'a') as file:
        a = input()
        file.write(a + '\n')

with open('hello.txt', 'r') as file:
    print(file.read())'''

'''import os
os.mkdir(r'D:\folder')'''


'''a = 1000
while a > 0:
    print(a)
    a -= 7'''


'''https://github.com/IBRAGIMOV77/Shaxa.project.git'''

''''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 '''''


'''try:
    number = int(input('Введите число: '))
    print('Молодец:', number)
except:
    print('Куда буквы суёшь')
print('Конец')'''

'''try:
    number = int(input('Введите число: '))
    print('Молодец:', number)
except:
    print('Куда буквы суёшь')
finally:
    print('Твой блок завершен')
print('Конец')'''

'''def my_func(x, y):
    try:
        return x + y
    except:
        return ('None')

print(my_func('123', 123))'''


'''dict ={'Разиков':'Максим',
        'Барисов':'Генадий',
        'Алексеев':'Валодя',
}
def func(x):
    w = sorted(x.items())
    return w

print(func(dict))'''

'''a = [2,7,3,8,1,9,4,6,5]
print(sorted(a))

a.sort()
print(a)

print(type(a))'''


'''class Car:
    name = None
    weight = None
    def grow(self, x):
        self.weight += x
a = Car()
b = Car()

a.weight = 100
b.weight = 100

a.grow(30)
b.grow(50)

print(a.weight)
print(b.weight)'''

'''class Car:
    engine_on = False
    color = None
    type = None
    eng_volume = 0
    wheels = 0
    doors = 0
    interior = None
    headlights = None
    disks = None
    petrol = 0
    windows = 0
    automatic = None
    capacity = 0
    exhaust = 0

    def __init__(self, a,b,c,d,e,f,g,h,i,j,k,l,m,n):
        self.engine_on = a
        self. color = b
        self.type = c
        self.eng_volume = d
        self.wheels = e
        self.doors = f
        self.interior = g
        self.headlights = h
        self.disks = i
        self.petrol =j
        self.windows = k
        self.automatic = l
        self.capacity = m
        self.exhaust = n
        
    def start_engine(self):
        self.engine_on = True
    def drive_to(self, city, road):
        if self.engine_on:
            print('Едем в город.'.format(city))
        else:
            print('Машина не заведена, никуда н еедем')

c = Car(False, 'blue', 'sedan', 5.5, 4, 4, 'Alikantara', 'Yelow', 21, 100, 4, 'Automatic', 5, 2)
c.start_engine()
c.drive_to('Самарканд')'''

'''class Dog:
    def __init__(self,name,age,sleep = False):
        self.name = name
        self.age = age
        self.sleep = sleep
    def asleep(self):
        self.sleep = True
    def wake_up(self):
        self.sleep = False
    def bark(self):
        if self.sleep == True:
            print('Dog is sleeping')
        else:
            print('GAW GAW')

dog = Dog('Jocker', 56)
dog.bark()
dog.asleep()
dog.bark()
dog.wake_up()'''


'''def func(x, y):
    if type(x) == list:
        return x[y]
    else:
        raise VallueError
a = [1,2,3,4,5]
b = {'key': 'value'}
c = 'Hello'
print(func(a, 0))
print(func(b, 'key'))
print(func(c, 3))'''


'''from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimetr(self):
        return 2 * pi * self.radius
class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimetr(self):
        return self.side * 4

class Rectangle:
    def __init__(self, asize, bsize):
        self.asize = asize
        self.bsize = bsize
    def area(self):
        return self.asize *  self.bsize
    def perimetr(self):
        return (self.asize + self.bsize) * 2

def print_shape_info(shape):
    print('Area = {}, Perimetr = {}'
        .format(shape.area(),
        shape.perimetr()
    ))

circle = Circle(int(input('Круг: ')))
square = Square(int(input('Квадрат: ')))
rectangle = Rectangle(int(input('Ваше значенияa a:')), int(input('Ваше значения b:')))
print_shape_info(square)
print_shape_info(circle)
print_shape_info(rectangle)'''

'''class Cat:
    def __init__(self, name, age, claw_length, sleep = False):
        self.name = name
        self.age = age
        self.claw_length = claw_length
        self.sleep = sleep
    def meow(self):
        if self.sleep == True:
            print('Cat is sleeping')
        else:
            print('GAW GAW')

class Dog:
    def __init__(self, name, age, toy,sleep = False):
        self.name = name
        self.age = age
        self.toy = toy
        self.sleep = sleep
    def bark(self):
        if self.sleep == True:
            print('Dog is sleeping')
        else:
            print('MEOW MEOW')

cat = Cat
cat.meow

dog = Dog
dog.bark'''

#Инкапсюляция
#Полиморфизм
#Наследование
#Абстракция


'''class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input('ctoroni' + str(i+1)+':')) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print('storona', i + 1, '--', self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('Oтвет: ')'''



'''class Machine:
    def __init__(self, name, switch, refuel, open_door):
        self.name = name
        self.switch = switch
        self.refuel = refuel
        self.open_door = open_door

    def engine(self):
        if self.switch == False:
            print('Заводите Машину')
        else:
            print('Можем ехать')

    def stop(self):
        if self.refuel == False:
            print('Заправить её')
        else:
            print('Заправдено')

    def door(self):
        if self.open_door == False:
            print('Закройте дверь а то не поедем')
        else:
            print('Поехали')

class Sedan(Machine):
    def __init__(self, name, switch, refuel, open_door, tire):
        super().__init__(name, switch, refuel, open_door)
        self.tire = tire

    def type_of_car(self):
        print('Sedan {}'.format(self.name))
class Bus(Machine):
    def __init__(self, name, switch, refuel, open_door, seats):
        super().__init__(name, switch, refuel, open_door)
        self.seats = seats
    def long_car(self):
        print('Bus {}'.format(self.name))

sedan = Sedan('BMW',False, False, False, 4)
bus = Bus('Volvo',True, True, True, 30)
sedan.engine()
bus.engine()
sedan.stop()
bus.stop()
sedan.door()
bus.door()
sedan.type_of_car()
bus.long_car()
print('Количество шин в BMW:',sedan.tire)
print('Количество пассажиров в Volvo:',bus.seats)'''


#Баззовый класс
#Производный класс




