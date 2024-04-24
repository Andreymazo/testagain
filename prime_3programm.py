### Задача 3. Написать функцию/метод, которая возвращает массив простых чисел в диапазоне (2 числа - минимальное и максимальное) заданных чисел.
### Например, на вход переданы 2 числа: от 11 до 20  (диапазон считается включая граничные значения).
### На выходе программа должна выдать [11, 13 , 17, 19]

### Только что делал токое. Копирую с гита (там много чего интересного посмотрите ,например одновременно скачивание емэйлов из mail.ru yandex.ru)
## https://github.com/Andreymazo/TestovoeTECCOD/blob/main/testovoe_teccod/management/commands/defs_for_test.py

#2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
def if_prime_number(num):# Определим простое ли число
        index = 1
        while index-1 <= num:
            index += 1
            if num % index == 0 and num==index:
                # print(False)
                return False  
            if num % index == 0:  
                index+=1
                # print(True)
                return True
            
def dprime_numbers(num_1, num_2):## На входе два числа (мал, боль) на выходе список простых чисел на интервале
    lst_prime_num = [i for i in range(num_1, num_2+1) if if_prime_number(i)==False]
    print(lst_prime_num)
            
if __name__ == "__main__":
     dprime_numbers(2,19)
