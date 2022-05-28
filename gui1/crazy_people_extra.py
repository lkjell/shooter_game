"""
Write a program that generates two random numbers between 0 and 9.

1. When the program starts, a 400x400 window appears. The title of the window is "Lottery".

2. There should be widgets in the program window:
- the label "Click to participate",
- two blanks for numbers "?"
- A "Try your luck" button.

3. After pressing the button:
- the first label should change to “You win! Play again" (the numbers are the same) or "You lose! Play again" (the numbers are not equal),
- numbers from 0 to 9 should appear in place of the blanks.

The program should work until the user clicks on the red x.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Drawing')
my_win.move(100, 100)
my_win.resize(400, 200)

# window widgets: button and label
button = QPushButton('Try your luck')
text = QLabel('Click to participate')
number1 = QLabel('?')
number2 = QLabel('?')

# widget layout
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(number1, alignment=Qt.AlignCenter)
line.addWidget(number2, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)


# function that generates and displays a number
def start_lottery():
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    number1.setText(str(n1))
    number2.setText(str(n2))
    if n1 == n2:
        text.setText('You win! Play again')
    else:
        text.setText('You lose! Play again')


# button click processing
button.clicked.connect(start_lottery)

my_win.show()
app.exec_()
