from flask import Flask, request, render_template
from markov import MarkovChain
app = Flask(__name__)


@app.route('/')
def generate_words():
  textFile = open('./text.txt')
  text = textFile.read().split()
  chain = MarkovChain(text)
  sentence = chain.walk(20).capitalize() + '.'
  return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
  app.run()