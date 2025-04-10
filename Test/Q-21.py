class Father:
    def __init__(self):
        self.father_name = "Mr. Papa Saini"
        self.father_hobby = "Gardening"

class Mother:
    def __init__(self):
        self.mother_name = "Mrs. Mummy Saini"
        self.mother_hobby = "Cooking"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Rahul"

    def show_family(self):
        print(f"Child: {self.child_name}")
        print(f"Father: {self.father_name}, Hobby: {self.father_hobby}")
        print(f"Mother: {self.mother_name}, Hobby: {self.mother_hobby}")

# Example usage
c = Child()
c.show_family()