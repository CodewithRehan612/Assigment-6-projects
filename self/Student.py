class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example usage:
if __name__ == "__main__":
    student1 = Student("Alice", 90)
    student1.display() 