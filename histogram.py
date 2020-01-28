text = "Who here’s ever failed? And no one raised their hand in the whole fuckin’ room. So I pause and I said, I know you’re out there, I can hear your hearts beating. Who here has ever failed? And I demanded an answer and then a few people raised their hand. I said, who here’s ever failed? And now they all started complying. So I said great, when you failed, why did you fail? And they said all the things you said. Didn’t have enough time. Didn’t have the right technology. Didn’t have the money. Didn’t have the contacts. You know, had the wrong people. The people said we had the wrong leader, right? And then this voice in the darkness, the whole room was pitch black, says I didn’t have enough Supreme Court Justices. And I looked down and it’s Vice President, Al Gore. Who you probably don’t know much about American politics, but he and Bush Jr., they tied basically. It had to go to a Supreme Court to decide who’s gonna be it and he lost. And when he said that we were in northern California, which is all Democrats, would’ve been supporters of his, they all stood up and gave him a standing ovation when he said this. So when they stopped the standing ovation I said, that’s one way to try to explain why you didn’t become President of the United States. But I wouldn’t say it’s an accurate one. And there was this pause, like what the fuck is he about to say? And I said, ’cause let’s just do this logically. Everything you people have told me, I didn’t have the technology, I didn’t have the right contacts, I didn’t have the time, I didn’t have money. Everything you’ve told me, I didn’t have enough Supreme Court Justices, those are resources. And so you’re telling me, I failed ’cause I didn’t have the resources. And I’m here to tell you what you already know. Resources are never the problem, it’s a lack of resourcefulness is why you failed. Because the ultimate resources are emotional states. Creativity, decisiveness, passion, honesty, sincerity, love, these are the ultimate human resources. And when you engage these resources you can get any other resource on earth. Resourcefulness is the ultimate resource. And if you don’t have what you want, stop telling yourself a story because you don’t have the money, you don’t have the time, that’s bullshit. It’s because you haven’t committed yourself where you would burn your boats. If you want to take the fuckin’ island, burn your fuckin’ boats and you will take the island. ‘Cause people when they’re gonna either die or succeed, tend to succeed." # Tony Robins speach excerpt
words = text.split()


def generate_histogram(text):
    histogram = {}
    for word in text:
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


histogram = generate_histogram(words)
unique_words = get_unique_words(histogram)




print('------------------ ALL WORD FREQUENCIES ------------------')
print(histogram)

print('------------------ UNIQUE WORDS ------------------')
print(unique_words)