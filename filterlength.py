from basefilter import BaseFilter


class LengthFilter(BaseFilter):
    def predict(self, email):
        words = email.split()
        for word in words:
            if len(word) > 40:
                return True
        return False