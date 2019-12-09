import plotserver as pls
import matplotlib.pyplot as plt
import numpy as np

def class_histogram(scores, labels, bins=40, minval=None, maxval=None):
    '''
    Plot a histogram of scores and their associated class
    '''

    plt.style.use('seaborn-deep')
    fig = plt.figure()
    classes = sorted(list(set(labels)))
    max_score = scores.max() if maxval is None else maxval
    min_score = scores.min() if minval is None else minval
    bins_arr = np.linspace(min_score, max_score, bins)
    for c in classes:
        class_scores = scores[labels == c]
        plt.hist(class_scores, bins_arr, alpha=0.5, label='%s' % c)
    plt.legend(loc='upper right')
    return fig


if __name__ == '__main__':
    pos_scores = np.random.normal(loc=.8, scale=.5, size=[200])
    neg_scores = np.random.normal(loc=.2, scale=.5, size=[200])
    pos_labels = np.ones(200)
    neg_labels = np.zeros(200)
    scores = np.concatenate([pos_scores, neg_scores])
    labels = np.concatenate([pos_labels, neg_labels])
    fig = class_histogram(scores, labels)
    pls.show(fig, host='0.0.0.0')
