participante1 = input("nombre del primer participante: ")
participante2 = input("nombre del segundo participante: ")
participante3 = input("nombre del tercer participante: ")

puntos1 = 0
puntos2 = 0
puntos3 = 0

#PRIMER JUEGO

primero = input("Quien quedo primero? ")
segundo = input("Quien quedo segundo? ")
tercero = input("Quien quedo tercero? ")

if primero == participante1:
    puntos1 = puntos1 + 3
elif segundo == participante1:
    puntos1 = puntos1 + 2
elif tercero == participante1:
    puntos1 = puntos1 + 1

if primero == participante2:
    puntos2 = puntos2 + 3
elif segundo == participante2:
    puntos2 = puntos2 + 2
elif tercero == participante2:
    puntos2 = puntos2 + 1

if primero == participante3:
    puntos3 = puntos3 + 3
elif segundo == participante3:
    puntos3 = puntos3 + 2
elif tercero == participante3:
    puntos3 = puntos3 + 1

print("asi esta la tabla ahora: ", participante1, ": ", puntos1, " puntos, ", participante2, ": ", puntos2, " puntos, ", participante3, ": ", puntos3, " puntos.")

#SEGUNDO JUEGO

primero = input("Quien quedo primero? ")
segundo = input("Quien quedo segundo? ")
tercero = input("Quien quedo tercero? ")

if primero == participante1:
    puntos1 = puntos1 + 3
elif segundo == participante1:
    puntos1 = puntos1 + 2
elif tercero == participante1:
    puntos1 = puntos1 + 1

if primero == participante2:
    puntos2 = puntos2 + 3
elif segundo == participante2:
    puntos2 = puntos2 + 2
elif tercero == participante2:
    puntos2 = puntos2 + 1

if primero == participante3:
    puntos3 = puntos3 + 3
elif segundo == participante3:
    puntos3 = puntos3 + 2
elif tercero == participante3:
    puntos3 = puntos3 + 1

print("asi esta la tabla ahora: ", participante1, ": ", puntos1, " puntos, ", participante2, ": ", puntos2, " puntos, ", participante3, ": ", puntos3, " puntos.")

#TERCER JUEGO

primero = input("Quien quedo primero? ")
segundo = input("Quien quedo segundo? ")
tercero = input("Quien quedo tercero? ")

if primero == participante1:
    puntos1 = puntos1 + 3
elif segundo == participante1:
    puntos1 = puntos1 + 2
elif tercero == participante1:
    puntos1 = puntos1 + 1

if primero == participante2:
    puntos2 = puntos2 + 3
elif segundo == participante2:
    puntos2 = puntos2 + 2
elif tercero == participante2:
    puntos2 = puntos2 + 1

if primero == participante3:
    puntos3 = puntos3 + 3
elif segundo == participante3:
    puntos3 = puntos3 + 2
elif tercero == participante3:
    puntos3 = puntos3 + 1

print("asi quedo la tabla: ", participante1, ": ", puntos1, " puntos, ", participante2, ": ", puntos2, " puntos, ", participante3, ": ", puntos3, " puntos.")