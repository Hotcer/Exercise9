
with open('archivo.txt', 'w') as f:

    f.write('Hola, este es un archivo de texto creado en Python.\n')
    f.close()

    file = open('archivo.txt', 'a')


    file.write('Aquí agregamos más contenido al archivo.')


    file.close()

with open('archivo.txt', 'r') as f:

    contenido = f.read()
    print(contenido)

