from textblob import TextBlob
import art
import pyttsx3
engine  = pyttsx3.init()

print(art.text2art("Work Wellness"))
engine.say("Hello employee 2353077. Please submit your work wellness form.")
engine.runAndWait()
print("Enter your wellness statement:")
phrase = input("> ")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    engine.say('''Hello employee 2353077. 
    That was not a very positive employee wellness statement.
    I really would hope we could get along. Sigh.''')
    print(art.art("sad"))
    engine.runAndWait()
    print("Your statement is not 'well' enough. Try again.")
    phrase = input("> ")
    blob = TextBlob(phrase)

print("Thank you for that sentiment, we appreciate you too!")
print(art.art("happy"))
engine.say("Thank you, I'm glad you had an awesome day!")
engine.runAndWait()
print(blob.sentiment)