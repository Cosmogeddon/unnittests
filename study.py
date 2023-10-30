class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not name_characters.issuperset(major):
            raise ValueError
        if gpa and not isinstance(gpa, float):
            raise ValueError
        if (gpa<0.0) or (gpa>4.0):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

print(Student('Kelderman', 'Cody', 'CIS', 4.0))
print(Student('Kelderman', 'Max', 'Aviation', 3.0))