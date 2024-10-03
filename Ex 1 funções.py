from math import sqrt

def equacao(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Esta equação não possui soluções reais.")
    elif delta == 0:
        X = -b / (2*a)
        print(f"A equação possui uma solução real: X = {X}")
    else:
        X1 = (-b + sqrt(delta)) / (2*a)
        X2 = (-b - sqrt(delta)) / (2*a)
        print(f"A equação possui duas soluções reais: X1 = {X1} e X2 = {X2}")

a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))

equacao(a, b, c)