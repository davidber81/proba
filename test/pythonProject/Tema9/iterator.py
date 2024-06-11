class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.i, self.a, self.b = 0, start, end
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i % 2 == 0:
            if self.a > self.b:
                raise StopIteration
            result = self.a
            self.a, self.b = self.a + 2, self.b
            return result
        else:
            self.a += 0
            return self.__next__()
    def __str__(self):
        return f'EvenNumbers({self.a}, {self.b})'

en = EvenNumbers(start=10, end=25)
print(en)
for val in en:
    print(val)

