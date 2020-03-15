#!/bin/env python3
import sys, requests
from smartcard.System import readers
from smartcard.Exceptions import NoCardException
from calypso import calypso
import viva

class Reader(object):
    def __init__(self):
        self.readers = readers()
        self.reader = self.get_reader()

    def get_reader(self):
        if not self.readers: 
            raise Exception("No reader detected.") 
        return self.readers[0] if (len(self.readers) == 1) else self.select_reader()

    def select_reader(self):
        for i, reader in enumerate(self.readers):
            print("[{}]: {}".format(i, reader))
        i = int(input("Select a reader: "))
        return self.readers[i]

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

    url = 'https://cloud-valid.appspot.com/viva/v1/card'
    response = requests.post(url, json = data)
    print(response.json())
  
if __name__ == '__main__':
    main()
