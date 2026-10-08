🏠 House Price Prediction

A regression project focused on predicting house prices using Python and Machine Learning.

🎯 Project Overview

This project was developed as a Machine Learning practice project using a hypothetical house-price dataset obtained from an educational course.

The goal was to build a regression workflow that predicts house prices based on:

📐 Area
🛏️ Number of Rooms
🚗 Parking
📦 Warehouse
🛗 Elevator

Rather than focusing only on the final prediction, the project explores the complete workflow from data preparation to model evaluation.

🔍 Project Workflow

Dataset → Data Cleaning → Data Preparation → EDA → Outlier Detection → Feature Scaling → Modeling → Evaluation → Prediction

01 · Data Cleaning

A data cleaning workflow using Python and Pandas:

- Data inspection
- Data type checking
- Missing value checking
- Duplicate checking
- Data preparation
- Preparing the dataset for further analysis

02 · Linear Regression

A manual Machine Learning workflow using Scikit-learn:

- Data exploration and preparation
- Outlier detection using IQR
- Feature selection
- Train/Test split
- Feature scaling
- Multiple Linear Regression
- Model evaluation
- Prediction on unseen data

03 · PyCaret Regression

An automated Machine Learning workflow using PyCaret to:

- Compare regression models
- Evaluate model performance
- Identify promising models
- Explore automated ML capabilities

📊 Evaluation

The models are evaluated using:

Metric| Purpose
R²| Measures explained variance
MAE| Average absolute prediction error
MSE| Penalizes larger errors
RMSE| Measures prediction error in target units

The Linear Regression model is treated as a baseline, providing a reference point for future model improvement.

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
├── House Price Predcition (using Pycaret).ipynb
├── House Price Prediction (using linear regression).ipynb
│
└── requirements.txt

🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · PyCaret · Jupyter Notebook · Excel

📓 Notebooks

🔹 Data Cleaning — View Notebook

🔹 Linear Regression — View Notebook

🔹 PyCaret Regression — View Notebook

🔹 Requirements — View requirements.txt

🚀 Future Improvements

- Feature engineering
- Advanced regression models
- Cross-validation
- Hyperparameter tuning
- Better outlier handling
- Model comparison
- Prediction intervals
- Improved preprocessing pipeline

💡 Key Takeaway

This project was created to practice the end-to-end regression workflow and understand how different preprocessing and modeling decisions affect prediction performance.

The dataset is hypothetical and intended for educational purposes, while the analysis, modeling workflow, evaluation, and experimentation were performed as part of this project.

👨‍💻 Author

Mohammad Mosayebi

Sales & Marketing Data Analyst | Python | Excel | Power BI | SQL Server

GitHub: MMosayebi

⭐ If you find this project useful, feel free to star the repository.