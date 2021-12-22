import json
from types import SimpleNamespace

# You will need this class at some point


class OrderBook:
    def __init__(self, json_data, exchange):
        # first convert your dict to true string json (encode)
        json_str = json.dumps(json_data)
        # Parse JSON into an object with attributes corresponding to dict keys.
        self = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
        # TO DO: INSTEAD JUST CONVERT DICT TO OBJECT

    def myfunc(self):
        print("Hello my name is " + self.name)
