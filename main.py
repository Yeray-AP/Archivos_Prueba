import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class weatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Nombre de la ciudad ", self)
        self.city_input = QLineEdit(self)
        self.get_tiempo_button = QPushButton("Obtener tiempo", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.descripcion_tiempo = QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Aplicacion del tiempo")
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_tiempo_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.descripcion_tiempo)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.descripcion_tiempo.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_tiempo_button.setObjectName("get_tiempo_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.descripcion_tiempo.setObjectName("descripcion_tiempo")
    
        self.setStyleSheet("""

            QLabel, QPushButton{
                font-family: 'Serif';
            }
            
            QLabel#city_label{
                font-size:40px;               
                font-style: italic;
            }
                           
            QLineEdit#city_input{
                font-size:20px;
                border-radius:10;
            }
                           
            QPushButton#get_tiempo_button{
                font-size:20px;
                font-weight:bold;
            }
            QLabel#temp_label{
             font-size: 75px;
            }
            QLabel#emoji_label{
                font-size:60px;
                font-family: Segoe UI emoji;                     
            }
            QLabel#descripcion_tiempo{
                font-size:70px;
            }
        """)
        
        self.get_tiempo_button.clicked.connect(self.get_tiempo)


    def get_tiempo(self):
        print("El boton funciona")
        api_key = ""
        pass
    def display_error(self, message):
        pass
    def display_tiempo(self,data):
        pass
if __name__ == "__main__":
    print("hola")
    app = QApplication(sys.argv)
    weather_app = weatherApp()
    weather_app.show()
    sys.exit(app.exec_())