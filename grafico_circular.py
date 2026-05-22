import matplotlib.pyplot as plt

# Datos
lenguajes = ["Python", "Java", "C++", "JavaScript"]
porcentajes = [40, 25, 15, 20]

# Crear gráfico circular
plt.pie(
    porcentajes,
    labels=lenguajes,
    autopct="%1.1f%%"
)

# Título
plt.title("Uso de Lenguajes")

# Mostrar
plt.show()