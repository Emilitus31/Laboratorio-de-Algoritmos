TAMANIO = 5

Arreglo_1 = [ 18, 12, 9, 2018, 912 ]

Arreglo_final = [ ]

numero_menor = Arreglo_1[0]

for i in Arreglo_1:
    if i < numero_menor:
        numero_menor = i

numero1 = numero_menor
Arreglo_final.append(numero1)

numero_menor = 999

for i in Arreglo_1:
    if i < numero_menor & i != numero1:
        numero_menor = i


numero2 = numero_menor
Arreglo_final.append(numero2)

numero_menor = 999

for i in Arreglo_1:
    if i < numero_menor & i != numero1 & i != numero2:
        numero_menor = i

numero3 = numero_menor
Arreglo_final.append(numero3)

numero_menor = 999

for i in Arreglo_1:
    if i < numero_menor & i != numero1 & i != numero2 & != numero3:
        numero_menor = i

numero3 = numero_menor
Arreglo_final.append(numero3)

numero_menor = 999