# Retail Buyer Segmentation

This project builds a full machine learning pipeline that segments retail customers into meaningful groups and predicts the segment of new customers using classification models. The goal is to help businesses understand their customer base, target marketing efforts, and personalize their strategies based on data-driven insights.

---

## 🚀 Project Overview

The project delivers three main components:

1. **Data Preparation & EDA**  
   Cleaning, transforming, exploring, and understanding the customer dataset.

2. **Unsupervised Segmentation (Clustering)**  
   Applying clustering techniques to uncover natural customer groups and documenting segment characteristics.

3. **Supervised Classification Models**  
   Training **five classification models** to predict a customer’s segment and comparing them using standardized evaluation metrics.

---

## 📂 Repository Structure


---

## 🧹 1. Data Preparation & EDA

Tasks performed:

- Missing-value imputation  
- Encoding categorical variables  
- Normalization & scaling  
- Outlier handling  
- Feature engineering  
- Visualization of distributions and trends  
- Initial business insights  

This stage outputs a clean and structured dataset ready for modeling.

---

## 🔍 2. Customer Segmentation (Clustering)

Clustering steps:

- Applying **K-Means** (primary model)  
- Optional: Hierarchical / GMM exploration  
- Silhouette Score evaluation  
- PCA/UMAP visualization of segments  
- Interpreting each segment’s demographics, behavior, and spending profile  

The result is a meaningful “cluster” label assigned to each customer.

---

## 🤖 3. Classification Models

Five supervised models are trained to predict cluster membership:

- Logistic Regression  
- Random Forest  
- XGBoost / LightGBM  
- KNN  
- Support Vector Machine (SVM)  

### Evaluation Metrics (per model)

- Accuracy  
- Precision (macro)  
- Recall (macro)  
- F1-score (macro)  
- Confusion Matrix  

A comparison table highlights the best-performing model.

---

## 📈 Goals of the Project

- Understand customer behavior patterns  
- Group customers into actionable segments  
- Build predictive tools for customer classification  
- Support targeted marketing and personalization  
- Deliver a reproducible, professional ML pipeline  

---

## 👥 Team Structure (4 Members)

- **Data Lead:** Cleaning, EDA, preprocessing  
- **Clustering Lead:** Models, silhouette, interpretation  
- **ML Lead:** Five classifiers + evaluation  
- **Documentation Lead:** Final report, repo organization, integration  

---

## 📊 Technologies Used

- Python  
- pandas / numpy  
- scikit-learn  
- XGBoost / LightGBM  
- matplotlib / seaborn  
- Jupyter Notebooks  

---

## 📝 Final Deliverables

- Fully cleaned and documented dataset  
- Clustering results with interpretation  
- Five classification models with evaluation  
- Final Report (PDF)  
- Reproducible code with organized notebooks  

---

## 📌 License

This project is for educational and research purposes.

---

## ⭐ Contributions

Feel free to fork, open issues, or submit pull requests.

