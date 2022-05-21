from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QVBoxLayout, QPushButton)

from random import randint

def generate_random():
    label.setText("The winner:")
    label.hide()
    x = randint(1, 100)
    label1.setText(str(x))


app = QApplication([])
my_win = QWidget()
my_win.show()
my_win.resize(400, 200)

my_win.setWindowTitle("Winner identifier")

label = QLabel("Click to find out the winner")
label1 = QLabel("?")

button = QPushButton("Generate")
button.clicked.connect(generate_random)

layout = QVBoxLayout()
my_win.setLayout(layout)  # la hoved vindu ha vertikal layout.

# pyqt5
layout.addWidget(label, alignment=Qt.AlignCenter)
layout.addWidget(label1, alignment=Qt.AlignCenter)
layout.addWidget(button, alignment=Qt.AlignCenter)

# pyqt6
# layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
# layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
# layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)


app.exec()
