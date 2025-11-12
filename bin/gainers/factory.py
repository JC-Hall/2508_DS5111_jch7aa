import bin.gainers.yahoo as yg
import bin.gainers.wsj as wg
import bin.gainers.cnbc as cg


class GainerFactory:
    def __init__(self):
        pass

    def get_handler(self, fname):
        if fname.startswith('ygainer'):
            return yg.GainerYahoo()
        elif fname.startswith('wsjgainer'):
            return wg.GainerWSJ()
        elif fname.startswith('cnbcgainer'):
            return cg.GainerCNBC()
        else:
            raise Exception(f"Unrecognized file type {fname}")
