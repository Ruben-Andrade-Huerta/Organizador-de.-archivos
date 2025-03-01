import shutil
import os
import logging

# Configurar el registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Diccionario para almacenar las rutas de las carpetas
carpetas = {
    "escritorio": "/Users/rubenandrade/Desktop",
    "descargas": "/Users/rubenandrade/Downloads",
    "imagenes": "/Users/rubenandrade/Pictures",
    "documentos": "/Users/rubenandrade/Documents",
    "videos": "/Users/rubenandrade/movies",
    "musica": "/Users/rubenandrade/music"
}

def mover_archivos(archivo, carpeta_origen, carpeta_destino):
    """
    Mueve un archivo de una carpeta a otra.

    Parámetros:
        archivo (str): Nombre del archivo que se quiere mover.
        carpeta_origen (str): Ruta de la carpeta de origen del archivo que se quiere mover.
        carpeta_destino (str): Ruta de la carpeta de destino.
    """
    ruta_archivo_destino = os.path.join(carpeta_destino, archivo)
    source_file = os.path.join(carpeta_origen, archivo) 

    if os.path.exists(ruta_archivo_destino): #Verifica si el archivo que se quiere mover ya existe en la carpeta de destino
        nombre, extension = os.path.splitext(archivo)
        counter = 1
        new_file_name = f"{nombre}_({counter}){extension}" #Se le da un nuevo nombre al archivo
        
        while os.path.exists(new_file_name):
            counter += 1
            new_file_name = f"{nombre}_{counter}{extension}"
        os.rename(os.path.join(carpeta_origen, archivo), new_file_name) 
        shutil.move(new_file_name, carpeta_destino)
        logging.info(f'archivo {new_file_name} moved to {carpeta_destino}')
    else: #Si el archivo no existe en la carpeta de destino lo mueve directamente
        shutil.move(source_file, carpeta_destino)
        logging.info(f'archivo {archivo} moved to {carpeta_destino}')

def mover_archivos_por_tipo(carpeta_origen_escritorio, carpeta_origen_descargas, carpeta_destino, archivos_permitidos):
    """
    Mueve archivos de una carpeta a otra según su extensión.

    Parámetros:
        carpeta_origen_escritorio (str): Ruta de la carpeta de origen en el escritorio.
        carpeta_origen_descargas (str): Ruta de la carpeta de origen en descargas.
        carpeta_destino (str): Ruta de la carpeta de destino.
        archivos_permitidos (list): Lista de extensiones de archivos permitidos.
    """
    carpetas_origen = [carpeta_origen_escritorio, carpeta_origen_descargas] #Las carpetas de donde se moverán los archivos
    counter = 0

    for carpeta in carpetas_origen:
        for archivo in os.listdir(carpeta):
            nombre, extension = os.path.splitext(archivo)
            if extension in archivos_permitidos: #Si la extensión del archivo está en la lista de extensiones permitidas lo moverá
                counter += 1
                mover_archivos(archivo, carpeta, carpeta_destino)
    if counter == 0:
        logging.info(f'No hay archivos que mover a la carpeta {carpeta_destino}')
        

def mover_a_imagenes():
    archivos_permitidos = [".jpg", ".png", ".jpeg", ".gif", ".webp"]
    mover_archivos_por_tipo(carpetas["escritorio"], carpetas["descargas"], carpetas["imagenes"], archivos_permitidos)

def mover_a_documentos():
    archivos_permitidos = [".pdf", ".doc", ".docx", ".txt", ".pptx", ".ppt", ".xls", ".xlsx", ".csv", ".zip", ".rar"]
    mover_archivos_por_tipo(carpetas["escritorio"], carpetas["descargas"], carpetas["documentos"], archivos_permitidos)

def mover_a_videos():
    archivos_permitidos = [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]
    mover_archivos_por_tipo(carpetas["escritorio"], carpetas["descargas"], carpetas["videos"], archivos_permitidos)

def mover_a_musica():
    archivos_permitidos = [".mp3", ".wav", ".flac", ".m4a", ".aac"]
    mover_archivos_por_tipo(carpetas["escritorio"], carpetas["descargas"], carpetas["musica"], archivos_permitidos)

# Ejecutar las funciones para mover archivos
mover_a_imagenes()
mover_a_documentos()
mover_a_videos()
mover_a_musica()