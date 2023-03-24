class IterInt(int):
    def __iter__(self):
        self.copy_number = self
        return self
    def __next__(self):
        if self.copy_number == 0:
            raise StopIteration
        last_digit = self.copy_number % 10
        self.copy_number = self.copy_number // 10
        return last_digit

n = IterInt(123)
for digit in n:
    print(digit)