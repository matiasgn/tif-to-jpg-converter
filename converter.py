import os
import sys
from skimage.color import gray2rgb
import tifffile as tf

def convertir_tif_a_jpg(filepath, output_dir):
    # Crear el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definir el nombre de archivo de salida JPG
    jpg_name = os.path.splitext(os.path.basename(filepath))[0] + ".jpg"
    jpg_path = os.path.join(output_dir, jpg_name)

    # Abrir la imagen TIF
    with tf.TiffFile(filepath) as tif:
        image = tif.asarray()

    # Verificar la forma de la imagen (número de dimensiones y tamaño de cada dimensión)
    print("Forma de la imagen:", image.shape)

    # Si la imagen tiene una sola dimensión, es una imagen en escala de grises y necesitas convertirla a RGB
    if len(image.shape) == 2:
        # Convertir la imagen en escala de grises a RGB
        image = gray2rgb(image)

    # Guardar la imagen como JPG
    tf.imwrite(jpg_path, image, photometric='rgb')

    print("\n\nJPG Conversion Completed")

if __name__ == "__main__":
    # Verificar que se hayan proporcionado los argumentos correctos
    if len(sys.argv) != 3:
        print("Uso: python script.py ruta_del_archivo_tif ruta_destino_jpg")
        sys.exit(1)

    # Obtener las rutas de los archivos de los argumentos de línea de comandos
    filepath = sys.argv[1]
    output_dir = sys.argv[2]

    # Llamar a la función para convertir el archivo TIF a JPG
    convertir_tif_a_jpg(filepath, output_dir)

