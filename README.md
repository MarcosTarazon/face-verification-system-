# Reconocimiento facial con Python

Proyecto sencillo de reconocimiento facial con `OpenCV` y `face_recognition`.
El script principal carga dos imagenes desde la carpeta `images/`, detecta los rostros, dibuja el recuadro de cada cara y compara si ambas pertenecen a la misma persona.

## Funcionalidades

- Carga automaticamente las primeras 2 imagenes dentro de `images/`.
- Detecta rostros en cada imagen.
- Dibuja rectangulos sobre las caras detectadas.
- Calcula la distancia facial entre ambas imagenes.
- Muestra las dos imagenes procesadas en pantalla.
- Imprime en consola la distancia y si ambas caras coinciden.

## Requisitos

- Python 3.9 o superior.
- Dependencias listadas en `requirements.txt`.
- Una carpeta llamada `images/` en la raiz del proyecto con al menos 2 imagenes validas.

## Instalacion

1. Crea y activa un entorno virtual.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Coloca tus imagenes dentro de `images/`.
2. Ejecuta el script principal:

```bash
python app.py
```

El programa abrira dos ventanas con las imagenes procesadas y mostrara en consola la distancia facial y el resultado de la comparacion.

## Estructura del proyecto

```text
.
├── app.py
├── images/
│   ├── foto1.JPEG
│   ├── foto2.JPEG
│   └── michael.JPEG
├── README.md
└── requirements.txt
```

## Como funciona

- El script toma como base la ubicacion de `app.py`, no una ruta local de tu computadora.
- Busca unicamente dentro de `images/`.
- Ordena alfabeticamente los archivos de imagen encontrados y usa los dos primeros.
- Si `images/` no existe o tiene menos de 2 imagenes, el script se detiene con error.

## Notas

- `face_recognition` depende de `dlib`, que en Windows puede requerir herramientas de compilacion si la instalacion no encuentra una rueda precompilada.
- Si vas a publicar el proyecto en GitHub, conviene mantener una o dos imagenes de ejemplo dentro de `images/` y reemplazarlas por las tuyas cuando pruebes el sistema.

## Licencia
