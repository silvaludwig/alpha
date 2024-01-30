import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

#application essential
app = QApplication(sys.argv)
central_widget = QWidget()
layout = QGridLayout()


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

#to show the widgets and keep the app running
central_widget.show()
app.exec()