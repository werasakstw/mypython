class Student():
    count = 0
    def __init__(self, name, dep, gpa):
        Student.count += 1
        self.sid = Student.count
        self.name = name
        self.dep = dep
        self.gpa = gpa
    def __repr__(self):
        return self.name
