
# 09. Reusing code and data with a class Fibonacci

# simple Fibonacci series
# the sum of two elements defines the next set

class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # A generator function that generates an iterator
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0,1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')

