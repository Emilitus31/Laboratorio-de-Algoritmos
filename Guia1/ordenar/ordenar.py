TAMANIO = 5

Arreglo_1 = [ 18, 12, 9, 2018, 912 ]

Arreglo_final = [ ]

numero_menor = Arreglo_1[0]

for i in Arreglo_1:
    if i < numero_menor:
        numero_menor = i

numero1 = numero_menor
Arreglo_final.append(numero1)

numero_menor = 9999

for i in Arreglo_1:
    if i < numero_menor:
        if i != numero1:
            numero_menor = i


numero2 = numero_menor
Arreglo_final.append(numero2)

numero_menor = 9999

for i in Arreglo_1:
    if i < numero_menor: 
        if i != numero1:
            if i != numero2:
                numero_menor = i

numero3 = numero_menor
Arreglo_final.append(numero3)

numero_menor = 9999

for i in Arreglo_1:
    if i < numero_menor: 
        if i != numero1:
            if i != numero2:
                if i != numero3:
                    numero_menor = i

numero4 = numero_menor
Arreglo_final.append(numero4)

numero_menor = 9999

for i in Arreglo_1:
    if i < numero_menor: 
        if i != numero1:
            if i != numero2:
                if i != numero3:
                    if i != numero4:
                        numero_menor = i

numero5 = numero_menor
Arreglo_final.append(numero5)

Arreglo_1 = Arreglo_final

print(Arreglo_1)