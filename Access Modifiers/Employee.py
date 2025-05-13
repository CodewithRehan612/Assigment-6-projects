class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

# Example usage:
if __name__ == "__main__":
    emp = Employee("John", 50000, "123-45-6789")
    print(emp.name)        # Public: Accessible
    print(emp._salary)     # Protected: Accessible, but by convention should not be accessed directly
    try:
        print(emp.__ssn)   # Private: Will raise AttributeError
    except AttributeError as e:
        print(f"Error: {e}")
    # Accessing private variable using name mangling
    print(emp._Employee__ssn)  # Accessible via name mangling 