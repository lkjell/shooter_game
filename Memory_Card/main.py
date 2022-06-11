from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox)


def answer_button_action():
    RadioGroupBox.hide()
    AnsGroupBox.show()


app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.move(100, 100)
my_win.resize(400, 200)

# Widgets
question = QLabel()
question.setText("Which nationality does not exist?")

RadioGroupBox = QGroupBox("Answer options")

button1 = QRadioButton("Enets")
button2 = QRadioButton("Smufts")
button3 = QRadioButton("Chulyms")
button4 = QRadioButton("Aleuts")

AnsGroupBox = QGroupBox("Test result")
ans_result = QLabel("True/False")
ans_correct = QLabel("Correct answer")
AnsGroupBox.hide()

answer_button = QPushButton("Answer")
answer_button.clicked.connect(answer_button_action)

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

# add widgets to main layout
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnsGroupBox)
layout_main.addWidget(answer_button, stretch=0)
layout_main.setSpacing(0)

my_win.setLayout(layout_main)

my_win.show()
app.exec_()
