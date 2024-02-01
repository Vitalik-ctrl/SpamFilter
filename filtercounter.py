from trainingcorpus import TrainingCorpus
from basefilter import BaseFilter


class RelativeCountFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.spam_words = {}
        self.spam_count = 0
        self.ham_count = 0
        self.ratio = 0

    def predict(self, email):
        words = email.split()
        for word in words:
            if self.spam_words.get(word, 0) > 37:
                return True
        return False

    def train(self, corpus_dir):
        corpus = TrainingCorpus(corpus_dir)
        self.spam_count = corpus.count_spam()
        self.ham_count = corpus.count_ham()
        self.ratio = self.spam_count / (self.spam_count + self.ham_count)

        for spam_content in corpus.spams():
            for word in spam_content.split():
                if word not in self.spam_words:
                    self.spam_words[word] = 0
                self.spam_words[word] += self.ratio

        for ham_content in corpus.hams():
            for word in ham_content.split():
                if word in self.spam_words:
                    self.spam_words[word] -= 1000 * self.ratio

    def test(self, corpus_test_dir):
        super().test(corpus_test_dir)
