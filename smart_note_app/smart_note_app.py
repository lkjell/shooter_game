# database
pupil_db = []


class Pupil:
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def print_info(self):
        print(f"{self.name} {self.surname} {self.grade}")

    def __str__(self):
        return f"{self.name} {self.surname} {self.grade}"

    def __repr__(self):
        return f"{self.name} {self.surname}"

def parse_elev(s):
    name, surname, grade = s.split(" ")
    return name, surname, int(grade)


with open("elev.txt", "r") as f:
    for line in f:
        r = parse_elev(line)
        # pupil = Pupil(r[0], r[1], r[2])
        pupil = Pupil(*r)
        # pupil.print_info()
        pupil_db.append(pupil)


with open("elev1.txt", "w") as f:
    for pupil in pupil_db:
        print("{} {} {}".format(pupil.name, pupil.surname, pupil.grade), file=f)
