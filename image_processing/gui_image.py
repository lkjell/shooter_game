#gui_image.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QFileDialog

from pathlib import Path

from image_processing.imagelib import ImageProcess

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Image editor')
my_win.move(500, 200)
my_win.resize(700, 600)

folder_btn = QPushButton("Folder")
image_list = QListWidget()


def chooseWorkingDir():
    workdir = QFileDialog.getExistingDirectory()
    return workdir


def find_image_files(files, extensions):
    result = [f for f in files if f.suffix in extensions]

    return result


cwd = Path("./")


def showFilenameList():
    extensions = [".jpg", ".jpeg", ".png", ".webp"]

    global cwd
    cwd = Path(chooseWorkingDir())  # current working directory
    filenames = cwd.iterdir()

    filenames = find_image_files(filenames, extensions)
    image_list.clear()
    for f in filenames:
        image_list.addItem(str(f.name))


image_process = None


def select_image(image_name):
    image_path = str(cwd / image_name)
    global image_process
    image_process = ImageProcess(image_path, image_area)
    image_process.show()

    black_and_white_btn.clicked.connect(image_process.grey)
    left_btn.clicked.connect(image_process.rotate_90)
    right_btn.clicked.connect(image_process.rotate_270)
    mirror_btn.clicked.connect(image_process.mirror)


folder_btn.clicked.connect(showFilenameList)
image_list.currentTextChanged.connect(select_image)

# layout 1
list_layout = QVBoxLayout()
list_layout.addWidget(folder_btn)
list_layout.addWidget(image_list)

left_btn = QPushButton("Left")
right_btn = QPushButton("Right")
mirror_btn = QPushButton("Mirror")
sharpness_btn = QPushButton("Sharpness")
black_and_white_btn = QPushButton("B&W")
save_btn = QPushButton("Save")

# layout 2
button_layout = QHBoxLayout()
button_layout.addWidget(left_btn)
button_layout.addWidget(right_btn)
button_layout.addWidget(mirror_btn)
button_layout.addWidget(sharpness_btn)
button_layout.addWidget(black_and_white_btn)
button_layout.addWidget(save_btn)

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
