import re
from basefilter import BaseFilter
from trainingcorpus import TrainingCorpus 


class ReceivedFilter(BaseFilter):
    def train(self, corpus_dir):
        corpus = TrainingCorpus(corpus_dir)
        self.received_spam = {}
        self.received_ham = {}
        
        for email in corpus.hams():
            lines = email.split('\n')
            for line in lines:
                if not (re.search("Received:", line) is None):
                    if self.received_ham.get(line) is None:
                        self.received_ham[line] = 1
                    else:
                        self.received_ham[line] += 1
                        
        for email in corpus.spams():
            lines = email.split('\n')
            for line in lines:
                if not (re.search("Received:", line) is None):
                    if self.received_spam.get(line) is None:
                        self.received_spam[line] = 1
                    else:
                        self.received_spam[line] += 1
    
    def predict(self, email):
        received = [line for line in email.split('\n') if re.search("Received:", line) is not None]
        for rc in received:
            if self.received_ham.get(rc) is None and self.received_spam.get(rc, 0):
                return True
        return False