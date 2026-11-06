import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget


class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).with_name("formulario.ui"), self)
        self.btnGuardar.clicked.connect(self.guardar)

    def guardar(self):
        archivo = Path(__file__).with_name("datos.txt")
        with archivo.open("a", encoding="utf-8") as salida:
            salida.write(
                f"Nombre: {self.inputNombre.text()}\n"
                f"Apellido: {self.inputApellido.text()}\n"
                f"Matrícula: {self.inputMatricula.text()}\n"
                f"Teléfono: {self.inputTelefono.text()}\n\n"
            )

        QMessageBox.information(self, "Guardado", "Los datos se guardaron correctamente.")
        self.inputNombre.clear()
        self.inputApellido.clear()
        self.inputMatricula.clear()
        self.inputTelefono.clear()


app = QApplication(sys.argv)
ventana = Formulario()
ventana.show()
sys.exit(app.exec())