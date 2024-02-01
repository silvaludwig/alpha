# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec


import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

#application essential
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QGridLayout()

def slot_example(status_bar):
    status_bar.showMessage('test message')

#buttons
button_1 = QPushButton('button n1')
button_1.setStyleSheet('font-size: 30px; color: blue;')

button_2 = QPushButton('button n2')
button_2.setStyleSheet('font-size: 30px; color: red;')

button_3 = QPushButton('button n3')
button_3.setStyleSheet('font-size: 30px; color: pink;')

button_4 = QPushButton('button n4')
button_4.setStyleSheet('font-size: 30px; color: orange;')

#setting the layout
central_widget.setLayout(layout)

#adding the widgets/buttons to the defined layout
layout.addWidget(button_1, 1, 1) #widget / row / column / row_span / column_span
layout.addWidget(button_2, 1, 2)
layout.addWidget(button_3, 2, 1, 1, 2)
layout.addWidget(button_4, 1, 3, 2, 1)

#statusBar
status_bar = window.statusBar()
status_bar.showMessage('status bar example')

#menuBar
menu = window.menuBar()
first_menu = menu.addMenu('First menu')
first_action = first_menu.addAction('First action')
first_action.triggered.connect(
    lambda: slot_example(status_bar)
)

#to show the widgets and keep the app running
window.show()
app.exec()