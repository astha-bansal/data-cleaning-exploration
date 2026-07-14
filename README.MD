# 🚢 Titanic Exploratory Data Analysis & Visualization

A complete **Exploratory Data Analysis (EDA)** and **Data Visualization** project on the famous Titanic dataset using **Python, Pandas, Matplotlib, and Seaborn**.

This project demonstrates the complete data analysis workflow—from loading and cleaning raw data to extracting insights through statistical analysis and professional visualizations.

---

## 📌 Project Overview

The Titanic dataset is one of the most popular beginner datasets in Data Science and Machine Learning.

The objective of this project is to:

- Load and inspect the dataset
- Clean missing and inconsistent data
- Perform exploratory data analysis (EDA)
- Create meaningful visualizations
- Generate a dashboard summarizing important insights

---

## 📂 Dataset

Dataset Source:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Dataset contains information such as:

- Passenger ID
- Passenger Class
- Name
- Sex
- Age
- Fare
- Embarked Port
- Number of Siblings/Spouses
- Number of Parents/Children
- Survival Status

---

# 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📋 Project Workflow

## 1️⃣ Data Loading

- Imported Titanic dataset using Pandas
- Inspected rows and columns
- Checked data types
- Generated descriptive statistics

---

## 2️⃣ Data Cleaning

Performed several preprocessing steps:

- Filled missing Age values using Median
- Filled missing Embarked values using Mode
- Removed Cabin column (too many missing values)
- Removed duplicate records

---

## 3️⃣ Feature Engineering

Created new useful features:

- **FamilySize**
- **IsAlone**
- **AgeGroup**

---

## 4️⃣ Exploratory Data Analysis

Performed statistical analysis including:

- Survival count
- Survival rate
- Average age by passenger class
- Survival rate by gender
- Correlation analysis
- GroupBy analysis

---

# 📊 Visualizations

The project contains multiple visualizations.

### 1. Survival Rate by Gender

- Bar Chart
- Female vs Male survival percentage

---

### 2. Age Distribution

- Histogram
- Comparison between survivors and non-survivors

---

### 3. Passenger Class Distribution

- Pie Chart
- Percentage of passengers in each class

---

### 4. Fare Distribution by Passenger Class

- Seaborn Boxplot
- Comparison based on survival

---

### 5. Correlation Heatmap

- Pearson Correlation Matrix
- Relationship between numerical features

---

### 6. Age vs Fare Scatter Plot

- Scatter Plot
- Colored by Survival
- Styled by Passenger Class

---

### 7. Dashboard

A professional dashboard containing:

- Survival Count
- Age Distribution
- Survival Rate by Class
- Survival Rate by Family Size

---

# 📈 Key Insights

Some interesting findings from the analysis:

- Female passengers had a significantly higher survival rate than male passengers.
- First-class passengers had better survival chances.
- Higher ticket fare generally correlated with higher survival probability.
- Passengers traveling with small families had better survival rates than those traveling alone or in very large groups.
- Most passengers belonged to the 3rd passenger class.
- Age alone was not a strong predictor of survival.

---
## 📁 Project Structure

```text
Titanic-EDA/
│
├── venv/                             # Virtual environment
├── Titanic_EDA.py                    # Main Python script
├── Titanic-Visualization.ipynb       # Jupyter Notebook
├── Titanic-Dataset.csv               # Original Titanic dataset
├── titanic_cleaned.csv               # Cleaned dataset after preprocessing
│
├── chart1_survival_by_gender.png     # Survival rate by gender
├── chart2_age_distribution.png       # Age distribution histogram
├── chart3_class_distribution.png     # Passenger class pie chart
├── chart4_fare_boxplot.png           # Fare distribution boxplot
├── chart5_correlation_heatmap.png    # Correlation heatmap
├── chart6_age_vs_fare_scatter.png    # Age vs Fare scatter plot
├── dashboard_titanic.png             # Combined dashboard
│
├── requirements.txt                  # Project dependencies
└── README.md                         # Project documentation
```
---

# ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/Titanic-EDA.git
```

### Navigate into the project

```bash
cd Titanic-EDA
```

### Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Run the notebook

```bash
jupyter notebook
```

Open:

```
Titanic_EDA.ipynb
```

Run all cells.

---

# 📦 Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Data Cleaning using Pandas
- Handling Missing Values
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Visualization
- Correlation Analysis
- Dashboard Creation
- Statistical Interpretation of Data

---

# 📸 Sample Output

The project generates:

- Cleaned Dataset
- Six Professional Charts
- Titanic Analysis Dashboard

---

# 👩‍💻 Author

**Astha Bansal**

B.Tech Computer Science Engineering

Data Science & Machine Learning Enthusiast

---

# ⭐ Acknowledgements

- Kaggle Titanic Dataset
- Data Science Dojo
- Pandas Documentation
- Matplotlib Documentation
- Seaborn Documentation