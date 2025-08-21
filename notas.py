estudiantes = [("Mateo", 92), ("Carlos", 75), ("Ana", 46), ("Damian", 57), ("Paula", 85)]
aprobados = []
reprobados = []


for nombres, notas in estudiantes:
    if notas >= 70 and notas <= 100:
        aprobados.append((nombres, notas))
    elif notas < 70:
        reprobados.append((nombres, notas))
    else:
        print(f"Nota invalida para {nombres}")

