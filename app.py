
from pathlib import Path

import cv2
import face_recognition as fr

#botiene la direccion absoluta de la carpeta raíz
BASE_DIR = Path(__file__).resolve().parent
EXTENSIONES_IMAGEN = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}

def cargar_imagenes(base_dir: Path, cantidad: int = 2) -> list[Path]:
    """Busca automaticamente las primeras imagenes en images/."""

    #obtiene la dirección de la carpeta "images"
    carpeta_imagenes = base_dir / "images"
    if not carpeta_imagenes.is_dir():
        raise FileNotFoundError(
            "No existe la carpeta images/. Debes crearla en la raiz del proyecto y colocar al menos 2 imagenes."
        )

    #ordena los archivos (imágenes) que cumplan con el filtro
    imagenes = sorted(
        archivo
        for archivo in carpeta_imagenes.iterdir()
        if archivo.is_file() and archivo.suffix.lower() in EXTENSIONES_IMAGEN
    )

    if len(imagenes) < cantidad:
        raise FileNotFoundError(
            "No se encontraron suficientes imagenes en images/. Coloca al menos 2 archivos de imagen para ejecutar el script."
        )

    #devuelve las 2 primeras imágenes de la lista
    return imagenes[:cantidad]

# cargar imágenes
foto_control_path, foto_prueba_path = cargar_imagenes(BASE_DIR)
foto_control = fr.load_image_file(foto_control_path)
foto_prueba = fr.load_image_file(foto_prueba_path)

#pasar imágenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_coficada_A = fr.face_encodings(foto_control)[0]

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_coficada_B = fr.face_encodings(foto_prueba)[0]

#mostrar rectangulos
"""El rectangulo se genera con los vertices del lugar_cara
genera 4 líneas en este orden: 
1. Vertical izquierda (x1)
2. horizontal superior (y1)
3. Vertical derecha (x2)
4. horizontal inferior (y2)
se genera en una tupla en ese orden, por eso los índices tienen ese orden
"""
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]), #x,y
              (lugar_cara_A[1], lugar_cara_A[2]), #x,y
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2)

#medida de la distancia (parámetro de comparativa)
distancia = fr.face_distance([cara_coficada_A], cara_coficada_B) 
print(distancia)

#realizar comparacíon 
resultado = fr.compare_faces([cara_coficada_A], cara_coficada_B)#compara en un objeto de tipo [list]
if resultado:
    print("Son la misma persona")
    
#mostrar imagenes 
cv2.imshow("Foto control", foto_control)
cv2.imshow("Foto prueba", foto_prueba)

#mantener el programa abierto 
cv2.waitKey(0)
