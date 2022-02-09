from math import sqrt, log, exp, factorial
import array
   
def main_menu(): 
    is_exit = False
    is_right_input = False
    choice = 0
    
    main_menu_string="""Выберите функцию:
    1) Калькулятор
    2) Анализ строки
    3) Построение матрицы"""
    
    while is_exit==False:
        while is_right_input==False:
            print(main_menu_string) 
            try:
                choice = int(input("Функция: "))
            except:
                print("Ошибка: Введите целое число. ")
            else: 
                is_right_input=True
        if choice == 1:
            print("Выбран калькулятор")
            is_exit=True
            choose_calc_func()
        elif choice == 2:
            print("Выбран анализ строки")
            is_exit=True
            string_analyse()
        elif choice == 3:
            print("Выбрано построение матрицы")
            is_exit=True
            matrix_create()
        else:
            is_right_input = False
        

def printMatrix ( matrix ): 
   for row in matrix: 
      for x in row: 
          print ( "{:4d}".format(x), end = "" ) 
      print ()
    
def matrix_create():
     true_choice = False
     choice = 0
     first_step = True
     mtx_rows = correct_int_input("Введите кол-во столбцов: ")
     mtx_columns = correct_int_input("Введите кол-во строк: ")
     start_value = correct_int_input("Введите начальное значение: ")
     mtx_step = correct_int_input("Введите шаг матрицы: ")
     mtx = []
  
     last_element = 0 

     for i in range(mtx_rows):
         a = []
         for j in range(mtx_columns):
             if(first_step == True):
                 first_step = False
                 a.append(start_value)
                 last_element = start_value
             else:
                 last_element += mtx_step
                 a.append(last_element)
         mtx.append(a)
     printMatrix(mtx)
    
     print("Вернуться в меню или повторить операцию? 1 - Вернуться, 2 - Повторить")
     while true_choice == False:
            choice = correct_input("Выберите операцию: ")
            if(choice == 1):
                true_choice = True
                main_menu()
            elif(choice == 2):
                true_choice = True
                matrix_create()




def string_analyse(): 
    is_string = False
    some_string = "SOME_STRING"

    true_choice = False
    choice = 0
    while is_string==False:
        try: 
            some_string = input("Введите строчку: ")
        except ValueError: 
            print("Ошибка: Формат строки неверный")
        else:
            string_length = len(some_string)
            comma_inc = 0
            space_inc = 0
            for i in range(string_length):
                if(some_string[i] == ','):
                    comma_inc +=1
                elif(some_string[i]==" "):
                    space_inc+=1
            is_string=True
            print ("Количество символов: ", string_length)
            print ("Количество запятых: ", comma_inc)
            print ("Количество пробелов: ", space_inc)
            print("Вернуться в меню или повторить операцию? 1 - Вернуться, 2 - Повторить")
            while true_choice == False:
                choice = correct_input("Выберите операцию: ")
                if(choice == 1):
                 true_choice = True
                 main_menu()
                elif(choice == 2):
                  true_choice = True
                  string_analyse()
      

def chooserator(index):
    if(index == 1):
        func_summ()
    elif(index == 2):
        func_subtraction()
    elif(index==3):
        func_multiplication()
    elif(index==4):
        func_dividing()
    elif(index==5):
        func_dividing_whole()
    elif(index==6):
        func_dividing_remainder()
    elif(index==7):
        func_pow()
    elif(index==8):
        func_sqrt()
    elif(index==9):
        func_log()
    elif(index==10):
        func_exp()
    elif(index==11):
        func_factorial()

def cls(): 
    print ("\n" * 100)

def correct_int_input(text):
    is_int = False
    while is_int==False:
        try:
            int_number = int(input(text))
        except ValueError: 
            print("Ошибка. Введите число.")
        else:
            is_int=True
    return int_number 

def correct_input(text):
    is_int = False
    while is_int==False:
        try:
            int_number = float(input(text))
        except ValueError: 
            print("Ошибка. Введите число.")
        else:
            is_int=True
    return int_number  
    
def func_summ():
    cls()
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Сумма: ")
    print(a+b)
    return_or_repeat(1)
        
def func_subtraction():
    cls()
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Разность: ")
    print(a-b)
    return_or_repeat(2)

def func_multiplication():
    cls()
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат умножения: ")
    print(a*b)
    return_or_repeat(3)

def func_dividing():
    cls()
    res = 0
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат деления: ")
    
    try:
        res = a/b
    except ZeroDivisionError:
        print("Ошибка: Делить на ноль нельзя!") 
        return_or_repeat(4)
    else: 
        print("Результат деления: ")
        print(res)
        return_or_repeat(4)

def func_dividing_whole():
    cls()
    res = 0
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат деления: ")
    
    try:
        res = a//b
    except ZeroDivisionError:
        print("Ошибка: Делить на ноль нельзя!") 
        return_or_repeat(4)
    else: 
        print("Результат деления нацело: ")
        print(res)
        return_or_repeat(5)

def func_dividing_remainder():
    cls()
    res = 0
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат деления: ")
    
    try:
        res = a%b
    except ZeroDivisionError:
        print("Ошибка: Делить на ноль нельзя!") 
        return_or_repeat(4)
    else: 
        print("Остаток от деления: ")
        print(res)
        return_or_repeat(6) 

def func_pow():
    cls()
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат возведения в степень: ")
    print(pow(a,b))
    return_or_repeat(7)

def func_sqrt():
    cls()
    a = False
    while a==False: 
        a=correct_input("Введите число А: ")
    print("Корень из A: ")
    print(sqrt(a))
    return_or_repeat(8)

def func_log():
    cls()
    a = False
    b = False
    while a==False and b == False: 
        a=correct_input("Введите число А: ")
        b=correct_input("Введите число B: ")
    print("Результат операции: ")
    print(log(a,b))
    return_or_repeat(9)

def func_exp():
    cls()
    a = False
    while a==False: 
        a=correct_input("Введите число А: ")
    print("Результат операции: ")
    print(log(a))
    return_or_repeat(10)   

def func_factorial():
    cls()
    a = False
    while a==False: 
        a=correct_int_input("Введите число А: ")
    print("Результат операции: ")
    print(factorial(a))
    return_or_repeat(11)
    
def choose_calc_func():
    is_exit = False
    is_right_input = False
    choice = 0
    
    main_menu_string="""Выберите функцию:
    1) Сумма
    2) Вычитание
    3) Умножение
    4) Деление
    5) Деление нацело
    6) Нахождение остатка от деления
    7) Степень
    8) Корень
    9) Логарифм
    10) Экспонента
    11) Факториал
    0) Вернуться в главное меню"""
    
    while is_exit==False:
        while is_right_input==False:
            print(main_menu_string) 
            try:
                choice = int(input("Выберите действие: "))
            except:
                print("Ошибка: Введите целое число. ")
            else: 
                is_right_input=True
        
        if choice == 1:
            print("Выбрано сложение")
            is_exit=True
            func_summ()
        elif choice == 2:
            print("Выбрано вычитание")
            is_exit=True
            func_subtraction()
        elif choice == 3:
            print("Выбрано умножение")
            is_exit=True
            func_multiplication()
        elif choice == 4:
            print("Выбрано деление")
            is_exit=True
            func_dividing()
        elif choice == 5:
            print("Выбрано деление нацело")
            is_exit=True
            func_dividing_whole()
        elif choice == 6:
            print("Выбрано нахождение остатка от деления")
            is_exit=True
            func_dividing_remainder()
        elif choice == 7:
            print("Выбрано нахождение степени")
            is_exit=True
            func_pow()
        elif choice == 8:
            print("Выбрано нахождение корня")
            is_exit=True
            func_sqrt()
        elif choice == 9:
            print("Выбрано нахождение логарифма")
            is_exit=True
            func_log()
        elif choice == 10:
            print("Выбрано нахождение экспоненты")
            is_exit=True
            func_exp()
        elif choice == 11:
            print("Выбрано нахождение факториала")
            is_exit=True
            func_factorial()
        elif choice == 0: 
            print("Возвращение в главное меню")
            is_exit=True
            main_menu()
        else: 
            print("Выберите корректную функцию!")
            is_right_input = False

def return_or_repeat(function):
    true_choice = False
    choice = 0
    while true_choice == False:
        print("Вернуться или повторить операцию? 1 - Вернуться, 2 - повторить")
        choice = correct_input("Выберите операцию: ")
        if(choice == 1):
          true_choice = True
          choose_calc_func()
        elif(choice == 2):
          true_choice = True
          chooserator(function)

main_menu()


