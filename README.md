#  Mental Health Status Classification from Social Media Text

##  Team Members

- Abhi P Vijay
- Nakshathra V

---

# 🎓 Course Details
Predictive Analytics

---

# 📌 Project Overview

This project focuses on detecting and classifying mental health status from social media text using Natural Language Processing (NLP) and Machine Learning techniques.

The system analyzes textual data and predicts whether the mental health condition reflected in the text belongs to:

- Normal
- Depression

The project demonstrates the complete machine learning workflow including:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature extraction
- Model training
- Model evaluation
- Deployment preparation

---

# 🎯 Objectives

- To preprocess and clean textual social media data
- To perform exploratory data analysis on text data
- To extract meaningful numerical features using TF-IDF
- To train machine learning models for classification
- To compare model performance using evaluation metrics
- To prepare the project for deployment using Streamlit

---

# 💡 Problem Statement

Mental health issues are increasingly reflected in online social media conversations. Identifying depressive patterns manually from large amounts of text data is difficult and time-consuming.

This project aims to build an NLP-based machine learning system capable of automatically classifying mental health status from textual data.

---

# 📂 Dataset Description

## Dataset Used
- IMDB Dataset

## Dataset Features

| Feature | Description |
|---|---|
| review | User review text |
| sentiment | Positive / Negative sentiment |

## Data Processing

The original sentiment labels were converted into mental health categories:

| Original Label | Converted Label |
|---|---|
| positive | normal |
| negative | depression |

## Dataset Size

- Total records: 50,000
- Positive reviews: 25,000
- Negative reviews: 25,000

---

# 🔄 Project Methodology

## 1️⃣ Data Collection

- Imported IMDB Dataset
- Loaded data using Pandas

---

## 2️⃣ Data Preprocessing

The preprocessing stage included:
- Lowercasing
- Removal of URLs
- Tokenization
- Stopword removal
- Text cleaning

Libraries used:
- NLTK
- Regular Expressions (re)

---

## 3️⃣ Exploratory Data Analysis (EDA)

EDA techniques performed:
- Label distribution analysis
- Word frequency analysis
- Data balance visualization

Visualization libraries:
- Matplotlib
- Seaborn

---

## 4️⃣ Feature Extraction

Text data was converted into numerical vectors using:

### TF-IDF Vectorization

TF-IDF helps identify important words while reducing the impact of commonly occurring words.

---

## 5️⃣ Model Building

The following machine learning models were trained:

### ✅ Support Vector Machine (SVM)

### ✅ Logistic Regression

---

## 6️⃣ Model Evaluation

Evaluation metrics used:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📊 Results Summary

| Model | Accuracy |
|---|---|
| SVM | 88% |
| Logistic Regression | 89% |

## Best Performing Model

- Logistic Regression achieved the highest accuracy of **89%**.

---

# 🛠️ Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- GitHub

---

# 📁 Project Structure

```bash
Predictive_Project_2/
│
├── models/
│   ├── mental_health_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── results/
│   └── confusion_matrix.png
│
├── src/
│   ├── preprocessing_eda.ipynb
│   ├── model_training.ipynb
│   └── evaluation_deployment.ipynb
│
├── dataset/
│   └── IMDB Dataset.csv
│
├── Mental_Health_Classification.ipynb
├── requirements.txt
└── README.md
