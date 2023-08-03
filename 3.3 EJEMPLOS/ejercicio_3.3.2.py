import os

# Solicito los datos al usuario
termino=input("¿Qué término quieres buscar?: ").upper()
ruta=input("¿En qué directorio quieres hacer la búsqueda?: ")

# Creo una lista para almacenar el resultado
resultado=list()

# Recorro la ruta
for directorio, directorios, archivos in os.walk(ruta):

    # Por cada directorio busco en los archivos
    for archivo in archivos:

        # Si el término está en el nombre del archivo
        # (Busco en mayúsculas para ignorar mayúsculas / minúsculas)
        if termino in archivo.upper():

            # Lo incluyo en la lista
            resultado.append(os.path.join(directorio,archivo))

# Escribo los resultados
print(f"He encontrado {len(resultado)} archivos:")

for archivo in resultado:
    print(f"\t> {archivo}")