import sys as sys
import random

if __name__ == "__main__":
    words = sys.argv[1:]
for word in words:
    rand_index = random.randint(0, len(words) - 1)
    print(words[rand_index])