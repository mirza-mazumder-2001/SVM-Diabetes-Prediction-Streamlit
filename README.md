# 🩺 Diabetes Prediction using SVM  
A machine learning web application built using a **Support Vector Machine (SVM)** classifier to predict whether a person is diabetic based on medical features.  
The app is deployed through **Streamlit** and uses the **PIMA Indians Diabetes Dataset**.

---
## 🎯 Objective

To develop a simple yet effective ML-based web application that predicts diabetes risk using SVM and Streamlit.

---

## 🚀 Live Demo
`🔗 https://svm-diabetes-prediction-app-cav3dzf7stca9pqkzhyqxb.streamlit.app/`

---

## 📌 Features
- Machine Learning model using **SVM (Linear Kernel)**
- Interactive and user-friendly **Streamlit web interface**
- Takes 8 medical input parameters
- Predicts:
  - **1 → Diabetic**
  - **0 → Not Diabetic**
- Model saved as `svm.sav` using pickle

---

## 📁 Project Structure
│── app.py
│── svm.sav
│── diabetes.csv
│── README.md
│── requirements.txt

## 📊 Dataset Information  

This project uses the **PIMA Indians Diabetes Dataset**, a widely used dataset for diabetes prediction in machine learning.

### **Features included in the dataset:**

| Feature | Description |
|--------|-------------|
| **Pregnancies** | Number of pregnancies |
| **Glucose** | Plasma glucose concentration |
| **BloodPressure** | Diastolic blood pressure |
| **SkinThickness** | Triceps skinfold thickness |
| **Insulin** | 2-hour serum insulin |
| **BMI** | Body Mass Index |
| **DiabetesPedigreeFunction** | Likelihood of diabetes based on family history |
| **Age** | Age in years |
| **Outcome** | Target variable (1 = Diabetic, 0 = Not Diabetic) |


---

## 🔧 Installation & Setup

### 1️⃣ Install requirements
```bash
pip install streamlit pandas numpy scikit-learn

