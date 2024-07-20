from flask import Flask, request
from flask_restful import Resource,Api, reqparse
import requests as rq
from dotenv import load_dotenv
import os 
# initializations
app = Flask(__name__)
api = Api(app)
load_dotenv()
apikey = os.getenv("APIKEY")
i = os.getenv("I")


# routes classes
class Landing(Resource):
	def get(self):
		

		return {"data":"landing"}


# top ten - return top ten moives

class Top_Ten(Resource):
	def get(self):
		return {"data":"top ten"}


# search [title director relase-year] - return search upon parameters
class Search(Resource):
	def get(self):
		return {"data":"search endpoint"}

	def post(self):
		global apikey
		global i
		print(apikey,i)
		data = request.json
		if len(data) < 2:
			return {"Error":"no enugh parameters"}
		title,ry,tp = "","",""
	
		if "type" not in data:
			data["type"] = ""

		if data["title"] != "":
			title = data["title"] 
		if data["ry"]:
			ry = data["ry"]
		if data["type"]:
			tp = data["type"]
		if data["title"] == "" and data["ry"] == "":
			return {"Error":"You have to insert title or relase data"}
		res = rq.get("http://www.omdbapi.com/?i={}&apikey={}&s={}&y={}".format(i,apikey,title,ry))
		res = res.json()

		if tp != "" and tp in ["movie","series"]:

			res = [x for x in res["Search"] if x["Type"] == tp]
		return {"data":res}

# get a movie details
class Search_details(Resource):
	global apikey
	global i
	def get(self):
		return {"data":"search details endpoint"}

	def post(self):
		data = request.json
		title = ""

		if data["title"]:
			title = data["title"] 
		if data["title"] == "":
			return {"Error":"You have to insert title"}
		res = rq.get("http://www.omdbapi.com/?i={}&apikey={}&t={}&plot=full".format(i,apikey,title))

		res = res.json()
		return {"data":res}

# adding routes to the api
api.add_resource(Landing,"/")
api.add_resource(Top_Ten,"/top_ten")
api.add_resource(Search,"/search")
api.add_resource(Search_details,"/search/details")


if __name__ == "__main__":
	app.run(debug=True)