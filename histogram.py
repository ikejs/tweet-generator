def generate_histogram(text):
    words = text.split()
    histogram = {}
    for word in words:
        word = word.rstrip()
        if word in histogram.keys():
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def get_unique_words(histogram):
    unique_words = []
    for word in histogram:
        if histogram[word] == 1:
            unique_words.append(word)
    return unique_words


# histogram = generate_histogram(words)
# unique_words = get_unique_words(histogram)




# print('------------------ ALL WORD FREQUENCIES ------------------')
# print(histogram)

# print('------------------ UNIQUE WORDS ------------------')
# print(unique_words)