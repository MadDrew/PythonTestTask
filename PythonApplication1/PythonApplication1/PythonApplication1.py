import random
#       ПЕРВОЕ ЗАДАНИЕ
#Есть два списка разной длины. В первом содержатся ключи, а во втором значения. 
#Напишите функцию, которая создаёт из этих ключей и значений словарь. 
#Если ключу не хватило значения, в словаре должно быть значение None. 
#Значения, которым не хватило ключей, нужно игнорировать
def task1():
    print("Введите произвольное количество ключей (через пробел):")
    firstList = input().split()
    print("Введите произвольное количество значений (через пробел):")
    secondList = input().split()
    userDictionary = {}
    i = 0
    j = 0
    while i < len(firstList):
        if i < len(secondList):
            userDictionary[firstList[i]] = secondList[j]
        else:
            userDictionary[firstList[i]] = None
        i = i + 1 
        j = j + 1
    print ("Составленный словарь: \n", userDictionary)

#       ВТОРОЕ ЗАДАНИЕ
#Есть строка, содержащая текст и целые числа. 
#Напишите функцию, которая создаёт список из целых чисел в строке.
def task2():
    print("Введите произвольную строку:")
    string = input()
    originallist = list(string)
    finallist = []
    i = 0
    j = len(originallist)
    while i < j:
        if originallist[i].isdigit():
            finallist.append(originallist[i])
        i = i + 1
    print("Строка содержит числа: \n", finallist)

#       ТРЕТЬЕ ЗАДАНИЕ
#Написать класс "Кошка". В качестве аргумента, класс принимает число - кол-во котят. 
#В конструкторе класса случайным образом создаются котята мальчики (кол-во) 
#и котята девочки (кол-во), общее кол-во которых равно аргументу класса - 
#кол-во котят. У класса есть два метода: метод "девочки", 
#возвращает кол-во котят девочек и метод "мальчики", 
#который возвращает кол-во котят мальчиков.
def task3():
    class Cat():
        def __init__(self, kittyCount):
            random.seed(version=2)
            self.kittyCount = kittyCount
            self.a = random.randint(0, kittyCount)        
        def kittyBoys(self):
            boysCount = self.a
            return(boysCount)
        def kittyGirls(self):
            girlsCount = self.kittyCount - self.a
            return(girlsCount)
    random.seed(version=2)
    kittyCount = random.randint(0, 50)
    cat = Cat(kittyCount)
    print("Количество котят (выбрано случайно): ", kittyCount)
    print("Количество котят мальчиков: ", cat.kittyBoys())
    print("Количество котят девочек): ", cat.kittyGirls())

#       ЧЕТВЁРТОЕ ЗАДАНИЕ
#Напишите программу, на вход которой подаётся список чисел одной строкой. 
#Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
#Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
#находящийся на противоположном конце этого списка. 
#Например, если на вход подаётся список "1 3 5 6 10", 
#то на выход ожидается список "13 6 9 15 7" (без кавычек). 
#Если на вход пришло только одно число, надо вывести его же. 
#Вывод должен содержать одну строку с числами нового списка, разделёнными 
def task4():
    print("Введите список из чисел (через пробел): ")
    originalList = input().split()
    for i in range(len(originalList)):
        originalList[i] = int(originalList[i])
    if len(originalList) == 1:
        print("В списке только один элемент: " + str(originalList[0]))
    else:
        finalList = []
        i = 0
        j = len(originalList)
        a = 0
        while i < j:
            finalList.append(originalList[i - 1] + originalList[(i + 1) % len(originalList)])
            i = i + 1
        print("Сумма соседних чисел каждого элемента списка: \n", finalList)

#       ПЯТОЕ ЗАДАНИЕ
# Напишите программу, которая выводит часть 
# последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
# (число повторяется столько раз, чему равно). 
# На вход программе передаётся неотрицательное целое число 
# n — столько элементов последовательности должна отобразить программа. 
def task5():
    print("Введите целое неотрицательное число")
    number = input()
    i = 0
    while i <= int(number):
        print((str(i) + " ") * i, end='')
        i = i + 1
    print()

#       ШЕСТОЕ ЗАДАНИЕ
#Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
#удаляет из него все нечётные значения, а чётные нацело делит на два. 
#Функция не должна ничего возвращать, требуется только изменение переданного списка,
def task6():
    def modify_list(lst):
        i = 0
        while i < len(lst):
            if lst[i] % 2 == 0:
                lst[i] = int(lst[i] / 2)
                i = i + 1
            else:
                del lst[i]
    lst = []
    random.seed(version=2)
    n = random.randint(2, 10)
    for i in range(n):
        newElem = random.randint(0, 100)
        lst.append(newElem)
    print("Исходный список (сгенерирован случайно): \n", lst)
    modify_list(lst)
    print("Конечный список: \n", lst)

print("Задание 1:")
task1()
print()

print("Задание 2:")
task2()
print()

print("Задание 3:")
task3()
print()

print("Задание 4:")
task4()
print()

print("Задание 5:")
task5()
print()

print("Задание 6:")
task6()
print()

print("Хотите перепроверить задание? (1-да 2-нет)")
key = input()
key2 = "0"
if key == "1":
    while key2 != "7":
        print("Выберите номер задания (1-6) или введите 7 для выхода: ")
        key2 = input()
        if key2 == "1":
            print("Задание "+key2)
            task1()
            print()
        elif key2 == "2":
            print("Задание "+key2)
            task2()
            print()
        elif key2 == "3":
            print("Задание "+key2)
            task3()
            print()
        elif key2 == "4":
            print("Задание "+key2)
            task4()
            print()
        elif key2 == "5":
            print("Задание "+key2)
            task5()
            print()
        elif key2 == "6":
            print("Задание "+key2)
            task6()
            print()