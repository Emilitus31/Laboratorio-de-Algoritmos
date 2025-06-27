TAMANIO = 5

Arreglo = [ 1, 4, 5, 2, 3 ]

error = 0

num_mayor = 0

for i in Arreglo:
    if i > num_mayor:
        num_mayor = i
    else:
        error = error +1

print("Tu arreglo ", Arreglo, " tiene ", error, " errores.")