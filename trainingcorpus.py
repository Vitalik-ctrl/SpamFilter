import os
from corpus import Corpus
from utils import read_classification_from_file


class TrainingCorpus(Corpus):
    def __init__(self, path):
        super().__init__(path)
        self.classifications = read_classification_from_file(os.path.join(self.path, '!truth.txt'))
        
    def spams(self):
        for email in self.emails():
            if self.classifications[email[0]] == 'SPAM':
                yield email
                
    def hams(self):
        for email in self.emails():
            if self.classifications[email[0]] == 'OK':
                yield email