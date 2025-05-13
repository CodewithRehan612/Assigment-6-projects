class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage:
if __name__ == "__main__":
    logger = Logger()
    del logger  # Explicitly destroy the object to see the destructor message 