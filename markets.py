from flask import Blueprint, render_template, flash, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import ccxt_service as ccxt


# to see how you can use the "request" to extract data:
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request

# to fix the CORS policy problem simply add the @cross_origin() decorator
# https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0

# initialize a blueprint to define routes on
routes = Blueprint("views", __name__)


@routes.route("/", methods=["GET", "POST"])
@cross_origin()
def markets():
    # normally you should do something like send(response) but a regular return will do with flask
    return jsonify({"Hello there": "Backend is running!"})


@routes.route("/exchanges", methods=["GET", "POST"])
@cross_origin()
def exchanges():
    response = ccxt.get_exchanges()
    return jsonify(response)


@routes.route("/pairs", methods=["POST"])
@cross_origin()
def pairs():
    # in python, json is implicitly treated as a "dict"
    json = request.json
    exchange = json["exchange"]
    pairs = ccxt.get_pairs(exchange)
    response = {"pairs": pairs}
    return jsonify(response)


# returns the raw json response
@routes.route("/order-book", methods=["POST"])
@cross_origin()
def order_book():
    json = request.json
    exchange = json["exchange"]
    symbol = json["symbol"]
    order_book = ccxt.get_order_book(symbol, exchange)
    response = order_book
    return jsonify(response)


# returns the raw json response
@routes.route("/recent-trades", methods=["POST"])
@cross_origin()
def recent_trades():
    json = request.json
    exchange = json["exchange"]
    symbol = json["symbol"]
    recent_trades = ccxt.get_recent_trades(symbol, exchange)
    return jsonify(recent_trades)

