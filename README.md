# Aplicación de Cálculo de Áreas con PyQt6

## Descripción

Esta aplicación de escritorio permite calcular el área de figuras geométricas básicas (círculo, triángulo, rectángulo y cuadrado) mediante una interfaz gráfica desarrollada con PyQt6 y siguiendo el paradigma de Programación Orientada a Objetos (POO). El usuario puede seleccionar la figura, ingresar los datos requeridos y obtener el área correspondiente.

---

## Características

- Interfaz gráfica intuitiva y fácil de usar.
- Cálculo de áreas para:
  - Círculo
  - Triángulo
  - Rectángulo
  - Cuadrado
- Validación de datos: solo se aceptan valores positivos.
- Manejo de errores amigable para el usuario.
- Código documentado siguiendo PEP 8 y Google Style Docstrings.

---

## Estructura del Proyecto
``` sh
proyecto/
├── src/
│   ├── logica/              # Lógica de negocio (clases para cálculos)
│   │   └── areas.py         # Implementación en POO (sin métodos estáticos)
│   ├── vista/               # Archivos de interfaz gráfica
│   │   ├── main_window.ui   # Diseñado en Qt Designer
│   │   └── ui_main.py       # Generado con `pyuic6`
├── app.py                   # Punto de entrada principal
└── README.md
```

---

## Instalación

1. **Clona el repositorio:**
``` sh
git clone <URL_DEL_REPOSITORIO>
cd Aplicación\ de\ Cálculo\ de\ Áreas\ con\ PyQt6\ \(POO\)
```
Crea y activa un entorno virtual (opcional pero recomendado):
```sh
python -m venv .venv
.venv\Scripts\activate
```
Instala las dependencias:
```sh
pip install -r requirements.txt
```
Si no existe requirements.txt, instala manualmente:
```sh
pip install PyQt6
```
Uso
1. Ejecuta la aplicación:
```sh
python app.py
```
2. Selecciona la figura geométrica desde el menú.

3. Ingresa los valores solicitados (solo positivos).

4. Visualiza el área calculada en pantalla.

Ejemplo de Uso
- Selecciona "Círculo" en el menú.
- Ingresa el radio (por ejemplo, 5).
- El área se mostrará en una ventana emergente.
- Documentación
- El código está documentado siguiendo el estándar PEP 8 y Google Style Docstrings.
- Cada clase y método incluye una descripción de sus argumentos, retornos y posibles excepciones.

Créditos
- Desarrollado por: Urquizo Oré Francis Maxuel - 
- Basado en PyQt6 y Python 3.x
