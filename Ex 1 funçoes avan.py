def contemp(temps, escala, destino):
    tempcon = []

    if escala == 'C' and destino == 'F':
        for temp in temps:
            temp_f = temp* (9/5)+32
            tempcon.append(temp_f)

    elif escala == 'F' and destino == 'C':
         for temp in temps:
            temp_c = temp* (9/5)
            tempcon.append(temp_c)

   
    return tempcon

temps = input("Digite as temperaturas separadas por vírgula: ")
temps = list(map(float, temps.split(',')))

escala = input("Digite a escala de início(C para celcius ou F para Fahrenheit): ").strip().upper()
destino = input("Digite a escala de início(C para celcius ou F para Fahrenheit): ").strip().upper()

tempcon = contemp(temps, escala, destino)

print(tempcon)
