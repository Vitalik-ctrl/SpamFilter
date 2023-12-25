import os


class Corpus:
    def __init__(self, path):
        self.path = path

    def emails(self):
        for filename in os.listdir(self.path):
            if not filename.startswith('!'):
                with open(os.path.join(self.path, filename), 'r', encoding='utf-8') as f:
                    yield filename, f.read()
