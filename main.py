#!/bin/env python3
import requests, json
from calypso import calypso
from reader import Reader

def main():
    reader = Reader()
    card = calypso.Calypso(reader.reader)

    data = {}
    data["atr"] = card.get_atr() # contactless does not provide atr data (only chip read)
    data["icc"] = card.get_id() # sometimes is null TODO
    data["environment"] = card.get_environment()
    data["contracts"] = card.get_contracts()
    data["history"] = card.get_history()
    data["counters"] = card.get_counters()

    print("Request:")
    print(json.dumps(data, indent=4))

    url = 'https://navegante.rijo.io/v1/card'
    response = requests.post(url, json = data)

    print("\nResponse:")
    print(json.dumps(response.json(), indent=4))
  
if __name__ == '__main__':
    main()
