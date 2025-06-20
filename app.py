from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from src.vista.ui_main import Ui_MainWindow
from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado
from PyQt6 import QtGui

class MainWindow(QMainWindow):
    """Ventana principal de la aplicación de cálculo de áreas.

    Esta clase maneja la interfaz gráfica principal y la lógica de interacción
    para calcular áreas de diferentes figuras geométricas. Utiliza el archivo
    generado automáticamente por Qt Designer (`Ui_MainWindow`) y conecta las
    acciones del menú con funciones para solicitar datos y mostrar los resultados.
    """

    def __init__(self):
        """Inicializa la ventana principal y conecta las señales.

        Configura la interfaz de usuario y establece las conexiones
        entre las acciones del menú y sus respectivas funciones.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexión de señales
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionCirculo.triggered.connect(self.abrir_dialogo_circulo)
        self.ui.actionTriangulo.triggered.connect(self.abrir_dialogo_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.abrir_dialogo_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.abrir_dialogo_cuadrado)

    def abrir_dialogo_circulo(self):
        """Abre un diálogo para ingresar el radio y calcula el área del círculo.

        Muestra un diálogo para que el usuario ingrese el radio del círculo,
        calcula su área y muestra el resultado en una ventana de información.
        Si ocurre un error de validación, muestra una ventana de advertencia.
        """
        radio, ok = QInputDialog.getDouble(self, "Círculo", "Radio:", min=0.0)
        if ok:
            try:
                area = Circulo(radio).calcular_area()
                QMessageBox.information(self, "Área Círculo", f"{area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_triangulo(self):
        """Abre diálogos para ingresar base y altura y calcula el área del triángulo.

        Muestra diálogos secuenciales para que el usuario ingrese la base y altura
        del triángulo, calcula su área y muestra el resultado en una ventana de
        información. Si ocurre un error de validación, muestra una ventana de advertencia.
        """
        base, ok1 = QInputDialog.getDouble(self, "Triángulo", "Base:", min=0.0)
        altura, ok2 = QInputDialog.getDouble(self, "Triángulo", "Altura:", min=0.0)
        if ok1 and ok2:
            try:
                area = Triangulo(base, altura).calcular_area()
                QMessageBox.information(self, "Área Triángulo", f"{area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_rectangulo(self):
        """Abre diálogos para ingresar base y altura y calcula el área del rectángulo.

        Muestra diálogos secuenciales para que el usuario ingrese la base y altura
        del rectángulo, calcula su área y muestra el resultado en una ventana de
        información. Si ocurre un error de validación, muestra una ventana de advertencia.
        """
        base, ok1 = QInputDialog.getDouble(self, "Rectángulo", "Base:", min=0.0)
        altura, ok2 = QInputDialog.getDouble(self, "Rectángulo", "Altura:", min=0.0)
        if ok1 and ok2:
            try:
                area = Rectangulo(base, altura).calcular_area()
                QMessageBox.information(self, "Área Rectángulo", f"{area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_cuadrado(self):
        """Abre un diálogo para ingresar el lado y calcula el área del cuadrado.

        Muestra un diálogo para que el usuario ingrese el lado del cuadrado,
        calcula su área y muestra el resultado en una ventana de información.
        Si ocurre un error de validación, muestra una ventana de advertencia.
        """
        lado, ok = QInputDialog.getDouble(self, "Cuadrado", "Lado:", min=0.0)
        if ok:
            try:
                area = Cuadrado(lado).calcular_area()
                QMessageBox.information(self, "Área Cuadrado", f"{area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()