from random import randint
import time
x = 0
while True:
    p = randint(1,99)
    o = randint(1,99)
    K = p + o
    time.sleep(0.5)
    print(f'{p} + {o} = ')
    time.sleep(0.2)
    V = int(input("Введите ответ - "))
    if V==K:
        print("Ответ верен")
        x += 1
        time.sleep(0.8)
        print(f'Ваши очки - {x}')
    else:
        print("Ответ не верный")
        time.sleep(1)
        print(f'Правильный ответ - {K}')
        time.sleep(0.8)
        print(f'Ваши очки - {x}')
        time.sleep(5)
        break
exit()
