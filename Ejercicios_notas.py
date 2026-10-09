nota = float(input("¿Qué nota sacaste en el examén?\n\n"))

if nota > 10:
    print("Incorrecta\n")
elif nota >=9:
    print("Sobresaliente\n")
elif nota >= 7:
    print("Notable\n")
elif nota >= 6:
    print("Bien\n")
elif nota >= 5:
    print("Suficiente\n")

elif nota <= 0:
    print("Insuficiente\n")

else:
    print("Incorrecta\n")