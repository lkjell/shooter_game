import os
import json
from random import shuffle, randrange
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox, QButtonGroup)

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QInputDialog

from imagelib import ImageFilter

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Image editor')
my_win.move(500, 200)
my_win.resize(700, 600)

folder_btn = QPushButton("Folder")
image_list = QListWidget()

# layout 1
list_layout = QVBoxLayout()
list_layout.addWidget(folder_btn)
list_layout.addWidget(image_list)

left_btn = QPushButton("Left")
right_btn = QPushButton("Right")
mirror_btn = QPushButton("Mirror")
sharpness_btn = QPushButton("Sharpness")
black_and_white_btn = QPushButton("B&W")

# layout 2
button_layout = QHBoxLayout()
button_layout.addWidget(left_btn)
button_layout.addWidget(right_btn)
button_layout.addWidget(mirror_btn)
button_layout.addWidget(sharpness_btn)
button_layout.addWidget(black_and_white_btn)

image_area = QLabel()

# layout 3
image_layout = QVBoxLayout()
image_layout.addWidget(image_area, 90)
image_layout.addLayout(button_layout)

# layout 4
layout_main = QHBoxLayout()
layout_main.addLayout(list_layout, 20)
layout_main.addLayout(image_layout, 80)

my_win.setLayout(layout_main)

my_win.show()
app.exec_()
