# 🩺 Diabetes Prediction using SVM

This project predicts whether a person is diabetic using a machine learning model built with **Support Vector Classifier (SVC)**. It uses the Pima Indians Diabetes Dataset.

---

## 📂 Dataset

- **Source**: [Kaggle - Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Target**: `0` = Non-Diabetic, `1` = Diabetic
- **Features**:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age

---

## ⚙️ Technologies Used

- `Python`
- `NumPy`, `Pandas` for data processing
- `scikit-learn` for machine learning:
  - `SVC` (Support Vector Classifier)
  - `train_test_split`, `accuracy_score`
  - *(Optional)* `StandardScaler` for feature scaling

---

## 🧪 Model Flow

1. Load the dataset with pandas
2. Separate features and labels
3. *(Optional)* Apply StandardScaler to normalize features  
4. Split into training and testing sets
5. Train SVC with a linear kernel
6. Evaluate with accuracy and confusion matrix
7. Predict new inputs

---

## 📌 Note on Scaling

We tested the model **with and without** `StandardScaler`.  
💡 *Both versions showed nearly identical accuracy on this dataset.*  
Still, scaling is generally good practice with SVM for consistent performance across datasets.

---

## 🚀 Run It Locally

```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
python diabetes_prediction.py
