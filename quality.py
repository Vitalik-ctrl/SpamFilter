from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix


def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + 10 * fp + fn)

def compute_quality_for_corpus(corpus_dir):
    truth_dict = read_classification_from_file(corpus_dir + '/' + "!truth.txt")
    pred_dict = read_classification_from_file(corpus_dir + '/' + "!prediction.txt")
    
    confmat = BinaryConfusionMatrix("SPAM", "OK")
    confmat.compute_from_dicts(truth_dict, pred_dict)
    
    tp, tn, fp, fn = confmat.as_dict().values()
    
    return quality_score(tp, tn, fp, fn)
    