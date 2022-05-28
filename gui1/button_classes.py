"""
The developer Kirill was getting ready to work with PyQt and created a Button class.
The program creates and displays an "ok" button at (100, 100). Then the button hides.

Class fields:
- a label on the title button,
- the x, y coordinates of the button,
- the visibility of the appearance button (by default, the widget is visible).

Class methods:
- a constructor that creates a button object,
- the hide method, which hides the button,
- the show method, which shows the button.

Correct the errors in the design of the program. It should work like the picture.

"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Button:
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True

    def hide(self):
        self.appearance = False

    def show(self):
        self.appearance = True

    def print_status(self):
        print('Widget data:')
        print(self.title, self.x, self.y, self.appearance)


ok_button = Button('ok', 100, 100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()

