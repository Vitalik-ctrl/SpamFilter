class BinaryConfusionMatrix:
    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.tp, self.tn = 0, 0
        self.fp, self.fn = 0, 0

    def as_dict(self):
        return {
            'tp': self.tp,
            'tn': self.tn,
            'fp': self.fp,
            'fn': self.fn
        }

    def update(self, truth, prediction):
        if (truth != self.pos_tag and truth != self.neg_tag) or \
                (prediction != self.pos_tag and prediction != self.neg_tag):
            raise ValueError("One of the arguments didn't match with class configuration\n")

        if truth == prediction and prediction == self.pos_tag:
            self.tp += 1
        elif truth == prediction and prediction == self.neg_tag:
            self.tn += 1
        elif not (truth == prediction) and prediction == self.pos_tag:
            self.fp += 1
        elif not (truth == prediction) and prediction == self.neg_tag:
            self.fn += 1

    def compute_from_dicts(self, truth_dict, pred_dict):
        for key in pred_dict:
            self.update(truth_dict[key], pred_dict[key])
