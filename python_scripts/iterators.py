class factorial_test():
    def __iter__(self):
        self.n = 1
        self.c = 1
        return(self)
    def __next__(self):
        if self.c <= 100:
            x = self.n
            self.c += 1
            self.n *= self.c
            return(x)
        else:
            raise StopIteration

test_var = factorial_test()
iter_obj = iter(test_var)

while True:
    print(next(iter_obj))
