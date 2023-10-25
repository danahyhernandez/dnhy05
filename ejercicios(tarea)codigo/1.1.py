import random

i = 2
n = random.randint(1,10)
suma = 0

for _ in range(1, i+2):
    i = random.randint(1,20)
    suma = i + 2
    print(f"resultado es:{suma}")

print(f"la suma es: {suma}")