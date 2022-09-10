import os
from random import shuffle, randrange
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox, QButtonGroup)

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Note app')
my_win.move(500, 200)
my_win.resize(700, 600)

# Create note layout
note_label = QLabel("List of notes")
note_list = QListWidget()
create_note = QPushButton("Create note")
delete_note = QPushButton("Delete note")
save_note = QPushButton("Save note")

note_create_delete_layout = QHBoxLayout()
note_create_delete_layout.addWidget(create_note)
note_create_delete_layout.addWidget(delete_note)

note_layout = QVBoxLayout()
note_layout.addWidget(note_label)
note_layout.addWidget(note_list)
note_layout.addLayout(note_create_delete_layout)
note_layout.addWidget(save_note)

# Create tag layout

tag_label = QLabel("List of tags")
tag_list = QListWidget()
create_tag = QLineEdit("")
create_tag.setPlaceholderText("Enter tag...")
add_tag2note = QPushButton("Add tag")
untag_from_note = QPushButton("Untag from note")
search_tag = QPushButton("Search note by tag")

tag_create_delete_layout = QHBoxLayout()
tag_create_delete_layout.addWidget(add_tag2note)
tag_create_delete_layout.addWidget(untag_from_note)

tag_layout = QVBoxLayout()
tag_layout.addWidget(tag_label)
tag_layout.addWidget(tag_list)
tag_layout.addWidget(create_tag)
tag_layout.addLayout(tag_create_delete_layout)
tag_layout.addWidget(search_tag)

# Create note text edit
note_text_edit = QTextEdit()

layout_note_tag = QVBoxLayout()
layout_note_tag.addLayout(note_layout)
layout_note_tag.addLayout(tag_layout)

layout_main = QHBoxLayout()
layout_main.addWidget(note_text_edit, stretch=2)
layout_main.addLayout(layout_note_tag, stretch=1)

my_win.setLayout(layout_main)

my_win.show()
app.exec_()
