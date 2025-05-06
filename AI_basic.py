from tkinter import *
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    text = entry.get()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        result_label.config(text="Sentiment: Positive")
    elif sentiment < 0:
        result_label.config(text="Sentiment: Negative")
    else:
        result_label.config(text="Sentiment: Neutral")

# GUI setup
window = Tk()
window.title("AI Sentiment Analyzer")

Label(window, text="Enter a sentence:").pack(pady=10)
entry = Entry(window, width=50)
entry.pack(pady=5)

Button(window, text="Analyze", command=analyze_sentiment).pack(pady=10)
result_label = Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

window.mainloop()
