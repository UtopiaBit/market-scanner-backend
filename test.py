# https://www.youtube.com/watch?v=t0JXiljpNRo&t=84s&ab_channel=CBTNuggets

import os
import requests
import asyncio

base_url = "http://httpbin.org/"


def make_request(sec):
    endpoint = base_url + "delay/" + str(sec)
    resp = requests.get(endpoint)
    data = resp.json()
    return data


# python is by default a BLOCKING language. By defualt the async call is awaited, even without the await keyword
# this is contrary to js, which is non-blocking and these calls are not awaited
def main_normal():
    print("Making the 1st request")
    data = make_request(4)
    print("The 1st request has returned. Here is the response")
    print("Making the 2nd request")
    data2 = make_request(2)
    print("The 2nd request has returned. Here is the response")
    # as you can see the problem here is that you could do the requests simultaneously

    # print(data)


# TO-DO
def main_async():
    print("Making the request. This will take a while")
    data = make_request(4)
    print("The request has returned. Here is the response")
    print(data)


main_normal()
