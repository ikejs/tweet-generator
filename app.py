from flask import Flask, request
from histogram import generate_histogram
from sample_freqs import sample
from random import randint
app = Flask(__name__)

test_text = "testing test 123 12 123 test testing test"

@app.route('/')
def generate_words():
  sentence = ""
  histogram = generate_histogram(test_text)
  num = request.args.get('num')
  for i in range(0, int(num)):
    word = sample(histogram)
    sentence += word + " "

  return sentence


if __name__ == '__main__':
  app.run()