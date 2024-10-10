def contstr(s):
    dicionario = {}
    for char in s:
        if char != ' ':  # ignore spaces
            if char in dicionario:
                dicionario[char] += 1
            else:
                dicionario[char] = 1
    return dicionario

s = input(str("Digite alguma palavra. "))
print(contstr(s))