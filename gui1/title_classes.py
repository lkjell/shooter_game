"""
(1) Create a Title class with the following fields:
- the text of the label,
- the x coordinate,
- the y coordinate,
- the visibility of the label;
and these methods:
- a constructor,
- displaying information about the object,
- hiding the label (with output to the console " - hidden"),
- displaying the label (with output to the console " - displayed").

(2) Create two labels:
- "Find out the winner right now!" with this location (150, 50),
- "There can be only one winner" with this location (150, -100).

(3) Hide the label "There can be only one winner".

The program should work like in the picture.
"""


class Title:
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True

    def hide(self):
        self.appearance = False
        print(self.title, '- hidden')

    def show(self):
        self.appearance = False
        print(self.title, '- displayed')

    def print_info(self):
        print('Button:', self.title)
        print('Position:', '(' + str(self.x) + ',' + str(self.y) + ')')
        print('Visibility:', self.appearance)


main_title = Title('Find out the winner now!', 150, 50)
rules_title = Title('There can only be one winner', 150, -100)
main_title.print_info()
rules_title.print_info()
rules_title.hide()
