from io import BufferedReader, FileIO
from pathlib import Path
import time

class Progress(BufferedReader):
    def __init__(self, filename, read_callback):
        f = open(filename, "rb")
        self.filename = Path(filename).name
        self.__read_callback = read_callback
        super().__init__(raw=f)
        self.start = time.time()
        self.length = Path(filename).stat().st_size

    def read(self, size=None):
        calc_sz = size
        if not calc_sz:
            calc_sz = self.length - self.tell()
        self.__read_callback(self.tell(), self.length,self.start,self.filename)
        return super(Progress, self).read(size)