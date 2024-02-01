import os
from corpus import Corpus
from utils import read_classification_from_file


class TrainingCorpus(Corpus):
    def __init__(self, path):
        super().__init__(path)
        self.classifications = read_classification_from_file(os.path.join(self.path, '!truth.txt'))
        self.spam_count = 0
        self.ham_count = 0

    def count_spam(self):
        self.spam_count = len(list(filter(lambda x: x == 'SPAM', self.classifications.values())))
        return self.spam_count

    def count_ham(self):
        self.ham_count = len(list(filter(lambda x: x == 'OK', self.classifications.values())))
        return self.ham_count

    def spams(self):
        for email in self.emails():
            if self.classifications[email[0]] == 'SPAM':
                yield email[1]

    def hams(self):
        for email in self.emails():
            if self.classifications[email[0]] == 'OK':
                yield email[1]
