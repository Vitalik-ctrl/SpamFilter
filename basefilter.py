import utils
from corpus import Corpus
import os


class BaseFilter:
    def __init__(self):
        self.corpus = None
        self.predictions = {}

    def create_dict(self):
        if self.corpus is None:
            raise ValueError("Corpus not set.")

        for filename, email in self.corpus.emails():
            self.predictions[filename] = 'SPAM' if self.predict(email) else 'OK'
        return self.predictions

    def predict(self, email):
        pass

    def train(self, corpus_dir):
        pass

    def test(self, corpus_test_dir):
        self.corpus = Corpus(corpus_test_dir)
        predictions_file = os.path.join(corpus_test_dir, "!prediction.txt")
        self.create_dict()
        utils.write_dict_to_file(predictions_file, self.predictions)
