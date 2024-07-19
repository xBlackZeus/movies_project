from flask import Flask
from flask_restful import Resource,Api

# initializations
app = Flask(__name__)
api = Api(app)

# routes classes
class Landing(Resource):
	def get(self):
		return {"data":"landing"}




# adding routes to the api
api.add_resource(Landing,"/")


if __name__ == "__main__":
	app.run(debug=True)