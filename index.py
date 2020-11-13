from flask import Flask, jsonify
from flask_cors import CORS
from News import news

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(news)

@app.route("/")
def hello():
    return "this is my flask app"

if __name__ == "__main__":
    app.run()
    # app.run(debug=True, port=8080)
