import scripts.textcleaning as TP
import pickle
import logging
import gensim
import praw
from praw.models import MoreComments

LOG = pickle.load(open('./Finalised_model/model_LOGREG.sav','rb'))
reddit = praw.Reddit(client_id = "F7Tj27YBPXb1Bw",client_secret = "d9HY3XFSHxOssTmZ1uZPfj6op1c",user_agent = "ashuv",username = "Ashuv12",password = "Priy@m@123")

def prediction(url):
	submission = reddit.submission(url = url)
	data = {}
	data["title"] = str(submission.title)
	data["url"] = str(submission.url)
	data["body"] = str(submission.selftext)

	submission.comments.replace_more(limit=None)
	comment = ''
	count = 0
	for top_level_comment in submission.comments:
		comment = comment + ' ' + top_level_comment.body
		count+=1
		if(count > 10):
		 	break
		
	data["comment"] = str(comment)

	data['title'] = TP.clean_text(str(data['title']))
	data['body'] = TP.clean_text(str(data['body']))
	data['comment'] = TP.clean_text(str(data['comment']))
    
	feature_combine = data["title"] + data["comment"] + data["body"] + data["url"]
	#print(feature_combine[:10]) 
	#print(feature_combine)
	return LOG.predict([feature_combine])

from flask import Flask
from flask import render_template
from flask import request
from flask import json
import requests
app = Flask(__name__)

@app.route("/")
def hello():
   	return render_template('post.html')

@app.route("/action_page",methods=['POST'])
def action(flair=None):
	text = request.form.get('Posturl',False)
	flair = str(prediction(text))
	return render_template('result.html',flair=str(flair))

@app.route("/automated_testing",methods=['POST'])
def endp(flair=None):
	files = {'upload_file': open('file.txt','rb')}
	url = request.form.get('Posturl',False)
	r = requests.post(url, files=files)
	data={}
	for req in r:
		flair = str(prediction(r))
		data[req]=flair
	json_data=json.dumps(data)
	return json_data 

@app.route("/stats")
def stats():
	return render_template('graph.html')

# run the application
if __name__ == "__main__":
    app.run()
