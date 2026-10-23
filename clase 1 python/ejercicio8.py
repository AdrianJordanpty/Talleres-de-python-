nombre = input("¿Cuál es tu nombre?")
print("Hola", nombre)
edad = input("¿Cuál es tu edad?")
print("Tu edad es", edad)

nota1  =float(input("Ingrese su priemera calificación"))

nota2 =float(input("Ingrese su segunda calificación"))

nota3 =float(input("Ingrese su tercera calificacion"))

promedio = ( nota1 + nota2 + nota3)/3

print(f"el promedio de sus notas es: {round(promedio, 2)}")

nota = float(input("Ingresa tu nota: "))

if nota >= 71:
    print("Aprobado")
else:
    print("No aprobado")     