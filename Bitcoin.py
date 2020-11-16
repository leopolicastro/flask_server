import requests
from flask import Blueprint

bitcoin = Blueprint("bitcoin", __name__)

BITCOIN_API_URL = "https://blockchain.info/ticker"


@bitcoin.route("/bitcoin")
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    # Convert the price to a floating point number
    return response_json["USD"]
