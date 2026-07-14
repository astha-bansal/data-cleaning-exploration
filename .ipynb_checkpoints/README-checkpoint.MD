# Data Cleaning & Exploratory Data Analysis (Titanic Dataset)

This mini-project focuses on the cleaning, transformation, and exploratory data analysis (EDA) of a Titanic passenger dataset. The script handles missing records, removes duplicate entries, engineers new features, and uncovers survival insights.

## Project Structure

```text
DATA CLEANING & EXPLORATION/
│
├── venv/                 # Python virtual environment
├── EDA.py                # Main script for data cleaning and exploration
├── requirements.txt      # Project dependencies (pandas, numpy)
├── tested.csv            # Raw input dataset
└── titanic_cleaned.csv   # Processed and cleaned output dataset
```

## Features & Implementation

### 1. Data Inspection & Cleaning
* **Missing Value Analysis:** Calculates absolute counts and percentages of missing data per column.
* **Imputation Strategy:** 
  * Replaces missing values in `Age` with the column median to limit outlier impact.
  * Replaces missing values in `Fare` with the most frequent value (mode).
  * Drops the `Cabin` column due to an excessive number of missing values.
* **Deduplication:** Identifies and drops duplicate rows to ensure data integrity.

### 2. Exploratory Data Analysis (EDA)
The script answers specific analytical questions using `pandas` aggregations:
* Absolute survival counts and total survival rate.
* Average age broken down by passenger class (`Pclass`).
* Survival rates compared across genders (`Sex`).
* Correlation matrix between `Fare`, `Age`, and `Survived`.

### 3. Feature Engineering
Three new computed columns are created to aid further analysis:
* `FamilySize`: Combined count of siblings/spouses (`SibSp`), parents/children (`Parch`), and the passenger themselves.
* `IsAlone`: A binary flag (1 if traveling alone, 0 otherwise).
* `AgeGroup`: Categorical binning of ages into `Child`, `Teen`, `Young Adult`, `Adult`, and `Senior`.

## Getting Started

### Prerequisites
Make sure you have Python installed. It is recommended to use the included virtual environment.

### Installation & Setup

1. **Activate the virtual environment:**
   * On Windows:
     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis:**
   ```bash
   python EDA.py
   ```

## Outputs
After running the script, the console will display the step-by-step processing logs and analytical summaries. A new file named `titanic_cleaned.csv` will be generated in the root directory containing the fully cleaned data and newly engineered features.
