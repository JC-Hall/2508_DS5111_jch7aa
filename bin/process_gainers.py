"""
Process gainers using two design patterns for a demo.

We'll use the Template pattern to ways processes.

We'll then use a factory method so we don't have to worry about the instantiating the right class to handle the files..
"""

from abc import ABCMeta, abstractmethod
import sys
sys.path.append('.')
import bin.gainers.factory as gf

class TemplateClass(metaclass=ABCMeta):
    def __init__(self, fname):
        pass

    @abstractmethod
    def create_csv(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    def template_method(self):
        print("Two step Algorithm. Extract csv, normalize")
        self.create_csv()
        self.normalize()


class TwoStepClass(TemplateClass):
    def __init__(self, fname):
        self.fname = fname
        self.handler = gf.GainerFactory().get_handler(fname)

    def create_csv(self):
        self.handler.extract_csv()

    def normalize(self):
        self.handler.normalize_data()


class ThreeStepClass(TemplateClass):
    def __init__(self, fname):
        self.fname = fname
        self.handler = gf.GainerFactory().get_handler(fname)

    def download_html(self):
        self.handler.download_html()

    def create_csv(self):
        self.handler.extract_csv()

    def normalize(self):
        self.handler.normalize_data()
    
    def template_method(self):
        print("Three step Algorithm. Download, extract csv, normalize")
        self.download_html()
        self.create_csv()
        self.normalize()

class Client:
    def main(self, process, fname):
        if process == 'two':
            self.concreate = TwoStepClass(fname)
        elif process == 'three':
            self.concreate = ThreeStepClass(fname)
        self.concreate.template_method()

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 3, "Example Usage:  python process_gainers.py two ygainers.html"
    process = sys.argv[1]
    fname = sys.argv[2]

    client = Client()
    client.main(process, fname)
