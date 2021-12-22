import ccxt
import time

from models import OrderBook


# you will need to use the async version in the future
# import asyncio
# import ccxt.async_support as ccxt

# print(ccxt.exchanges)  # print a list of all available exchange classes

# returns a list of exchanges in json array format
def get_exchanges():
    return ccxt.exchanges


def get_recent_trades(symbol, exchange_):
    exchange = getattr(ccxt, exchange_)({"id": "exchange1"})
    limit = 20
    if exchange.has["fetchTrades"]:
        result = exchange.fetch_trades(symbol, limit=limit)
        return result

    else:
        return None


# https://docs.ccxt.com/en/latest/manual.html#order-book
# returns a list of exchanges in json array format
def get_order_book(symbol, exchange_):
    exchange = getattr(ccxt, exchange_)({"id": "exchange1"})
    # limit = 10  # limit doesn't work properly with every exchange so don't use it
    # we want the L2 level detail. we have a special decorated method for that (just ad l2 suffix)
    # response = exchange.fetch_l2_order_book(symbol)
    response = exchange.fetchOrderBook(symbol)
    # add exchange name
    response["exchange"] = exchange_
    # order_book = OrderBook(response, exchange_)
    return response


# returns the pairs that match the given exchange and quote(optional)
def get_pairs(exchange, quote=None):
    print("Fetching pairs from: " + exchange)
    # you need to use getattr to convert string to object attribute
    exchange = getattr(ccxt, exchange)({"id": "exchange1"})
    # you need to load the markets to make them available
    markets = exchange.load_markets()
    # now the markets are availabe inside the exchange variable
    symbols = exchange.symbols  # array of all symbols
    if quote != None:
        # filter by quote
        filtered = []
        for symbol in symbols:
            parsed = symbol.split("/")
            if parsed[1] == quote:
                # exact match
                filtered.append(symbol)
        symbols = filtered
    # print(symbols)
    return symbols


# takes a list and puts the highest volume pairs at the top
def order_pairs(list):
    return None


get_order_book("BTC/USDT", "btcturk")
# get_recent_trades("BTC/USDT", "btcturk")
