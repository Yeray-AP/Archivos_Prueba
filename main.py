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
        api_key = "x"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:    
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_tiempo(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Check your input")
                case 401:
                    self.display_error("Invalid API key")
                case 403:
                    self.display_error("Access denied")
                case 404:
                    self.display_error("Not found")
                case 500:
                    self.display_error("Internal server error")
                case 502:
                    self.display_error("Bad gateway")
                case 503:
                    self.display_error("Service unavailable")
                case 504:
                    self.display_error("Gateway timeout")
                case _:
                    self.display_error(f"Error {http_error}")
            
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")
    
    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 15px")
        self.temp_label.setText(message)
        self.descripcion_tiempo.clear()
    
    def display_tiempo(self,data):
        self.temp_label.setStyleSheet("font-size: 70px")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        self.temp_label.setText(f"{temp_c:.0f}°C")
        weather_description = data["weather"][0]["description"]
        self.descripcion_tiempo.setText(weather_description)

if __name__ == "__main__":
    print("App has started")
    app = QApplication(sys.argv)
    weather_app = weatherApp()
    weather_app.show()
    sys.exit(app.exec_())