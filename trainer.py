import time
import pandas as pd

from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier



class Trainer():
    def __init__(self, idx):
        self.model_list = [DecisionTreeClassifier(), RandomForestClassifier(),
                            XGBClassifier(), LGBMClassifier(), SVC(), MultinomialNB()]
        
        self.idx = idx
    
    def change_idx(self, idx):
        self.idx = idx

    def train(self, x, y):
        self.clf = self.model_list[self.idx]
        start_time = time.time()
        self.clf.fit(x, y)
        end_time = time.time()
        print(f"\nTrained Model: {self.clf}")
        print(f"Training Time: {round(end_time - start_time, 2)} seconds")

    def pred(self, x_test):
        preds = self.clf.predict(x_test)
        return preds
    
    def result(self, y_true, preds, save = True):
        print('------------------------')
        print(classification_report(y_true, preds, digits = 4))
        print('------------------------')

        if (save):
            report = classification_report(y_true, preds, digits = 4, output_dict=True)
            df = pd.DataFrame(report).transpose()
            df.to_csv(f"{self.clf}.csv", index= True)


        
    





