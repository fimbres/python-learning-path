class Generador:
    def __init__(self) -> None:
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 10:
            raise StopIteration
        result = self.i**2
        self.i += 1
        return result