# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

def rotations(num):
    nstr = str(num)
    for ind in range(0, len(nstr)):
        nstr = nstr[1:] + nstr[:1]
        yield int(nstr)

class PrimeSeq:
    def __init__(self, max):
        self.seq = [2, 3]
        self.update(max)

    def update(self, max):
        start = self.seq[-1] + 2

        for ind in range(start, max, 2):
            self.feed(ind)

    def is_prime(self, num):
        self.update(num)
        return num in self.seq

    def feed(self, num):
        """
        Called just by update.
        """
        for ind in self.seq:
            if num % ind == 0:
                return False
        self.seq.append(num)
        return True

    def is_circular(self, num):
        for ind in rotations(num):
            if not self.is_prime(ind):
                return False
        return True
    
    def __iter__(self):
        return iter(self.seq)

def calc():
    count = 0
    seq = PrimeSeq(1000000)
    for ind in seq:
        if seq.is_circular(ind):
            count = count + 1
    print("Result:", count)

if __name__ == "__main__":
    calc()

