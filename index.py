from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from routes.News import news
from routes.GitHub import github
from routes.Bitcoin import bitcoin
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.register_blueprint(news)
app.register_blueprint(bitcoin)
app.register_blueprint(github)


@app.route("/")
def hello():
    return "this is my flask app"


if __name__ == "__main__":
    app.run()
    # app.run(debug=True, port=8080)
