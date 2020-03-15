from . import constants
from smartcard.Exceptions import NoCardException

def bytearray_to_hex(b_array):
    return ''.join('{:02x}'.format(x) for x in b_array) if sum(b_array) > 0 else None

class Calypso(object):
    def __init__(self, reader):
        self.reader = reader
        self.calypso = self.__get_card__()

    def __get_card__(self):
        try:
            calypso = self.reader.createConnection()
            calypso.connect()
            return calypso           
        except NoCardException:
            raise Exception("No card detected.") 

    def __extra__(self, data, sw1, sw2):
        if sw1 != 0x61: return data, sw1, sw2
        get_response_apdu = [0x00] + constants.GET_RESPONSE_INS + [0x00, 0x00, sw2]
        extra, sw1, sw2 = self.calypso.transmit(get_response_apdu)
        return self.__extra__(data + extra, sw1, sw2)

    def __read__(self, record):
        read_record_apdu = constants.CALYPSO_CLA + constants.READ_RECORD_INS + [record + 1, 0x04, 0x1D]
        data, sw1, sw2 = self.calypso.transmit(read_record_apdu)

        #print(read_record_apdu, sw1, data)

        if sw1 != constants.OK:
            raise Exception("Error reading card data.")

        return {'data' : data, 'sw1' : sw1, 'sw2' : sw2 }

    def __select__(self, cmd, records = [0]): # records [1, 2, 3, 4]
        
        select_apdu = constants.CALYPSO_CLA + constants.SELECT_INS + [0x00, 0x00, 0x02] + cmd + [0x00]

        data, sw1, sw2 = self.calypso.transmit(select_apdu)

        #print(select_apdu, sw1, data)

        data, sw1, sw2 = self.__extra__(data, sw1, sw2)

        records = [r for r in records]
        result = { r : bytearray_to_hex(self.__read__(r).get('data')) for r in records }
        return result
    
    def get_atr(self):
        return bytearray_to_hex(self.calypso.getATR())

    def get_id(self):
        data = self.__select__(constants.ICC_FID)
        return data.get(0)

    def get_environment(self):
        data = self.__select__(constants.TICKETING_ENVIRONMENT_FID)
        return data.get(0)

    def get_history(self, event = None):
        records = [event] if event else range(3) # max 3 event records
        data = self.__select__(constants.TICKETING_EVENTS_FID, records = records)
        return data

    def get_contracts(self, contract = None):
        records = [contract] if contract is not None else range(4) # max 4 contract records
        data = self.__select__(constants.TICKETING_CONTRACTS_FID, records = records)
        return data

    def get_counters(self, index = None):
        counters = [ constants.COUNTERS_FIDS[c] for c in range(len(constants.COUNTERS_FIDS)) if index is None or c == index]
        data = {c : self.__select__(constants.TICKETING_COUNTERS_FID + [counters[c],]).get(0)  for c in range(len(counters))}
        return data