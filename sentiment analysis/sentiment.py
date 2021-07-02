'''A brief explanation of sentiment analysis.
    Polarity: the sentiment analysis will have a scale of polarity -1 meaning
    a bad sentiment, 0 meaning neutral sentiment and 1 meaning a relly good sentiment
    Subjectivity: also a subjectivity analysis will be given, 0 meaning that are facts 
    what's beeing given and 1 meaning that's a personal opinion what's beeing given'''


from textblob import TextBlob #sentiment analysis library


def analysis(paragraph):
    text = TextBlob(paragraph)
    english = text.translate(to="en") #article given is Spanish I've to transalte it to english
    #print(english) #print to see the translation
    print(english.sentiment,"\n") #print to see the sentiment analysis
