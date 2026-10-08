# 🏠 House Price Prediction

A Machine Learning regression project for predicting house prices based on property features.

### 🎯 Goal

Build a regression model that predicts house prices using:

* 📐 Area
* 🛏️ Number of Rooms
* 🚗 Parking
* 📦 Warehouse
* 🛗 Elevator

---

### 🔄 Workflow

```text
Data → EDA → Preprocessing → Outlier Detection
     → Train/Test Split → Scaling
     → Regression → Evaluation → Prediction
```

### 🤖 Model

**Multiple Linear Regression** is used as the baseline model.

The project also explores **PyCaret** for automated regression model comparison and future model improvement.

### 📊 Evaluation

The model is evaluated using:

* **R² Score**
* **MAE**
* **MSE**
* **RMSE**

A prediction workflow for **unseen house data** is also included.

---

### 🧹 Data Preparation

* Exploratory Data Analysis
* Outlier detection using **IQR**
* Feature scaling with **StandardScaler**
* Train/Test split
* Data leakage prevention

---

### 🛠️ Tech Stack

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `PyCaret` · `Jupyter`

---

### 🚀 Future Improvements

* Feature Engineering
* Advanced Regression Models
* Hyperparameter Tuning
* Cross-Validation
* Better Outlier Handling
* Prediction Intervals
* Model Comparison

---

### 📁 Project Structure

```text
House Price Prediction/
├── dataset/
├── modules/
├── notebooks/
├── README.md
└── requirements.txt
```

---

### 👨‍💻 Author

**Mohammad Mosayebi**

Data Analysis · Data Science · Machine Learning

[GitHub](https://github.com/MMosayebi)
