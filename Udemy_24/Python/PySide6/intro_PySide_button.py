import sys
from PySide6.QtWidgets import QApplication, QPushButton


app = QApplication(sys.argv)

button = QPushButton('Example')
button.setStyleSheet('font-size: 30px;')
button.show()

app.exec()