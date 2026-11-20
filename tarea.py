
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))  # int() convierte el texto a número
materia = input("Ingresá tu materia favorita: ")

print(f"Hola {nombre}, tenés {edad} años y tu materia favorita es {materia}.")






if edad >= 16:
    print("Puede votar próximamente")
else:
    print("Todavía no puede votar")







alumnos = [
    {"nombre": "Joaquin", "materia": "Programacion", "edad": 17},
    {"nombre": "Tomas", "materia": "Redes", "edad": 18},
    {"nombre": "Yasmin", "materia": "Matematica", "edad": 17},
    {"nombre": "Jorge", "materia": "Automatizacion", "edad": 16},
    {"nombre": "Priscila", "materia": "Base de Datos", "edad": 17},
]








print("\n--- Lista de alumnos ---")
for alumno in alumnos:
    print(alumno["nombre"], "-", alumno["materia"])







def buscar_alumno():
    buscado = input("\nIngresá el nombre del alumno a buscar: ")
    for alumno in alumnos:
        # .lower() para que no importe si escriben con mayúscula o minúscula
        if alumno["nombre"].lower() == buscado.lower():
            print("Nombre:", alumno["nombre"])
            print("Materia favorita:", alumno["materia"])
            print("Edad:", alumno["edad"])
            return  # si lo encontró, sale de la función
    print("Alumno no encontrado")


buscar_alumno()








mayores_de_16 = 0
for alumno in alumnos:
    if alumno["edad"] > 16:
        mayores_de_16 = mayores_de_16 + 1

print("\n--- Estadísticas ---")
print("Cantidad total de alumnos:", len(alumnos))
print("Alumnos mayores de 16 años:", mayores_de_16)
