"""
Write a program that generates a winner's number in a drawing.

1. When you start the program, a 400x200 window appears. The title of the window is Winner Generator.

2. There should be widgets in the program window:
- the label "Click to find out the winner",
- a blank for the winner's number "?",
- the "Generate" button.

3. After pressing the button:
- the first label should change to "Winner:",
- a random number from 1 to 100 should appear in place of the blank.

The program should work until the user clicks on the red x
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from random import randint



app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Winner Identifier')
my_win.move(100, 100)
my_win.resize(400, 200)

# window widgets: button and label
button = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')

# widget layout
line = QHBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)


# function that generates and displays a number
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Winner:')


# button click processing
button.clicked.connect(show_winner)

my_win.show()
app.exec_()
