class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

# Example usage:
if __name__ == "__main__":
    engine = Engine()
    car = Car(engine)
    car.start_engine() 