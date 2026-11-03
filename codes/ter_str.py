import itertools
import numpy as np

symbols = ['a', 'b', 'c']

# Generate all possible strings of length 5
all_strings = np.array(
    list(itertools.product(symbols, repeat=5))
)

# Check whether adjacent characters are equal
has_repeat = np.any(
    all_strings[:, :-1] == all_strings[:, 1:],
    axis=1
)

# Count strings satisfying the condition
total = len(all_strings)
count = np.sum(has_repeat)

print("Total possible strings:", total)
print("Strings containing aa, bb, or cc:", count)
print("Strings containing no aa, bb, or cc:", total - count)

