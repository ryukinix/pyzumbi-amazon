import os
import urllib.request as urllib2

class Progress(object):
    def __init__(self):
        self._seen = 0.0

    def update(self, total, size, name):
        self._seen += size
        pct = (self._seen / total) * 100.0
        print ('%s progress: %.2f' % (name, pct))

class file_with_callback(file):
    def __init__(self, path, mode, callback, *args):
        file().__init__(self, path, mode)
        self.seek(0, os.SEEK_END)
        self._total = self.tell()
        self.seek(0)
        self._callback = callback
        self._args = args

    def __len__(self):
        return self._total

    def read(self, size):
        data = file.read(self, size)
        self._callback(self._total, len(data), *self._args)
        return data

path = 'large_file.txt'
progress = Progress()
stream = file_with_callback(path, 'rb', progress.update, path)
req = urllib2.Request(url, stream)
res = urllib2.urlopen(req)