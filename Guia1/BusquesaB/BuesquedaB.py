N = 5

a = [1, 2, 3, 4, 5]

facu = int(input("Ingresar número entero: "))

l = -1

for i in a:
    l = l + 1
    if i >= facu:
        print(l)
        break
    elif l == 4:
        print("Número no encontrado")