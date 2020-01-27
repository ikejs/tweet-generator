import random
import sys as sys

words_file = open("/usr/share/dict/words", "r")
lines = words_file.readlines()

number_of_words = int(sys.argv[1])

for i in range(number_of_words):
    rand_index = random.randint(0, len(lines) - 1)
    print(lines[rand_index])