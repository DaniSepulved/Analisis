import csv
import random
from faker import Faker

fake = Faker('es_ES')

profesores = []
for i in range(1, 2001):
    nombre = fake.name()
    email = fake.unique.email()
    profesores.append([i, nombre, email])

with open('profesores.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id_profesor', 'nombre', 'email'])
    writer.writerows(profesores)

cuestionarios = []
for i in range(1, 2001):
    titulo = fake.sentence(nb_words=4)
    cuestionarios.append([i, titulo, i]) 

with open('cuestionarios.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id_cuestionario', 'titulo', 'id_profesor'])
    writer.writerows(cuestionarios)

preguntas = []
for i in range(1, 2001):
    texto = fake.sentence(nb_words=6)
    preguntas.append([i, texto, i]) 

with open('preguntas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id_pregunta', 'texto', 'id_cuestionario'])
    writer.writerows(preguntas)

estudiantes = []
for i in range(1, 2001):
    nombre = fake.name()
    email = fake.unique.email()
    estudiantes.append([i, nombre, email])

with open('estudiantes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id_estudiante', 'nombre', 'email'])
    writer.writerows(estudiantes)

respuestas = []
for i in range(1, 2001):
    id_pregunta = random.randint(1, 2000)
    id_estudiante = random.randint(1, 2000)
    respuestas.append([i, id_pregunta, id_estudiante])

with open('respuestas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id_respuesta', 'id_pregunta', 'id_estudiante'])
    writer.writerows(respuestas)