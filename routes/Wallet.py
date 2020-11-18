from flask import Blueprint
from pywallet import wallet

wallet = Blueprint("wallet", __name__)


@wallet.route("/wallet/", methods=["POST"])
def create_hd_wallet():
    seed = wallet.generate_mnemonic()
    bitcoin_hd_wallet = wallet.create_wallet(network="BTC", seed=seed, children=1)
    return bitcoin_hd_wallet


@wallet.route("/wallet/<xpub>/", methods=["POST"])
def create_child_wallet(xpub):
    child_wallet = wallet.create_address(network="BTC", xpub=xpub)
    return child_wallet
