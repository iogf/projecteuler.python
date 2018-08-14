# Obs: Run on python3.

# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

ctz_formulae = lambda num: 3 * num + 1 if num % 2 else num // 2 

class Collatz:
    def __init__(self):
        self.ctz_nums = {}

    def ctz_chain(self, num):
        return self.ctz_nums.setdefault(num, self.calc_chain(num))

    def calc_chain(self, num):
        count = 1

        while num > 1:
            num = ctz_formulae(num)
            try:
                return count + self.ctz_nums[num]
            except KeyError:
                count = count + 1
        return count
    
    def max_chain(self, lim):
        num, max = 1, 1

        for ind in range(1, lim):
            count = self.ctz_chain(ind)
            if count > max:
                num, max = ind, count
        return num, max

if __name__ == '__main__':
    ctz = Collatz()

    print('Result:', ctz.max_chain(1000000))

