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
    V = int(input("Enter the answer - "))
    if V==K:
        print("The answer is correct")
        x += 1
        time.sleep(0.8)
        print(f'Your points - {x}')
    else:
        print("The answer is incorrect")
        time.sleep(1)
        print(f'The correct answer is - {K}')
        time.sleep(0.8)
        print(f'Your points - {x}')
        time.sleep(5)
        break
exit()
