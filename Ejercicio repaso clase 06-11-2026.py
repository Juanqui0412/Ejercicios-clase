edad = int(input("¿Cuántos años tienes? "))
estudiante = input("¿Eres estudiante? (si/no): ").lower()
dia = input("¿Qué día de la semana es? ").lower()

precio_base = 8.33

if dia == "miércoles" or dia == "miercoles":
    precio = 4
elif edad < 12:
    precio = precio_base / 2
elif edad > 65:
    precio = 5
elif estudiante == "si":
    precio = precio_base * 0.7
else:
    precio = precio_base

print(f"El precio de tu entrada es {precio:.2f} €")