alumnos = {
    60902 : "Rodolfo Fernandez",
    61654 : "Luis Gomez",
    61852 : "Andrea Pereira",
    61754 : "Juan Cruz Gonzales"
}

materias = [
    ["Ciencias",    0, 0, 0],
    ["Historia",    0, 0, 0],
    ["Geografía",   0, 0, 0],
    ["Matemáticas", 0, 0, 0],
    ["Física",      0, 0, 0]
]

notasFinales = [
    ["Rodolfo Fernandez",  0],
    ["Luis Gomez",         0],
    ["Andrea Pereira",     0],
    ["Juan Cruz Gonzales", 0]
]

indiceAlumno = 0

for alumno in alumnos.values():
    print("\nAlumno", alumno)

    for materia in materias:
        print(f"\nIngrese las notas para la materia {materia[0]}")

        nota1 = int(input("Nota 1: "))
        while nota1 < 0 or nota1 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota1 = int(input("Nota 1: "))

        nota2 = int(input("Nota 2: "))
        while nota2 < 0 or nota2 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota2 = int(input("Nota 2: "))

        materia[1] = nota1
        materia[2] = nota2
        materia[3] = (nota1 + nota2) / 2
        print("Nota Final", materia[3])

    # mostrar tabla de materias completa
    print("\nMaterias de", alumno)
    print("-" * 40)
    for materia in materias:
        print(materia[0], "-", materia[1], "-", materia[2], "-", materia[3])

    # materia con nota más alta
    materiaMasAlta = materias[0]
    for materia in materias:
        if materia[3] > materiaMasAlta[3]:
            materiaMasAlta = materia
    print("Materia con nota más alta:", materiaMasAlta[0], "-", materiaMasAlta[3])

    # promedio general del alumno
    sumaNotas = 0
    for materia in materias:
        sumaNotas += materia[3]
    promedioGeneral = sumaNotas / len(materias)

    notasFinales[indiceAlumno][1] = promedioGeneral
    indiceAlumno += 1

    # resetear notas para el próximo alumno
    for materia in materias:
        materia[1] = 0
        materia[2] = 0
        materia[3] = 0

# alumno con mejor promedio
mejorAlumno = notasFinales[0]
for nf in notasFinales:
    if nf[1] > mejorAlumno[1]:
        mejorAlumno = nf

print("\n=== Resultados finales ===")
for nf in notasFinales:
    print(nf[0], "-", nf[1])

print("\nAlumno con mejor promedio:", mejorAlumno[0], "-", mejorAlumno[1])
