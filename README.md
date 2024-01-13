# ECGHearbeat

[Dataset Download (104MB)](https://www.kaggle.com/datasets/shayanfazeli/heartbeat/download?datasetVersionNumber=1)

- There are 5 classes 0: Normal, 1: Supraventricular, 2: Ventricular, 3: Fusion of ventricular and normal, 4: Unclassifiable availalbe in the dataset

![image](https://github.com/dchung1209/ECGHearbeat/assets/121478848/16040140-77ff-466f-bd5a-e046a035f48e)

- Total 87554 instances for train dataset and 21892 instances for test dataset

## How to use

| Number | 0             | 1             | 2       | 3    | 4    | 5           | 6>=     |
| ------ | ------------- | ------------- | ------- | ---- | ---- | ----------- | ------- |
| Model  | Decision Tree | Random Forest | XGBoost | LGBM | SVM  | Naive Bayes | Run All |

Run on the command `python main.py --m="model number here" --u="dataset directory here"`

## Results

| Model/Macro Avg | Precision | Recall | F1-Score |
| --------------- | --------- | ------ | -------- |
| Decision Tree   | 79.50%    | 80.25% | 79.87%   |
| Random Forest   | 96.02%    | 80.74% | 86.94%   |
| XGBoost         | 95.83%    | 86.10% | 90.33%   |
| LightGBM        | 93.23%    | 84.78% | 88.47%   |
| SVM             | 92.86%    | 76.36% | 82.89%   |
| Naive Bayes     | 52.35%    | 28.10% | 30.53%   |

| Model/Micro Avg | Precision | Recall | F1-Score |
| --------------- | --------- | ------ | -------- |
| Decision Tree   | 95.41%    | 95.38% | 95.39%   |
| Random Forest   | 97.39%    | 97.39% | 97.22%   |
| XGBoost         | 98.06%    | 98.09% | 97.99%   |
| LightGBM        | 97.75%    | 97.82% | 97.71%   |
| SVM             | 96.76%    | 96.80% | 96.57%   |
| Naive Bayes     | 79.10%    | 82.96% | 78.93%   |

The dataset is highly unbalanced, so using the macro average would be more meaningful for observations

## Conclusion

**XGBoost** demonstrates the best performance, while **Naive Bayes** exhibits the worst performance among machine learning algorithms. Deep learning approaches also show decent performance but require relatively longer training times compared to traditional machine learning algorithms.
