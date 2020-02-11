from random import randint
# text = 'one fish two fish red fish blue fish'
# histogram = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

def sample(histogram):
  count_sum = 0
  start = 0
  end = 0
  
  for word in histogram.keys():
    count_sum += histogram[word]

  rand_index = randint(0, count_sum - 1)
  
  for word, count in histogram.items():
    end = start + count
    
    if rand_index in range(start+end):
      return word
    else:
      start = end