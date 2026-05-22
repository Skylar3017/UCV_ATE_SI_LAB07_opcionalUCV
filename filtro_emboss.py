from PIL import Image, ImageFilter

imagen = Image.open("imagenes/marte.jpg")

resultado = imagen.filter(ImageFilter.SMOOTH)

resultado.show()