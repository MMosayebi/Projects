🏠 House Price Prediction

A regression project focused on predicting house prices using Python and Machine Learning.

🎯 Project Overview

This project was developed as a Machine Learning practice project using a hypothetical house-price dataset obtained from an educational course.

The goal was to build a regression workflow that predicts house prices based on:

- 📐 Area
- 🛏️ Number of Rooms
- 🚗 Parking
- 📦 Warehouse
- 🛗 Elevator

Rather than focusing only on the final prediction, this project explores an end-to-end regression workflow, from data cleaning and exploratory analysis to model evaluation and prediction.

---

🔍 Project Workflow

Dataset
   ↓
Data Cleaning
   ↓
EDA
   ↓
Outlier Detection
   ↓
Feature Preparation & Scaling
   ↓
Modeling
   ↓
Evaluation
   ↓
Prediction

---

🧹 01 · Data Cleaning

The first stage of the project focuses on preparing the dataset for analysis and machine learning.

The data-cleaning workflow includes:

- Loading and inspecting the dataset
- Checking data types
- Identifying missing values
- Checking duplicated records
- Reviewing inconsistent data
- Preparing features for modeling
- Basic data validation

Notebook:

📓 Data Cleaning

"Data Cleaning.ipynb"

---

📊 02 · Exploratory Data Analysis

Exploratory Data Analysis was performed to better understand the dataset and the relationship between the available features and house prices.

The analysis includes:

- Distribution analysis
- Feature exploration
- Relationship between features and price
- Correlation analysis
- Data visualization
- Identifying potential anomalies and outliers

---

📈 03 · Outlier Detection

Outliers were investigated using the Interquartile Range (IQR) method.

The general approach was:

Q1 → First Quartile
Q3 → Third Quartile
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

This step was used to better understand the distribution of house prices and identify potentially unusual observations.

---

🤖 04 · Linear Regression

A manual Machine Learning workflow was implemented using Scikit-learn.

The workflow includes:

- Data preparation
- Feature selection
- Train/Test split
- Feature scaling
- Multiple Linear Regression
- Model training
- Model evaluation
- Prediction on unseen data

The Linear Regression model is used as a baseline model, providing a reference point for future model improvement.

Notebook:

📓 Linear Regression

"House Price Prediction (using linear regression).ipynb"

---

⚙️ 05 · PyCaret Regression

An automated Machine Learning workflow was also explored using PyCaret.

The PyCaret workflow was used to:

- Set up a regression environment
- Compare multiple regression models
- Evaluate model performance
- Identify promising models
- Explore automated Machine Learning capabilities

Notebook:

📓 PyCaret Regression

"House Price Predcition (using Pycaret).ipynb"

---

📊 Evaluation

The regression models are evaluated using several standard metrics:

Metric| Purpose
R²| Measures the proportion of variance explained by the model
MAE| Measures the average absolute prediction error
MSE| Penalizes larger prediction errors
RMSE| Measures prediction error in the same units as the target

Using multiple evaluation metrics provides a more complete view of model performance rather than relying on a single score.

---

📁 Project Structure

House Price Prediction/
│
├── data transform/
│   └── data.xlsx
│
├── dataset/
│   └── HousePrice.csv
│
├── Data Cleaning.ipynb
├── House Price Prediction (using linear regression).ipynb
├── House Price Predcition (using Pycaret).ipynb
│
└── requirements.txt

---

🛠️ Tech Stack

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 🤖 Scikit-learn
- ⚙️ PyCaret
- 📓 Jupyter Notebook
- 📗 Microsoft Excel

---

📓 Notebooks

🔹 Data Cleaning

Data inspection, cleaning, preprocessing, and preparation.

Notebook: "Data Cleaning.ipynb"

🔹 Linear Regression

Manual regression workflow using Scikit-learn, including preprocessing, scaling, model training, evaluation, and prediction.

Notebook: "House Price Prediction (using linear regression).ipynb"

🔹 PyCaret Regression

Automated regression workflow for comparing different Machine Learning models.

Notebook: "House Price Predcition (using Pycaret).ipynb"

---

🚀 Future Improvements

Several improvements can be explored in future versions of the project:

- Feature engineering
- Advanced regression models
- Cross-validation
- Hyperparameter tuning
- Improved outlier handling
- Model comparison
- Prediction intervals
- Improved preprocessing pipelines
- Feature importance analysis
- More robust model evaluation
- Deployment of the final model

---

💡 Key Takeaway

This project was created to practice and understand the end-to-end Machine Learning regression workflow.

The main focus was not only on obtaining a final prediction, but also on understanding how different stages of a Machine Learning project — including data cleaning, exploratory analysis, preprocessing, feature scaling, model selection, and evaluation — can affect model performance.

The project also provides a comparison between a manually implemented Scikit-learn workflow and an automated PyCaret workflow.

The dataset is hypothetical and was obtained from an educational course. It is intended for learning and practice purposes, while the data preparation, analysis, modeling, evaluation, and experimentation were performed as part of this project.

---

👨‍💻 Author

Mohammad Mosayebi

Sales & Marketing Data Analyst | Python | Excel | Power BI | SQL Server

GitHub: MMosayebi

---

⭐ If you find this project useful, feel free to star the repository.