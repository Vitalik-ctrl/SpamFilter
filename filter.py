from basefilter import BaseFilter
from filtercounter import RelativeCountFilter
from filterreceived import ReceivedFilter
from filterlength import LengthFilter


class MyFilter(BaseFilter):

    def __init__(self):
        super().__init__()
        self.filters = [RelativeCountFilter(), ReceivedFilter(), LengthFilter()]
        self.weights = [1, 1, 1]

    def train(self, train_corpus_dir):
        for f in self.filters:
            f.train(train_corpus_dir)

    def predict(self, email):
        prediction = 0
        for index, f in enumerate(self.filters):
            prediction += f.predict(email) * self.weights[index]
        prediction /= sum(self.weights)
        return prediction > 0.5
