from PIL import Image

imagen = Image.open("imagenes/marte.jpg")

rotada = imagen.rotate(45)

rotada.show()