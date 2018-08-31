from flask import Flask, request, render_template
import feedparser
url = request.form['url']
dic = {}
url = 'https://www.google.co.in/search?&q=filetype%3Apdf+2014+india+election&num=100'
data = feedparser.parse(url)
print(data)