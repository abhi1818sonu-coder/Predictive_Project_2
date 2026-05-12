# Mental Health Status Classification from Social Media Text

## Team Members

- Abhi P Vijay(253226)
- Nakshathra V(253207)

---

# Course Details

- Course: Predictive Analytics


---

# Project Overview

This project focuses on detecting and classifying mental health status from textual social media/movie review data using Natural Language Processing (NLP) and Machine Learning techniques.

The system analyzes textual input and predicts whether the mental health condition reflected in the text belongs to:

- Normal
- Depression

The project demonstrates the complete machine learning pipeline including:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature extraction using TF-IDF
- Machine learning model training
- Model evaluation
- Model saving and deployment preparation

---

#  Objectives

- To preprocess and clean textual data
- To perform exploratory data analysis on text data
- To extract meaningful numerical features using TF-IDF
- To train machine learning classification models
- To compare model performance using evaluation metrics
- To save trained models for deployment

---

#  Problem Statement

Mental health-related emotions and sentiments are increasingly reflected in online text data. Manual analysis of such large-scale textual content is difficult and time-consuming.

This project aims to develop an NLP-based machine learning system capable of automatically classifying mental health-related sentiment from text.

---

#  Dataset Description

## Dataset Used

- IMDB Movie Review Dataset

## Dataset Features

| Feature | Description |
|---|---|
| review | User review text |
| sentiment | Positive / Negative sentiment |

---

## Dataset Size

| Category | Count |
|---|---|
| Positive Reviews | 25,000 |
| Negative Reviews | 25,000 |
| Total Records | 50,000 |

---

## Data Processing

The original sentiment labels were mapped into mental health categories:

| Original Label | Converted Label |
|---|---|
| positive | normal |
| negative | depression |

---

#  Project Workflow

##  Data Collection

- Imported IMDB dataset
- Loaded data using Pandas

---

##  Data Preprocessing

The preprocessing stage included:
- Lowercasing
- URL removal
- Tokenization
- Stopword removal
- Text cleaning

Libraries used:
- NLTK
- Regular Expressions (`re`)

---

##  Exploratory Data Analysis (EDA)

EDA techniques performed:
- Label distribution analysis
- Dataset balance checking
- Visualization of class distribution

Visualization libraries:
- Matplotlib
- Seaborn

---

##  Feature Extraction

Text data was converted into numerical vectors using:

## TF-IDF Vectorization

TF-IDF helps identify important words while reducing the impact of frequently occurring words.

```python id="yoqmqv"
TfidfVectorizer(max_features=5000)
```

---

#  Machine Learning Models

The following machine learning models were trained and evaluated:

##  Support Vector Machine (SVM)

```python id="6n4siy"
LinearSVC()
```

### Accuracy Achieved
- 88%

---

##  Logistic Regression

```python id="mnkq2q"
LogisticRegression()
```

### Accuracy Achieved
- 89%

---

#  Model Evaluation

Evaluation metrics used:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

#  Results Summary

| Model | Accuracy |
|---|---|
| SVM | 88% |
| Logistic Regression | 89% |

## 🏆 Best Performing Model

- Logistic Regression achieved the best performance with **89% accuracy**.

---

#  Confusion Matrix Interpretation

The confusion matrix shows that the majority of predictions were classified correctly with relatively few misclassifications.

The model demonstrated:
- Balanced precision and recall
- Good classification capability
- Reliable performance on unseen test data

---
## Deployment
## Live Demo

Streamlit App:
https://mental-health-predictor-predictive-project-2.streamlit.app/


#  Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle
- GitHub

---


#  Conclusion

This project successfully demonstrates the use of NLP and machine learning techniques for mental health-related text classification.

The system preprocesses textual data, extracts meaningful features using TF-IDF, trains machine learning models, evaluates performance, and saves trained models for future deployment.

The project highlights the practical application of artificial intelligence in text analytics and sentiment-based mental health analysis.

---

 

---
