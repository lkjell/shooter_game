from random import shuffle
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox, QButtonGroup)

questions_db = [
    ("Which nationality does not exist?", "Smufts", "Enets", "Chulyms", "Aleuts"),
    ("Who is coolest?", "Me", "You", "John", "Mia"),
    ("Which is a country?", "Spain", "Paris", "Oslo", "Moon"),
    ("Where is hottest?", "Sun", "Earth", "Moon", "Jupiter"),
    ("What color comes first in the rainbow?", "Red", "Yellow", "Purple", "Green"),
    ("What is not alive?", "France", "Fox", "Bird", "Snake"),
    ('This is a copy of a Kahoot question?.', 'YESSSSS', 'ok', 'NOOOOOOO', ':)'),
]

question_index = 0

# class Question:
#     def __init__(self, text, r, w1, w2, w3):
#         self.text = text
#         self.right = r
#         self.wrong1 = w1
#         self.wrong2 = w2
#         self.wrong3 = w3
#
#
# questions_db = [Question("Who is coolest?", "Me", "You", "John", "Mia"),
#                 Question("Which is a country?", "Spain", "Paris", "Oslo", "Moon"),]


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer_button.setText("Next question")


def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer_button.setText("Answer")

    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)


#
def ask(question_text, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    ans_correct.setText(right_answer)
    question.setText(question_text)


# Check if you have pressed the correct button
def check_answer():
    if answers[0].isChecked():
        ans_result.setText("Correct!")
        # ans_correct.setText("Correct answer.")
        show_result()
    else:
        for a in answers[0:]:
            if a.isChecked():
                ans_result.setText("Incorrect!")
                # ans_correct.setText("Incorrect answer.")
                show_result()
                break


def start_test():
    if answer_button.text() == "Answer":
        check_answer()
    else:
        show_questions()
        global question_index
        question_index += 1
        if question_index >= len(questions_db):
            question_index = 0

        ask(*questions_db[question_index])


app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.move(500, 500)
my_win.resize(400, 200)

# Widgets
question = QLabel()
question.setText("Which nationality does not exist?")

RadioGroupBox = QGroupBox("Answer options")

button1 = QRadioButton("Enets")
button2 = QRadioButton("Smufts")
button3 = QRadioButton("Chulyms")
button4 = QRadioButton("Aleuts")
answers = [button1, button2, button3, button4]

RadioGroup = QButtonGroup()
for btn in answers:
    RadioGroup.addButton(btn)
# RadioGroup.addButton(button1)
# RadioGroup.addButton(button2)
# RadioGroup.addButton(button3)
# RadioGroup.addButton(button4)

AnsGroupBox = QGroupBox("Test result")
ans_result = QLabel("True/False")
ans_correct = QLabel("Correct answer")
AnsGroupBox.hide()

answer_button = QPushButton("Answer")
answer_button.clicked.connect(start_test)

# init questions
# ask("Who is coolest", "Me", "You", "You", "You1")
# ask(questions_db[0][0],
#     questions_db[0][1],
#     questions_db[0][2],
#     questions_db[0][3],
#     questions_db[0][4])

ask(*questions_db[question_index])

# Layout

# Layout radio button
# Layout radio button part 1
layoutv1 = QVBoxLayout()
layoutv1.addWidget(button1)
layoutv1.addWidget(button2)

# Layout radio button part 2
layoutv2 = QVBoxLayout()
layoutv2.addWidget(button3)
layoutv2.addWidget(button4)

# Layout radio button both parts
layout_radiobutton = QHBoxLayout()
layout_radiobutton.addLayout(layoutv1)
layout_radiobutton.addLayout(layoutv2)

RadioGroupBox.setLayout(layout_radiobutton)

# Layout answer group box
layoutv_ans = QVBoxLayout()
layoutv_ans.addWidget(ans_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layoutv_ans.addWidget(ans_correct, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(layoutv_ans)

# Layout answer button
layouth_ans_button = QHBoxLayout()
layouth_ans_button.addStretch(2)
layouth_ans_button.addWidget(answer_button, 1)
layouth_ans_button.addStretch(2)

# add widgets to main layout
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnsGroupBox)
layout_main.addLayout(layouth_ans_button)
# layout_main.addWidget(answer_button, stretch=0)
# layout_main.setSpacing(0)

my_win.setLayout(layout_main)

my_win.show()
app.exec_()
