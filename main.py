import argparse

from datautils import DataUtils
from trainer import Trainer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", action="store")
    parser.add_argument("--u", action="store")
    args = parser.parse_args()
    model_num = int(args.m)
    dir = args.u

    instance = DataUtils(dir)

    train = instance.clean_df(instance.get_df(True))
    train_labels = instance.get_labels(True)

    test = instance.clean_df(instance.get_df(False))
    test_labels = instance.get_labels(False)

    trainer = Trainer(model_num)
    if (model_num >= 6):
        for idx in range(6):
            trainer.change_idx(idx)
            trainer.train(train, train_labels)
            trainer.result(test_labels, trainer.pred(test))

    trainer.train(train, train_labels)
    trainer.result(test_labels, trainer.pred(test))
