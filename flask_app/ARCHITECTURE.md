# Application Architecture & Flow

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                         │
│                    http://localhost:5000                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      FLASK WEB SERVER                       │
│                         (app.py)                            │
│                                                             │
│  Routes:                                                    │
│  • GET  /              → home.html                          │
│  • GET  /manual_input  → manual_input.html                  │
│  • POST /predict_manual → results.html                      │
│  • POST /upload        → insights.html                      │
│  • GET  /about         → about.html                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATA PROCESSING LAYER                     │
│                                                             │
│  • preprocess_data()       → Clean & engineer features     │
│  • perform_clustering()    → K-Means segmentation          │
│  • generate_visualizations() → Create matplotlib charts     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    MACHINE LEARNING                         │
│                                                             │
│  • scikit-learn: KMeans, MinMaxScaler                       │
│  • pandas: Data manipulation                                │
│  • matplotlib/seaborn: Visualizations                       │
└─────────────────────────────────────────────────────────────┘
```

## User Flow - Manual Input

```
┌──────────┐
│  START   │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│   Home Page     │
└────┬────────────┘
     │ Click "Manual Input"
     ▼
┌─────────────────┐
│  Manual Input   │
│     Form        │
└────┬────────────┘
     │ Fill form & Submit
     ▼
┌─────────────────┐
│  Flask Backend  │
│  Process Data   │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Calculate:     │
│  • Total Spent  │
│  • Segment      │
│  • Metrics      │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Results Page   │
│  • Segment      │
│  • Metrics      │
│  • Recommendations
└────┬────────────┘
     │
     ▼
┌──────────┐
│   END    │
└──────────┘
```

## User Flow - CSV Upload

```
┌──────────┐
│  START   │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│   Home Page     │
└────┬────────────┘
     │ Upload CSV File
     ▼
┌─────────────────┐
│  Validate File  │
│  • Extension    │
│  • Size < 16MB  │
└────┬────────────┘
     │ ✅ Valid
     ▼
┌─────────────────┐
│  Save to        │
│  /uploads/      │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Read CSV       │
│  pandas.read_csv│
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Preprocess     │
│  • Handle nulls │
│  • Feature eng. │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  K-Means        │
│  Clustering     │
│  • 4 Segments   │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Generate       │
│  Visualizations │
│  • 4+ Charts    │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Calculate      │
│  Statistics     │
│  • 6 Metrics    │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Insights Page  │
│  • Stats Cards  │
│  • Charts       │
│  • Data Table   │
└────┬────────────┘
     │
     ▼
┌──────────┐
│   END    │
└──────────┘
```

## Data Processing Pipeline

```
Raw Data Input
      │
      ▼
┌──────────────────┐
│  Data Validation │
│  • Check columns │
│  • Check types   │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Handle Missing  │
│  • Median (num)  │
│  • Mode (cat)    │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Feature Eng.    │
│  • total_spent   │
│  • total_purchases
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Scaling         │
│  MinMaxScaler    │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  ML Model        │
│  K-Means (k=4)   │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Results         │
│  • Clusters      │
│  • Insights      │
└──────────────────┘
```

## File Structure & Relationships

```
flask_app/
│
├── app.py ───────────────────┐
│   │                         │
│   ├─→ templates/ ───────────┼─→ Renders HTML
│   │   ├─ base.html          │
│   │   ├─ home.html          │
│   │   ├─ manual_input.html  │
│   │   ├─ results.html       │
│   │   ├─ insights.html      │
│   │   └─ about.html         │
│   │                         │
│   ├─→ static/ ──────────────┼─→ Serves Assets
│   │   ├─ css/style.css      │
│   │   ├─ js/main.js         │
│   │   └─ images/ (dynamic)  │
│   │                         │
│   └─→ uploads/ ─────────────┼─→ Stores CSV
│                             │
├── requirements.txt ─────────┼─→ Dependencies
│                             │
├── run.bat ──────────────────┼─→ Windows Launcher
├── run.sh ───────────────────┼─→ Unix Launcher
│                             │
└── sample_data.csv ──────────┴─→ Test Data
```

## Technology Stack

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                   │
├─────────────────────────────────────────────────────┤
│  • HTML5                                            │
│  • CSS3 (Custom Red/Black Theme)                    │
│  • JavaScript (Vanilla)                             │
│  • Bootstrap 5                                      │
│  • Font Awesome Icons                               │
└────────────────────┬────────────────────────────────┘
                     │
┌─────────────────────────────────────────────────────┐
│                    BACKEND LAYER                    │
├─────────────────────────────────────────────────────┤
│  • Flask 3.0.0 (Web Framework)                      │
│  • Werkzeug (WSGI Utilities)                        │
│  • Jinja2 (Templating)                              │
└────────────────────┬────────────────────────────────┘
                     │
┌─────────────────────────────────────────────────────┐
│                  DATA SCIENCE LAYER                 │
├─────────────────────────────────────────────────────┤
│  • pandas 2.0.3 (Data Manipulation)                 │
│  • NumPy 1.24.3 (Numerical Computing)               │
│  • scikit-learn 1.3.0 (Machine Learning)            │
│    - KMeans Clustering                              │
│    - MinMaxScaler                                   │
│  • matplotlib 3.7.2 (Visualization)                 │
│  • seaborn 0.12.2 (Statistical Plots)               │
└─────────────────────────────────────────────────────┘
```

## Request-Response Cycle

```
Client Browser                Flask Server               ML Pipeline
      │                            │                         │
      │  HTTP GET /                │                         │
      ├───────────────────────────>│                         │
      │                            │                         │
      │  home.html + CSS/JS        │                         │
      │<───────────────────────────┤                         │
      │                            │                         │
      │  POST /upload (CSV file)   │                         │
      ├───────────────────────────>│                         │
      │                            │  preprocess_data()      │
      │                            ├────────────────────────>│
      │                            │                         │
      │                            │  perform_clustering()   │
      │                            ├────────────────────────>│
      │                            │                         │
      │                            │  generate_viz()         │
      │                            ├────────────────────────>│
      │                            │                         │
      │                            │  Results (clusters,     │
      │                            │  stats, plots)          │
      │                            │<────────────────────────┤
      │                            │                         │
      │  insights.html + images    │                         │
      │<───────────────────────────┤                         │
      │                            │                         │
```

## Customer Segmentation Logic

```
Input Features
      │
      ├─→ annual_income
      ├─→ age
      ├─→ total_spent
      ├─→ total_purchases
      ├─→ spend_wine
      ├─→ spend_meat
      ├─→ ... (20 features)
      │
      ▼
┌──────────────────┐
│  MinMaxScaler    │
│  Scale 0-1       │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  K-Means (k=4)   │
│  • Cluster 0     │
│  • Cluster 1     │
│  • Cluster 2     │
│  • Cluster 3     │
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│  Business Rules  │
│  Total Spent:    │
│  • > $1000 = Premium
│  • $500-1000 = Regular
│  • < $500 = Budget
└────┬─────────────┘
     │
     ▼
Customer Segment
```

## Visualization Generation

```
DataFrame (df)
      │
      ▼
┌─────────────────────┐
│  Age Distribution   │
│  plt.hist()         │
│  → age_distribution.png
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│  Income vs Spend    │
│  plt.scatter()      │
│  → income_vs_spend.png
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│  Cluster Distribution│
│  plt.bar()          │
│  → cluster_distribution.png
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│  Spending Category  │
│  plt.bar()          │
│  → spending_by_category.png
└─────────────────────┘
      │
      ▼
  Save to static/images/
```

## Error Handling Flow

```
User Action
      │
      ▼
┌──────────────────┐
│  Validation      │
│  • File type?    │
│  • File size?    │
│  • Required cols?│
└────┬─────────────┘
     │
     ├─✅ Valid
     │  └─→ Process Data
     │
     └─❌ Invalid
        └─→ Flash Error Message
            └─→ Redirect to Home
```

---

This diagram provides a complete visual overview of how all components work together!
