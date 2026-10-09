nota = float(input("Dime tu nota del examen \n\n"))

if nota > 10 or nota < 0:
    print("Incorrecto\n")
if nota < 5:
    print("Insuficiente\n")
elif nota < 6:
    print("Suficiente\n")
elif nota < 7:
    print("Bien\n")
elif nota < 9:
    print("Notable\n")
else:
    print("Sobresaliente\n")
