# ECGHearbeat

[Dataset Download (104MB)](https://www.kaggle.com/datasets/shayanfazeli/heartbeat/download?datasetVersionNumber=1)

- There are total 5 classes
  - 0: **Normal**
  - 1: **Supraventricular**
  - 2: **Ventricular**
  - 3: **Fusion of ventricular and normal**
  - 4: **Unclassifiable**

![image](https://github.com/dchung1209/ECGHearbeat/assets/121478848/6f2c5bf4-a8f0-45ad-8159-d7e7d9cd50f8)


- There are 87554 instances for train dataset and 21892 instances for test dataset available
- The distribution of both datasets is highly *unbalanced* and *skewed*, yet share the same distribution

## How to use

| Number | 0             | 1             | 2       | 3    | 4    | 5           | 6>=     |
| ------ | ------------- | ------------- | ------- | ---- | ---- | ----------- | ------- |
| Model  | Decision Tree | Random Forest | XGBoost | LGBM | SVM  | Naive Bayes | Run All |

Run on the command `python main.py --m="model number here" --u="dataset directory here"`

## Results

### Macro Average

| Model | Precision | Recall | F1-Score |
| --------------- | --------- | ------ | -------- |
| Decision Tree   | 79.50%    | 80.25% | 79.87%   |
| Random Forest   | 95.02%    | 80.74% | 86.94%   |
| XGBoost         | 95.83%    | 86.10% | 90.33%   |
| LightGBM        | 93.23%    | 84.78% | 88.47%   |
| SVM             | 92.86%    | 76.36% | 82.89%   |
| Naive Bayes     | 52.35%    | 28.10% | 30.53%   |

| Model | Precision | Recall | F1-Score |
| --------------- | --------- | ------ | -------- |
| Bi-LSTM         | 94.02%    | 86.74% | 89.99%   |
| 1D CNN + LSTM   | 92.67%    | 90.37% | 91.40%   |




### Weighted Average

| Model | Precision | Recall | F1-Score |
| --------------- | --------- | ------ | -------- |
| Decision Tree   | 95.41%    | 95.38% | 95.39%   |
| Random Forest   | 97.39%    | 97.39% | 97.22%   |
| XGBoost         | 98.06%    | 98.09% | 97.99%   |
| LightGBM        | 97.75%    | 97.82% | 97.71%   |
| SVM             | 96.76%    | 96.80% | 96.57%   |
| Naive Bayes     | 79.10%    | 82.96% | 78.93%   |

| Model | Precision | Recall | F1-Score |
| ------------------ | --------- | ------ | -------- |
| Bi-LSTM            | 98.04%    | 98.09% | 98.01%   |
| 1D CNN + LSTM      | 98.49%    | 98.52% | 98.49%   |


- The dataset is highly unbalanced, so using the **macro average** would be more meaningful for observations

- **XGBoost** demonstrates the best performance, while **Naive Bayes** exhibits the worst performance among machine learning algorithms.
- Deep learning approaches also show decent performance but require way longer training times compared to traditional machine learning algorithms. (took <=10 mins with A100 GPU)
  - Bi-LSTM used two stacks of (bi-LSTM) with the size of 128 (hidden size)
  - 1D CNN + LSTM was inspired by [this model](https://ieeexplore.ieee.org/document/8978926)
  - Experiment done in [google colab](https://colab.research.google.com/drive/1OtWUMyA9tEvlKlgiwaE24HayKKdxzv0E?usp=sharing)

  
