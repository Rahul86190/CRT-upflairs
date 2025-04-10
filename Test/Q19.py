class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

# Example
s1 = Student("Rahul", 80)
print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())