class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage:
if __name__ == "__main__":
    m = Multiplier(3)
    print(callable(m))      # Should print True
    print(m(10))            # Should print 30 