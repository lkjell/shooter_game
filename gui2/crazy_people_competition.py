"""
Write a program that asks a multiple-choice question.

1. When you start the program, a 400x200 window appears. The heading for the window is “Competition from Crazy People.”

2. There should be widgets in the program window:
- a label with the question "In what year did the channel receive the "gold play button" from YouTube?"
- 4 radio buttons with answer options: "2005," "2010," "2015," "2020."
The widgets should be arranged as shown in the picture.

3. When clicking the mouse:
- A new window should appear on the radio button labeled “2005” with the notification: “Correct! You win a gyro scooter."
- On any other switch, it's a window with the notification: “No, it was 2015. You win a company poster."

The program should run until the user clicks on the "red x" in the question window.

"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox)


def show_win():
    win = QMessageBox()
    win.setText("Correct\nYou win a gyro scooter")
    win.exec_()


def show_lose():
    win = QMessageBox()
    win.setText("Wrong\nIt was 2015")
    win.exec_()


app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Winner Identifier')
my_win.move(100, 100)
my_win.resize(400, 200)

# window widgets: button and label
text = QLabel('What year did the channel received the "golden play button" from YouTube?')

button1 = QRadioButton("2005")
button2 = QRadioButton("2010")
button3 = QRadioButton("2015")
button4 = QRadioButton("2020")

# widget layout
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)

# add radio button layout
layouth1 = QHBoxLayout()
layouth2 = QHBoxLayout()

# group two radio button togetherY
layouth1.addWidget(button1, alignment=Qt.AlignCenter)
layouth1.addWidget(button2, alignment=Qt.AlignCenter)

layouth2.addWidget(button3, alignment=Qt.AlignCenter)
layouth2.addWidget(button4, alignment=Qt.AlignCenter)

line.addLayout(layouth1)
line.addLayout(layouth2)

button1.clicked.connect(show_lose)
button2.clicked.connect(show_lose)
button3.clicked.connect(show_win)
button4.clicked.connect(show_lose)

my_win.setLayout(line)

my_win.show()
app.exec_()
