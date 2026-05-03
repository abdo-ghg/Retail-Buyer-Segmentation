# 🛍️ Retail Buyer Segmentation

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)]()

---

## 📋 About the Project

**Retail Buyer Segmentation** is a comprehensive machine learning pipeline designed to help businesses understand their customer base through intelligent data-driven segmentation. The project combines unsupervised learning (K-Means clustering) with five supervised classification models to segment customers into meaningful groups and predict the segment of new customers. 

This end-to-end solution includes an interactive Flask web application featuring a sleek red-and-black theme, enabling both single-customer predictions and batch analytics through an intuitive dashboard.

---

## ✨ Key Features

- 🎯 **Customer Segmentation** – K-Means clustering to uncover natural customer groups with distinct behavioral patterns
- 📊 **Dual Input Methods** – Manual data entry form or bulk CSV upload for flexibility
- 🤖 **5 Classification Models** – Logistic Regression, Random Forest, XGBoost, KNN, and SVM with comprehensive evaluation metrics
- 📈 **Interactive Analytics Dashboard** – Real-time visualizations including age distribution, income vs. spending, and category breakdown
- 🎨 **Modern UI/UX** – Professional red-and-black theme with Bootstrap 5, responsive design, and smooth animations
- 🔍 **Comprehensive Data Pipeline** – Automated preprocessing, feature engineering, missing value handling, and normalization
- 📱 **Mobile-Friendly** – Fully responsive interface optimized for all devices
- ⚡ **Production-Ready** – Error handling, data validation, and secure file management

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | Python 3.8+, Flask 3.0 |
| **Machine Learning** | scikit-learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Styling** | Font Awesome, Custom CSS Animations |

---

## 📊 Dataset & Methodology

### Data Features
The project utilizes customer behavioral data including:
- **Demographics**: Annual Income, Age
- **Spending Behavior**: Wine, Fruits, Meat, Fish, Sweets, Gold (6 categories)
- **Purchase Channels**: Web, Catalog, Store, Discount (4 channels)

### ML Methodology
1. **Data Preparation & EDA**: Cleaning, encoding, normalization, outlier handling, and feature engineering
2. **Unsupervised Segmentation**: K-Means clustering with silhouette score evaluation and PCA/UMAP visualization
3. **Supervised Classification**: Training 5 models with evaluation metrics (Accuracy, Precision, Recall, F1-Score)
4. **Model Comparison**: Standardized performance comparison to identify the best-performing classifier

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/abdo-ghg/Retail-Buyer-Segmentation.git
cd Retail-Buyer-Segmentation
```

#### 2. Set Up Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Flask Application

Navigate to the Flask app directory:
```bash
cd flask_app
```

**Development Mode:**
```bash
python app.py
```

**Or use the startup script:**

Windows:
```bash
run.bat
```

macOS/Linux:
```bash
chmod +x run.sh
./run.sh
```

#### 5. Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

---

## 🚀 Usage Guide

### Manual Customer Prediction

1. Go to **Home** page
2. Click **"Start Manual Input"**
3. Fill in customer details:
   - Annual Income
   - Age
   - Spending amounts across 6 categories
   - Purchase channel counts
4. Click **"Predict Segment"**
5. View results including:
   - Customer segment classification (Premium/Regular/Budget)
   - Total spending and purchase metrics
   - Personalized recommendations

**Example:**
```
Annual Income: $50,000
Age: 35
Wine Spending: $200
Meat Spending: $300
Web Purchases: 5
→ Predicted Segment: Regular
```

### Batch Analytics (CSV Upload)

1. Go to **Home** page
2. Click **"Upload CSV File"**
3. Select a CSV file with the following required columns:
   - `annual_income`
   - `age`
   - `spend_wine`, `spend_fruits`, `spend_meat`, `spend_fish`, `spend_sweets`, `spend_gold`
   - `num_web_purchases`, `num_catalog_purchases`, `num_store_purchases`, `num_discount_purchases`
4. Click **"Upload & Analyze"**
5. Explore comprehensive insights:
   - Summary statistics
   - Interactive visualizations (histograms, scatter plots, bar charts)
   - Data preview table

**Sample CSV provided:** `flask_app/sample_data.csv`

---

## 📁 Project Structure

```
Retail-Buyer-Segmentation/
│
├── README.md                          # Main documentation
├── requirements.txt                   # Project dependencies
├── dashboard.py                       # Streamlit dashboard (optional)
├── project.ipynb                      # Jupyter notebook with analysis
├── Data/
│   └── data.csv                       # Raw customer dataset
│
└── flask_app/                         # Flask Web Application
    ├── app.py                         # Main Flask application
    ├── requirements.txt               # Flask dependencies
    ├── run.bat                        # Windows startup script
    ├── run.sh                         # Linux/macOS startup script
    ├── sample_data.csv                # Test dataset
    │
    ├── templates/                     # HTML Templates
    │   ├── base.html                  # Navigation & layout
    │   ├── home.html                  # Landing page
    │   ├── manual_input.html          # Customer data entry form
    │   ├── results.html               # Single prediction results
    │   ├── insights.html              # CSV analytics dashboard
    │   └── about.html                 # About & information page
    │
    ├── static/                        # Static Assets
    │   ├── css/
    │   │   └── style.css              # Red-black theme styling
    │   ├── js/
    │   │   └── main.js                # Interactive functionality
    │   ├── images/                    # Generated visualizations
    │   └── uploads/                   # Uploaded CSV files
    │
    └── README.md                      # Flask app documentation
```

---

## 📈 Model Performance

The project trains and evaluates **5 classification models**:

| Model | Purpose |
|-------|---------|
| **Logistic Regression** | Baseline linear classifier |
| **Random Forest** | Ensemble method with feature importance |
| **XGBoost** | Gradient boosting for enhanced performance |
| **K-Nearest Neighbors** | Instance-based classification |
| **Support Vector Machine** | Complex decision boundary learning |

### Evaluation Metrics
- **Accuracy**: Overall prediction correctness
- **Precision (Macro)**: Per-segment prediction reliability
- **Recall (Macro)**: Per-segment detection capability
- **F1-Score (Macro)**: Balanced performance metric
- **Confusion Matrix**: Detailed misclassification analysis

---

## 🎨 Design & UI

### Color Scheme
- **Primary Red**: `#dc143c` – Eye-catching accent color
- **Dark Red**: `#8b0000` – Secondary highlighting
- **Black**: `#0a0a0a` – Professional background
- **Light Gray**: `#cccccc` – Text and borders
- **White**: `#ffffff` – Clean contrast

### Features
✅ Bootstrap 5 responsive framework  
✅ Smooth CSS animations and transitions  
✅ Font Awesome iconography  
✅ Mobile-optimized layouts  
✅ Accessible form inputs with validation  

---

## 🔧 Customization

### Change Application Port
Edit `flask_app/app.py` (line 227):
```python
app.run(debug=True, port=5001)  # Change to desired port
```

### Modify Color Theme
Edit `flask_app/static/css/style.css` (lines 7-15) to adjust CSS variables.

### Update ML Model
Edit the clustering function in `flask_app/app.py` (lines 63-88) to experiment with different algorithms or parameters.

### Add New Features
1. Create HTML template in `flask_app/templates/`
2. Add Flask route in `flask_app/app.py`
3. Update navigation in `flask_app/templates/base.html`

---

## 📚 Data Requirements

For optimal results, ensure your CSV file includes:
- **Numeric columns**: Income, Age, Spending amounts
- **No missing values** or handle them before upload
- **Reasonable ranges**: Income (0-300,000+), Age (18-100), Spending (0+)
- **Maximum file size**: 16MB

---

## 🚀 Deployment

### Local Development
```bash
cd flask_app
python app.py
```

### Production with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## 👥 Contributors

This project was developed by a dedicated team of data scientists and ML engineers:

- **Data Lead** – Cleaning, EDA, and preprocessing
- **Clustering Lead** – Segmentation models and interpretation
- **ML Lead** – Classification models and evaluation
- **Documentation Lead** – Integration, documentation, and deployment

---

## 📝 License

This project is licensed under the **MIT License** – see below for details:

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", BASIS, WITHOUT ANY WARRANTY; of any kind,
express or implied, including but not limited to the warranties of
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

---

## 🤝 Support & Feedback

For questions, issues, or suggestions:
- 📧 Open an issue on GitHub
- 🔗 Check existing documentation in `flask_app/README.md`
- 📖 Refer to the quick start guide: `flask_app/QUICKSTART.md`

---

## 🎓 Learning Resources

- [scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Pandas Data Processing](https://pandas.pydata.org/)
- [Machine Learning Fundamentals](https://www.coursera.org/learn/machine-learning)

---

**Made with ❤️ for data-driven business insights**
