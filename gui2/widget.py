class Widget:
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y

    def print_info(self):
        print(f"Label: {self.title}")
        print(f"Location: {self.x} {self.y}")


class Button(Widget):
    def __init__(self, title, x, y, is_clicked):
        super(Button, self).__init__(title, x, y)
        self.is_clicked = is_clicked

    def click(self):
        self.is_clicked = True
        print("You are signed up")


w = Button("Participate", 100, 100, False)
w.print_info()

answer = input("Want to sign up? (yes/no)\n")

if answer == "yes":
    w.click()
elif answer == "no":
    print("That is a shame!")
