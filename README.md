# Reconocimiento facial con Python

Proyecto sencillo de reconocimiento facial con `OpenCV` y `face_recognition`.
El script carga dos imagenes, detecta los rostros, dibuja el recuadro de cada cara y compara si ambas pertenecen a la misma persona.

## Funcionalidades

- Carga imagenes desde disco.
- Detecta rostros en cada imagen.
- Genera rectangulos sobre las caras detectadas.
- Calcula la distancia facial entre ambas imagenes.
- Muestra el resultado de la comparacion en pantalla.

## Requisitos

- Python 3.9 o superior.
- Dependencias listadas en `requirements.txt`.
- Las imagenes `foto1.JPEG` y `foto2.JPEG` deben estar disponibles en la ruta esperada por el script.

## Instalacion

1. Crea y activa un entorno virtual.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script principal:

```bash
python reconocimiento_facial.py
```

El programa abrira dos ventanas con las imagenes procesadas y mostrara en consola la distancia facial y el resultado de la comparacion.

## Estructura del proyecto

```text
.
├── README.md
├── requirements.txt
├── app.py
├── foto1.JPEG
├── foto2.JPEG
├── michael.JPEG
└── imagenes/   # opcional
```

## Notas

- `face_recognition` depende de `dlib`, que en Windows puede requerir herramientas de compilacion si la instalacion no encuentra una rueda precompilada.
- El script busca automaticamente las primeras 2 imagenes unicamente dentro de `images/`.
- Si `images/` no existe o tiene menos de 2 imagenes, el script se detiene con error.

## Licencia
