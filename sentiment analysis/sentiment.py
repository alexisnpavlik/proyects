'''A brief explanation of sentiment analysis.
    Polarity: the sentiment analysis will have a scale of polarity -1 meaning
    a bad sentiment, 0 meaning neutral sentiment and 1 meaning a relly good sentiment
    Subjectivity: also a subjectivity analysis will be given, 0 meaning that are facts 
    what's beeing given and 1 meaning that's a personal opinion what's beeing given'''


from textblob import TextBlob #sentiment analysis library
import matplotlib.pyplot as plt #graphs


#due to it's only one value that it's been returned no graph needed
# def graphs(polarity_l:list, subjectivity_l:list):
#     try:
#         plt.plot(polarity_l, c = 'blue', label= "polarity") #graph polarity with blue
#         plt.plot(subjectivity_l, c = "orange", label = "subjectivity") #graph subjectivity with orange
#         plt.legend()
#         plt.show() #showing the graph
#     except ValueError as ve:
#         print(ve)


def analysis(article:str):
    try:
        text = TextBlob(article)
        en_text = text.translate(to="en") #due to article is given in Spanish I've to transalte it to english
        polarity = en_text.sentiment.polarity #polarity of the article
        subjectivity = en_text.sentiment.subjectivity #subjectivity of the article
        #print(english) #print to see the translation
        print(f"Polarity analysis: {polarity}" + 
                f"\nSubjectivity analysis: {subjectivity}") #print to see the sentiment analysis
        return polarity, subjectivity
    except ValueError as ve:
        print(ve)