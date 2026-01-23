# Titanic Survival Prediction using Naive Bayes

This is a small, introductory project where I explore the **Naive Bayes** classification algorithm for the first time. The goal is to predict whether a passenger survived the Titanic disaster based on features like age, fare, and passenger class.

## 🚀 Project Overview
In this project, I implemented a `GaussianNB` model from Scikit-Learn. Since Naive Bayes assumes that features are independent, it serves as a great baseline model for binary classification tasks like this one.
## 📂 Folder Structure
- `Naive_bayes/`: Contains the core logic for the model.
  - `naive_bayes.ipynb`: The main script for data preprocessing and model training

## 🛠️ Key Features
- **Data Cleaning:** Handled missing values (imputation) for the 'Age' column.
- **Preprocessing:** handled the categorical encoding manually, for categorical features like 'Sex'.
- **Modeling:** Implemented `sklearn.naive_bayes.GaussianNB`.
- **Evaluation:** evaluated the model using metrics like score and predict_proba

## 📈 What I Learned
- How the "Naive" assumption of feature independence works.
- How to handle continuous data using the Gaussian (Normal) distribution.
- Chaining steps together in a clean workflow.
