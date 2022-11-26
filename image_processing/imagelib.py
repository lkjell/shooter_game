#imagelib.py
# package name is PILLOW
from PIL import Image, ImageQt
from PIL import ImageFilter
from copy import copy

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import numpy as np


class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.image_original = None
        self.image = None
        self.history = []

    def open(self):
        try:
            self.image_original = Image.open(self.filename)
            self.image = self.image_original
            self.history.append(self.image_original)
        except FileNotFoundError:
            print("File not found!")

    def show(self):
        if self.image is None:
            self.open()

        self.image.show()

    def grey(self):
        if self.image is None:
            self.open()

        # self.image = self.image.convert("L")
        self.image = copy(self.image_original)
        self.image = self.image.convert("RGB")

        data = self.image.getchannel(0)
        data = tuple([tuple((d,0,0)) for d in data])
        # data[:, [1, 2]] = 0
        # data = tuple([tuple(d) for d in data])
        #
        self.image.putdata(data)

        #
        # x, y = self.image.size
        # for i in range(x):
        #     for j in range(y):
        #         pixel = self.image.getpixel((i, j))
        #         pixel = (pixel[0], 0, 0)
        #         self.image.putpixel((i, j), pixel)

        self.history.append(copy(self.image))

    def rotate_90(self):
        if self.image is None:
            self.open()

        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.history.append(copy(self.image))

    def blur(self):
        if self.image is None:
            self.open()

        self.image = self.image.filter(ImageFilter.BLUR)
        self.history.append(copy(self.image))

    def rotate_270(self):
        if self.image is None:
            self.open()

        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.history.append(copy(self.image))

    def mirror(self):
        if self.image is None:
            self.open()

        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.history.append(copy(self.image))

    def flip(self):
        if self.image is None:
            self.open()

        self.image = self.image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.history.append(copy(self.image))


class ImageProcess(ImageEditor):
    def __init__(self, filename, image_area):
        self.image_area = image_area
        super().__init__(filename)

    def show(self):
        # if self.image is None:
        self.open()
        self.show_()

    def show_(self):
        self.image_area.hide()
        # !Kjell se her
        image = ImageQt.ImageQt(self.image)
        pixmapimage = QPixmap.fromImage(image)

        w = self.image_area.width()
        h = self.image_area.height()
        self.pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.image_area.setPixmap(self.pixmapimage)
        self.image_area.show()

    def grey(self):
        super().grey()
        self.show_()

    def rotate_90(self):
        super().rotate_90()
        self.show_()

    def rotate_270(self):
        super().rotate_270()
        self.show_()

    def blur(self):
        super().blur()
        self.show_()

    def mirror(self):
        super().mirror()
        self.show_()

    def flip(self):
        super().flip()
        self.show_()


if __name__ == "__main__":
    imageEditor = ImageEditor("../images/original.jpg")
    imageEditor.grey()
    # imageEditor.mirror()
    # imageEditor.blur()
    imageEditor.show()
