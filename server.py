from flask import Flask, request, render_template
import feedparser
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
	if request.method =='POST':
		url = request.form['url']
		dic = {}
		url = url+'/feed'
		data = feedparser.parse(url)

		for x in range(len(data.entries)):		
			dic.setdefault(x+1, []).append(data.entries[x].title)
			dic.setdefault(x+1, []).append(data.entries[x].link)
			dic.setdefault(x+1, []).append(data.entries[x].published)
		return render_template('result.html',dic = dic)
	return render_template('error.html')
if __name__ == '__main__':
	app.run()