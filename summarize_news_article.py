import tkinter as tk
import nltk
import requests
from textblob import TextBlob
from newspaper import Article

nltk.download("punkt")

def summarize():

    url=utext.get("1.0", "end").strip()


    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    pubdate.config(state="normal")
    summary_box.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)

    author.delete("1.0", "end")
    author.insert("1.0", article.authors)

    pubdate.delete("1.0", "end")
    pubdate.insert("1.0", article.publish_date)

    summary_box.delete("1.0", "end")
    summary_box.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete("1.0", "end")
    sentiment.insert("1.0", f'Polarity: {analysis.polarity},Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state="disabled")
    author.config(state="disabled")
    pubdate.config(state="disabled")
    summary_box.config(state="disabled")
    sentiment.config(state="disabled")

    #print(f'Title: {article.title}')
    #print(f'Authors: {article.authors}')
    #print(f'Publication Date: {article.publish_date}')
    #print(f'Summary: {article.summary}')

    analysis = TextBlob(article.text)
    #print(analysis.polarity)
    #print(f'Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


#GUI
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1000x600")

tklabel = tk.Label(root, text="Title")
tklabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

atlabel = tk.Label(root, text="Author")
atlabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

publabel = tk.Label(root, text="Publication Date")
publabel.pack()

pubdate = tk.Text(root, height=1, width=140)
pubdate.config(state="disabled", bg="#dddddd")
pubdate.pack()

sumlabel = tk.Label(root, text="Summary")
sumlabel.pack()

summary_box = tk.Text(root, height=20, width=140)
summary_box.config(state="disabled", bg="#dddddd")
summary_box.pack()

sentlabel = tk.Label(root, text="Sentiment")
sentlabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn_submit = tk.Button(root, text= "Summarize", command=summarize)
btn_submit.pack()

print("hi")
root.mainloop()
