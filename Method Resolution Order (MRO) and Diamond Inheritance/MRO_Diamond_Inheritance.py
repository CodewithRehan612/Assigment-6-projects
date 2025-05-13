class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Example usage:
if __name__ == "__main__":
    d = D()
    d.show()  # Observe MRO
    print(D.__mro__)  # Print the MRO 