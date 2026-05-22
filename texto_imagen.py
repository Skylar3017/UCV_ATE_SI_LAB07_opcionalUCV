from PIL import Image
from PIL import ImageDraw

imagen = Image.open("imagenes/marte.jpg")

dibujo = ImageDraw.Draw(imagen)

dibujo.text((50, 50), "Laboratorio 07", fill="white")

imagen.show()