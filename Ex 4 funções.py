a = int(input('Digite um valor para a: '))
fat = a
a = a-1
def fatorial(fat, a):
    while a > 0:
        fat = fat * a
        a = a-1
    

    print(fat)
    
fatorial(fat, a)