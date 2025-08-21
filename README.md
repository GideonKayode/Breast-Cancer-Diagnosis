# Breast-Cancer-Diagnosis (Ongoing)
## Python-based project for exploring, analyzing, and classifying breast cancer datasets using machine learning models like Random Forest and SVC. Includes data preprocessing, model evaluation, feature importance analysis, and deployment-ready scripts

This project focuses on analyzing and classifying breast cancer data using machine learning techniques. The goal is to provide an end-to-end workflow for data preprocessing, model training, evaluation, and deployment-ready predictions.

---

## 🔍 Project Overview

Breast cancer is one of the most common cancers worldwide. Accurate classification of tumors as benign or malignant is crucial for early detection and treatment. This project leverages the well-known **Breast Cancer Wisconsin Dataset** to build predictive models using Python.

The project covers:

- Data exploration and preprocessing
- Feature selection and analysis
- Model training and evaluation
- Deployment-ready prediction pipeline

---

## 🛠️ Technologies & Libraries

- Python 3.x
- Pandas, NumPy
- Scikit-learn (Random Forest, SVC, etc.)
- Matplotlib & Seaborn (visualizations)
- Streamlit (for deployment)

---

## 📂 Project Structure

├── data/ │   └── breast_cancer_data.csv      # Original dataset ├── notebooks/ │   └── analysis.ipynb              # EDA & model experiments ├── src/ │   ├── preprocessing.py            # Data cleaning and encoding │   ├── train_model.py              # Model training scripts │   └── predict.py                  # Prediction pipeline ├── app.py                          # Streamlit deployment app ├── requirements.txt                # Python dependencies └── README.md

---

## ⚙️ Features

- **Data Cleaning & Preprocessing:** Handle missing values, Got rid of redundant features for selection, normalize features.
- **Exploratory Data Analysis (EDA):** Visualize distributions, correlations, and feature importance.
- **Machine Learning Models:** Train and evaluate Random Forest, Support Vector Classifier (SVC), and other models.
- **Model Evaluation:** Accuracy, precision, recall, F1-score, ROC-AUC.
- **Deployment:** Interactive Streamlit app for predicting tumor diagnosis from user input.

---

## 🧠 How to Use

1. Clone the repository:

```bash
git clone https://github.com/yourusername/breast-cancer-classification.git
cd breast-cancer-classification

2. Install dependencies:



pip install -r requirements.txt

3. Run the Streamlit app:



streamlit run app.py

4. Upload your dataset or enter features manually to get predictions.




---

📈 Model Insights

Random Forest: Robust and high accuracy for classification.

SVC: Effective for smaller datasets; handles non-linear boundaries.

Feature Importance: Identifies key features influencing predictions.



---

⚠️ Notes

Ensure numeric input is properly formatted; non-numeric input may cause errors.

The models were trained on the original dataset without heavy encoding for the target variable, as Random Forest and SVC handle categorical targets differently.



---

📫 Contact

For questions, improvements, or collaborations, reach out to:

Gideon Ayomide Kayode
Email: giddywrites@gmail.com
