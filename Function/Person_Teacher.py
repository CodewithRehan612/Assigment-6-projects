class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage:
if __name__ == "__main__":
    t = Teacher("Alice", "Mathematics")
    print(f"Name: {t.name}, Subject: {t.subject}") 