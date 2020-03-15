
from smartcard.System import readers

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
