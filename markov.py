from dictogram import Dictogram
from random import randrange

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, 
        # "fish": {"two":1, "red":1, "blue":1}, 
        # "two": {"fish":1}, 
        # "red": {"fish":1}, 
        # "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        sentence = []

        word = list(self.markov_chain.keys())[randrange(len(self.markov_chain))]
        sentence.append(word)

        while len(sentence) < num_words:
            word = self.markov_chain[word].sample()
            sentence.append(word)

        return ' '.join(sentence)


    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)




# markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
# markov_chain.print_chain()
# print(markov_chain.walk(10))