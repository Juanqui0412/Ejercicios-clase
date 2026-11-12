total_space = float(input("Total space (GB): "))
disk_usage = float(input("Used space (GB): "))

def disk_space(total, disk):
    result = ""
    if total > disk:
        result = "Saving the document"
    elif total == disk:
        result = "No space available"
    else:
        result = "Error"
    return result

print(disk_space(total_space,disk_usage))



edad = int(input("¿Cuántos años tienes? "))
estudiante = input("¿Eres estudiante? (si/no): ").lower()
dia = input("¿Qué día de la semana es? ").lower()

precio_base = 8.33

def precio(edad, estudiante, dia):
    result = ""

    if dia == "miércoles" or dia == "miercoles":
        result = 4
    elif edad < 12:
        result = precio_base / 2
    elif edad > 65:
        result = 5
    elif estudiante == "si":
        result = precio_base * 0.7
    else:
        result = precio_base
    return result

print(f"El precio de tu entrada es {precio(edad, estudiante, dia):.2f} €")