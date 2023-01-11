import qrcode

# Abrir el archivo de texto
with open("qr.txt", "r") as f:
    lines = f.readlines()

# Recorrer las líneas en el archivo
for i, line in enumerate(lines):
    # Crear un objeto QR
    qr = qrcode.QRCode(version=1, box_size=10, border=0)
    
    # Agregar el texto a codificar
    qr.add_data(line.strip())
    
    # Generar la imagen
    img = qr.make_image()
    nombre_archivo= f"{i + 1}.png"
    
    # Guardar la imagen en disco
    img.save(nombre_archivo)
    print(f"Archivo {nombre_archivo} creado con valor {line.strip()}")
