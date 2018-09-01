from flask import Flask, request, render_template, json
from flask import jsonify
import requests
import feedparser
app = Flask(__name__)



urls = ["http://feeds.feedburner.com/EducationWeekSpecialEducation",
"https://feeds.feedburner.com/EducationWeekNewsAndInformationAboutEducationIssues",
"http://feeds.feedburner.com/EdutopiaNewContent",
"http://www.forbes.com/education/index.xml",
"http://feeds.guardian.co.uk/theguardian/education/rss",
"http://scholasticadministrator.typepad.com/thisweekineducation/atom.xml",
"https://ei-ie.org/en/rss_themes/4/en.rss",
"http://edscoop.com/rss",
"http://mindshift.kqed.org/feed/",
"http://feeds.feedburner.com/EducationWeekUrbaneducation",
"http://www.eschoolnews.com/feed/",
"http://mbrooks888.blogspot.com/feeds/posts/default",
"http://euroboticsweekeducation.blogspot.com/feeds/posts/default",
"http://www.nytimes.com/services/xml/rss/nyt/Education.xml",
"http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/education/rss.xml",
"http://feeds.feedburner.com/EducationWeekBilingualeducation",
"http://www.npr.org/rss/rss.php?id=1013",
"http://www.fractuslearning.com/feed/",
"https://ei-ie.org/en/latestnews/rss",
"http://edtechreview.in/index.php?",]
''' "http://www.indiaeducation.net/rss/",
"https://www.indiatoday.in/education-today",
"http://www.educationtimes.com/rssfeedall/all",
"http://newsrack.in/extras/known-indian-feeds",
"http://www.indiatogether.org/c/education",
"https://www.hindustantimes.com/rss",
"http://indianexpress.com/syndication/",
"https://www.thehindu.com/education/schools/",'''

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method =='POST':
        url = request.form['url']
        dic = {}
        #url = url+'/feed'
        data = feedparser.parse(url)
        #print(data.entries)
        for x in range(len(data.entries)):
            dic.setdefault(x+1, []).append(data.entries[x].title)
            dic.setdefault(x+1, []).append(data.entries[x].summary)
            dic.setdefault(x+1, []).append(data.entries[x].link)
            dic.setdefault(x+1, []).append(data.entries[x].published)
        #return jsonify(data)
        return render_template('result.html',dic = dic)
    return render_template('error.html')

@app.route('/searchapi')
def searchapi():
    return render_template('welcome_api.html')

@app.route('/resultapi', methods=['POST', 'GET'])
def resultapi():
    if request.method =='POST':
        uri = request.form['url']
        #uri = "https://werindia.com/newsservice/education"
        try:
            uResponse = requests.get(uri)
        except requests.ConnectionError:
            return "Connection Error"
        Jresponse = uResponse.text
        dic = {}
        #print(Jresponse)
        data = json.loads(Jresponse)
        #print(data['category'][0]['news'][0]['title'])
        for x in range(len(data['category'][0]['news'])):
            dic.setdefault(x + 1, []).append(data['category'][0]['news'][x]['title'])
            dic.setdefault(x + 1, []).append(data['category'][0]['news'][x]['url'])
            dic.setdefault(x + 1, []).append(data['category'][0]['news'][x]['image_path'])
            dic.setdefault(x + 1, []).append(data['category'][0]['news'][x]['news_source'])
            dic.setdefault(x + 1, []).append(data['category'][0]['news'][x]['date'])
        #displayName = data['items'][0]['display_name']  # <-- The display name
        #reputation = data['items'][0]['reputation']  # <-- The reputation
        #return render_template('result.html',dic = dic)
        #return Jresponse

        return render_template('result_api.html',dic = dic)


if __name__ == '__main__':
    app.run()
