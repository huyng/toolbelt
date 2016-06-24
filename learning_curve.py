import pandas as pd
import pylab as P
import sys


def plot_training_curve(fpath):
    """
    plot loss and accuracy for trn and val

    fpath is a csv file with following header loss,val_loss,acc,val_acc
    """
    df = pd.read_csv(fpath, na_values="None")
    P.figure(figsize=(16, 6))
    P.subplot(121)
    df['loss'].plot(ax=P.gca(), marker="o", markeredgecolor=(0, 0, 1, 0), linestyle='', markerfacecolor=(.9, .9, .9, .1))
    pd.rolling_mean(df[['loss']], 100).plot(ax=P.gca(), c=(.5,0,1))
    df['val_loss'].plot(ax=P.gca(), marker="o", c=(0,1,0,.8), label="val_loss")\
                  .legend(loc="upper right")
    P.ylabel("loss")
    P.xlabel("iteration")
    P.title(fpath)
    P.subplot(122)
    df['acc'].plot(ax=P.gca(), marker="o", markeredgecolor=(0, 0, 1, 0), linestyle='', markerfacecolor=(.9, .9, .9, .1))
    pd.rolling_mean(df[['acc']], 100).plot(ax=P.gca(), c=(.5, 0, 1))
    df['val_acc'].plot(ax=P.gca(), marker="o", c=(0, 1, 0, .8), label="val_acc").legend(loc="lower right")
    P.ylabel("accuracy")
    P.xlabel("iteration")
    P.title(fpath)

if __name__ == '__main__':
    plot_training_curve(sys.argv[1])
