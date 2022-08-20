from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QGroupBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

app = QApplication([])
my_win = QWidget()
my_win.show()
my_win.resize(400, 200)

my_win.setWindowTitle("Memory card")
layout = QVBoxLayout()
my_win.setLayout(layout)

radioGroupBox = QGroupBox("Options")
rbtn1 = QRadioButton("Enets")
rbtn2 = QRadioButton("Smurfs")
rbtn3 = QRadioButton("Chulyms")
rbtn4 = QRadioButton("Aleuts")

hlayout1 = QHBoxLayout()
hlayout2 = QHBoxLayout()
vlayout1 = QVBoxLayout()

hlayout1.addWidget(rbtn1)
hlayout1.addWidget(rbtn3)
hlayout2.addWidget(rbtn2)
hlayout2.addWidget(rbtn4)

vlayout1.addLayout(hlayout1)
vlayout1.addLayout(hlayout2)

question = QLabel("Which nationality does not exist?")

layoutanswer = QHBoxLayout()
answerbutton = QPushButton("Answer")
layoutanswer.addStretch(2)
layoutanswer.addWidget(answerbutton)
layoutanswer.addStretch(2)

radioGroupBox.setLayout(vlayout1)

resultGroupBox = QGroupBox("Result")
result_layout_v = QVBoxLayout()
result_text = QLabel("Correct")
result_layout_v.addWidget(result_text, alignment=(Qt.AlignBottom | Qt.AlignCenter))
resultGroupBox.setLayout(result_layout_v)
resultGroupBox.hide()

layout.addWidget(question, alignment=Qt.AlignCenter)
layout.addWidget(radioGroupBox)
layout.addWidget(resultGroupBox)
layout.addLayout(layoutanswer)


def show_result():
    radioGroupBox.hide()
    resultGroupBox.show()
    answerbutton.setText("Next question")


def show_questions():
    radioGroupBox.show()
    resultGroupBox.hide()
    answerbutton.setText("Answer")


def start_test():
    if answerbutton.text() == "Answer":
        show_result()
    else:
        show_questions()


answerbutton.clicked.connect(start_test)

# layout.addWidget(rbtn1)
# layout.addWidget(rbtn2)
# layout.addWidget(rbtn3)
# layout.addWidget(rbtn4)


app.exec()
