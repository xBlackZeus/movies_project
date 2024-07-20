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
		data = request.json
		title,ry,tp = "","",""
		if data["title"]:
			title = data["title"] 
		if data["ry"]:
			ry = data["ry"]
		if data["type"]:
			tp = data["type"]
		if data["title"] == "" and data["ry"] == "":
			return {"Error":"You have to insert title or relase data"}
		res = rq.get("http://www.omdbapi.com/?i={3}&apikey={4}&s={0}&y={1}&plot=full".format(title,ry,apikey,i),proxies={"http":"127.0.0.1:8080"})
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
		res = rq.get("http://www.omdbapi.com/?i={2}&apikey={1}&t={0}&plot=full".format(title,apikey,i))

		res = res.json()
		return {"data":res}

# adding routes to the api
api.add_resource(Landing,"/")
api.add_resource(Top_Ten,"/top_ten")
api.add_resource(Search,"/search")
api.add_resource(Search_details,"/search/details")


if __name__ == "__main__":
	app.run(debug=True)