import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

# Crear gráfico
plt.scatter(x, y)

# Título
plt.title("Gráfico de Dispersión")

# Etiquetas
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar
plt.show()