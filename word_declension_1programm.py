### Задача 1. Разработайте функцию, которая принимает целое число в качестве аргумента и возвращает строку, содержащую это число 
### и слово "компьютер" в нужном склонении по падежам в зависимости от числа. Например, при вводе числа 25 функция должна возвращать
## "25 компьютеров", для числа 41 — "41 компьютер", а для числа 1048 — "1048 компьютеров".

def declens(num):
    variants = {
        1: 'компьютер',
        2: 'компьютера',
        3: 'компьютеров'
    }
    if num in range(0,2):
        print(f' {num} {variants[1]}')
    elif num in range(2,5):
        print(f'{num} {variants[2]}')
    elif num in range(5,10000000):
        print(f'{num} {variants[3]}')


if __name__ == "__main__":
     declens(5)