# Organizador de Archivos

Este proyecto es una herramienta para organizar archivos en diferentes carpetas según su tipo. Utiliza Python y el módulo `shutil` para mover archivos de una carpeta a otra.

## Características

- Mueve archivos de una carpeta a otra según su extensión.
- Soporta múltiples tipos de archivos, incluyendo imágenes, documentos, videos y música.
- Utiliza el módulo `logging` para registrar las operaciones realizadas.

## Requisitos

- Python 3.x
- `shutil` (incluido en la biblioteca estándar de Python)
- `os` (incluido en la biblioteca estándar de Python)
- `logging` (incluido en la biblioteca estándar de Python)
- `PyInstaller` (para crear el ejecutable)

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/organizador-archivos.git
    cd organizador-archivos
    ```

2. Instala `PyInstaller` si planeas crear un ejecutable:

    ```bash
    pip install pyinstaller
    ```

## Uso

### Ejecución del Script

Para ejecutar el script directamente con Python:

```bash
python file_organizer.py

Ejemplo de Uso
El script moverá archivos de las carpetas de origen a las carpetas de destino según su extensión. Por ejemplo, los archivos .jpg y .png se moverán a la carpeta de imágenes.

Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría hacer.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

