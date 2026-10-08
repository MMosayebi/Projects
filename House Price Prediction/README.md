# 🏠 House Price Prediction

> A regression project focused on predicting house prices using Python and Machine Learning.

## 🎯 Project Overview

This project was developed as a **Machine Learning practice project** using a hypothetical house-price dataset obtained from an educational course.

The goal was to build a regression workflow that predicts house prices based on:

* 📐 Area
* 🛏️ Number of Rooms
* 🚗 Parking
* 📦 Warehouse
* 🛗 Elevator

Rather than focusing only on the final prediction, the project explores the complete workflow from data preparation to model evaluation.

---

## 🔍 Project Workflow

**Dataset → Data Preparation → EDA → Outlier Detection → Feature Scaling → Modeling → Evaluation → Prediction**

### 01 · Linear Regression

A manual Machine Learning workflow using **Scikit-learn**:

* Data exploration and preparation
* Outlier detection using IQR
* Feature selection
* Train/Test split
* Feature scaling
* Multiple Linear Regression
* Model evaluation
* Prediction on unseen data

### 02 · PyCaret Regression

An automated Machine Learning workflow using **PyCaret** to:

* Compare regression models
* Evaluate model performance
* Identify promising models
* Explore automated ML capabilities

---

## 📊 Evaluation

The models are evaluated using:

| Metric   | Purpose                                   |
| -------- | ----------------------------------------- |
| **R²**   | Measures explained variance               |
| **MAE**  | Average absolute prediction error         |
| **MSE**  | Penalizes larger errors                   |
| **RMSE** | Measures prediction error in target units |

The Linear Regression model is treated as a **baseline**, providing a reference point for future model improvement.

---

## 📁 Project Structure

```text
House Price Prediction/
│
├── data transform/
│   └── data.xlsx
│
├── dataset/
│   └── HousePrice.csv
│
├── House Price Predcition (using Pycaret).ipynb
├── House Price Prediction (using linear regression).ipynb
│
└── requirements.txt
```

---

## 🛠️ Tech Stack

**Python** · **Pandas** · **NumPy** · **Scikit-learn**
**Matplotlib** · **Seaborn** · **PyCaret** · **Jupyter Notebook** · **Excel**

---

## 📓 Notebooks

🔹 **Linear Regression**
[View Notebook](https://github.com/MMosayebi/Projects/blob/main/House%20Price%20Prediction/House%20Price%20Prediction%20%28using%20linear%20regression%29.ipynb)

🔹 **PyCaret Regression**
[View Notebook](https://github.com/MMosayebi/Projects/blob/main/House%20Price%20Prediction/House%20Price%20Predcition%20%28using%20Pycaret%29.ipynb)

🔹 **Requirements**
[View requirements.txt](https://github.com/MMosayebi/Projects/blob/main/House%20Price%20Prediction/requirements.txt)

---

## 🚀 Future Improvements

* Feature engineering
* Advanced regression models
* Cross-validation
* Hyperparameter tuning
* Better outlier handling
* Model comparison
* Prediction intervals
* Improved preprocessing pipeline

---

## 💡 Key Takeaway

This project was created to practice the **end-to-end regression workflow** and understand how different preprocessing and modeling decisions affect prediction performance.

The dataset is hypothetical and intended for educational purposes, while the analysis, modeling workflow, evaluation, and experimentation were performed as part of this project.

---

### 👤 Author

**Mohammad Mosayebi**
Data Analysis · Data Science · Machine Learning
