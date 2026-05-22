import matplotlib.pyplot as plt

# Datos
cursos = ["Python", "Java", "C++", "JavaScript"]
alumnos = [25, 18, 15, 30]

# Crear gráfico
plt.bar(cursos, alumnos)

# Título
plt.title("Cantidad de alumnos por curso")

# Etiquetas
plt.xlabel("Cursos")
plt.ylabel("Alumnos")

# Mostrar
plt.show()