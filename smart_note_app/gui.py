import os
import json
from random import shuffle, randrange
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QMessageBox, QGroupBox, QButtonGroup)

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QInputDialog

note_db = {}
tag_db = {}

app = QApplication([])

# main window:
my_win = QWidget()
my_win.setWindowTitle('Note app')
my_win.move(500, 200)
my_win.resize(700, 600)

# Create note layout
note_label = QLabel("List of notes")
note_list = QListWidget()
create_note_btn = QPushButton("Create note")
delete_note_btn = QPushButton("Delete note")
save_note_btn = QPushButton("Save note")

note_create_delete_layout = QHBoxLayout()
note_create_delete_layout.addWidget(create_note_btn)
note_create_delete_layout.addWidget(delete_note_btn)

note_layout = QVBoxLayout()
note_layout.addWidget(note_label)
note_layout.addWidget(note_list)
note_layout.addLayout(note_create_delete_layout)
note_layout.addWidget(save_note_btn)


# note functionality
def add_note():
    note_name, result = QInputDialog.getText(my_win, "Add note", "Note name:")
    if result and note_name != "" and note_name not in note_db:
        note_db[note_name] = {"text": "", "tags": []}
        note_list.addItem(note_name)

    if not note_list.selectedItems():
        note_list.setCurrentRow(0)
    else:
        note_list.setCurrentRow(len(note_list) - 1)


def delete_note():
    if note_list.selectedItems():
        key = note_list.selectedItems()[0].text()
        del note_db[key]
        tag_list.clear()
        row = note_list.currentRow()
        note_list.takeItem(row)

        with open("note_db.json", "w") as f:
            json.dump(note_db, f, indent=2)


def save_note():
    if note_list.selectedItems():
        key = note_list.selectedItems()[0].text()
        note_db[key]["text"] = note_text_edit.toPlainText()

    save_note_()


def save_note_():
    with open("note_db.json", "w") as f:
        json.dump(note_db, f, indent=2, ensure_ascii=False)
        print("Saving")


create_note_btn.clicked.connect(add_note)
delete_note_btn.clicked.connect(delete_note)
save_note_btn.clicked.connect(save_note)

# Create tag layout

tag_label = QLabel("List of tags")
tag_list = QListWidget()
create_tag = QLineEdit("")
create_tag.setPlaceholderText("Enter tag...")
add_tag2note_btn = QPushButton("Add tag")

untag_from_note_btn = QPushButton("Untag from note")
search_tag_btn = QPushButton("Search note by tag")

tag_create_delete_layout = QHBoxLayout()
tag_create_delete_layout.addWidget(add_tag2note_btn)
tag_create_delete_layout.addWidget(untag_from_note_btn)

tag_layout = QVBoxLayout()
tag_layout.addWidget(tag_label)
tag_layout.addWidget(tag_list)
tag_layout.addWidget(create_tag)
tag_layout.addLayout(tag_create_delete_layout)
tag_layout.addWidget(search_tag_btn)


def add_tag():
    if not note_list.selectedItems():
        return

    key = note_list.selectedItems()[0].text()
    tag_name = create_tag.text()
    tags = note_db[key]["tags"]

    if tag_name != "" and tag_name not in tags:
        tags.append(tag_name)
        tag_list.addItem(tag_name)
        save_note_()


def untag():
    if not note_list.selectedItems():
        return

    if not tag_list.selectedItems():
        return

    note_name = note_list.selectedItems()[0].text()
    tag_name = tag_list.selectedItems()[0].text()
    tags = note_db[note_name]["tags"]
    tags.remove(tag_name)

    row = tag_list.currentRow()
    tag_list.takeItem(row)

    save_note_()


def load_note_db():
    try:
        with open("note_db.json", "r") as f:
            global note_db
            note_db = json.load(f)
            print("Loading")

        for note_name in note_db:
            note_list.addItem(note_name)

        note_list.setCurrentRow(0)

    except Exception as e:
        print(e)
        pass


def select_note(note_name):
    try:
        tags = note_db[note_name]["tags"]
        note_text = note_db[note_name]["text"]
        note_text_edit.setText(note_text)

        tag_list.clear()
        for t in tags:
            tag_list.addItem(t)
    except KeyError:
        pass


def search_note():
    tag_name = create_tag.text()

    note_list.clear()
    if tag_name == "":
        for note_name in note_db:
            note_list.addItem(note_name)
    else:
        for note_name, value in note_db.items():
            tags = value["tags"]
            if tag_name in tags:
                note_list.addItem(note_name)


def textChanged():
    if not note_list.selectedItems():
        return

    save_note()


note_list.currentTextChanged.connect(select_note)

add_tag2note_btn.clicked.connect(add_tag)
untag_from_note_btn.clicked.connect(untag)
search_tag_btn.clicked.connect(search_note)

# Create note text edit
note_text_edit = QTextEdit()
note_text_edit.textChanged.connect(textChanged)

layout_note_tag = QVBoxLayout()
layout_note_tag.addLayout(note_layout)
layout_note_tag.addLayout(tag_layout)

layout_main = QHBoxLayout()
layout_main.addWidget(note_text_edit, stretch=2)
layout_main.addLayout(layout_note_tag, stretch=1)

my_win.setLayout(layout_main)

load_note_db()
my_win.show()
app.exec_()
