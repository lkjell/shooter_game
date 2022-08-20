from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox)

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.move(100, 100)
my_win.resize(400, 200)

button1 = QPushButton("Hei")
button2 = QPushButton("Hei")
button3 = QPushButton("Hei")

# add widgets to main layout
layout_main = QHBoxLayout()
layout_main.addWidget(button1, stretch=1)
layout_main.addStretch(1)
layout_main.addWidget(button2, stretch=1)
layout_main.addWidget(button3, stretch=1)

# layout_main.setSpacing(0.2)
# layout_main.setStretch(5, 5)


my_win.setLayout(layout_main)

my_win.show()
app.exec_()
