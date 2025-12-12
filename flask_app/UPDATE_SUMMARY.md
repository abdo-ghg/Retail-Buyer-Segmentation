# Flask App Update Summary

## Overview
Updated the Flask application to match the notebook's machine learning pipeline with 23 features, 6 models, and 2-cluster segmentation.

## Changes Made

### 1. Backend (app.py)

#### Imports Added
- `DecisionTreeClassifier` from sklearn.tree
- `KNeighborsClassifier` from sklearn.neighbors
- `LogisticRegression` from sklearn.linear_model
- `GaussianNB` from sklearn.naive_bayes
- `XGBClassifier` from xgboost
- `pickle` module

#### Global Variables Added
```python
AVAILABLE_MODELS = {
    'Random Forest': 'rf',
    'XGBoost': 'xgb',
    'Logistic Regression': 'lr',
    'Decision Tree': 'dt',
    'K-Nearest Neighbors': 'knn',
    'Naive Bayes': 'nb'
}
```

#### Function Updates

**perform_clustering():**
- Changed from 4 clusters to 2 clusters
- Updated all 23 features matching notebook:
  - education_level, annual_income, num_children, num_teenagers
  - days_since_last_purchase, 6 spending categories
  - 4 purchase channels, web_visits_last_month
  - total_accepted_campaigns, age, signup_year
  - Derived: total_spent, total_purchases, children, family_size

**manual_input() route:**
- Now passes `models=AVAILABLE_MODELS` to template

**predict_manual() route:**
- Extracts all 23 features from form
- Gets selected model from dropdown
- Calculates derived features (total_spent, total_purchases, children, family_size)
- Uses 2-cluster segmentation:
  - Cluster 0: High-Value Segment (total_spent > $800)
  - Cluster 1: Standard Segment (total_spent ≤ $800)
- Returns enhanced insights including model name

### 2. Frontend (templates/manual_input.html)

#### New Features Added
1. **Model Selection Section:**
   - Dropdown with all 6 available models
   - Default selection: Random Forest

2. **Additional Input Fields:**
   - Education Level (dropdown: Undergraduate/Graduate/Postgraduate)
   - Marital Status (dropdown: Single/Partner)
   - Number of Children (integer)
   - Number of Teenagers (integer)
   - Year Joined (2000-2024, default 2013)
   - Website Visits Last Month (integer)
   - Days Since Last Purchase (integer, default 30)
   - Accepted Marketing Campaigns (0-5)

#### Total Features: 23
**Demographics (7):**
- Education Level, Marital Status, Annual Income, Age
- Number of Children, Number of Teenagers, Year Joined

**Spending (6):**
- Wine, Fruits, Meat, Fish, Sweets, Gold Products

**Purchase Channels (4):**
- Web, Catalog, Store, Discount

**Engagement (3):**
- Website Visits, Days Since Last Purchase, Accepted Campaigns

**Derived Features (3):**
- Total Spent, Total Purchases, Family Size

### 3. Results Page (templates/results.html)

#### Enhancements
1. **Model Display:**
   - Shows which model was used for prediction
   - Displayed as info alert at top

2. **Segment Display:**
   - Shows cluster number alongside segment name
   - Example: "High-Value Segment (Cluster 0)"

3. **Additional Metrics:**
   - Age
   - Family Size
   - Annual Income
   - Web Visits

4. **Updated Recommendations:**
   - Cluster 0 (High-Value): VIP programs, premium products, early access
   - Cluster 1 (Standard): Targeted promotions, value campaigns, loyalty programs

## Segmentation Logic

### 2 Clusters
- **Cluster 0 - High-Value Segment:**
  - Total spending > $800
  - Premium customers with high engagement
  - Color: Success (green)

- **Cluster 1 - Standard Segment:**
  - Total spending ≤ $800
  - Regular customers with moderate spending
  - Color: Info (blue)

## Available Models
1. Random Forest (default)
2. XGBoost
3. Logistic Regression
4. Decision Tree
5. K-Nearest Neighbors
6. Naive Bayes

## Next Steps (Optional)

### To Use Trained Models:
1. Train all 6 models in the notebook
2. Save models using pickle:
   ```python
   import pickle
   for name, model in models_dict.items():
       with open(f'flask_app/models/{name.lower().replace(" ", "_")}.pkl', 'wb') as f:
           pickle.dump(model, f)
   ```

3. Load models in app.py:
   ```python
   MODELS = {}
   for name, code in AVAILABLE_MODELS.items():
       model_path = os.path.join('models', f'{code}.pkl')
       if os.path.exists(model_path):
           with open(model_path, 'rb') as f:
               MODELS[name] = pickle.load(f)
   ```

4. Use loaded models in predict_manual():
   ```python
   if selected_model in MODELS:
       # Preprocess features
       features = np.array([[education_level, annual_income, ...]])
       prediction = MODELS[selected_model].predict(features)[0]
   ```

## Testing

### Manual Input Test:
1. Navigate to `/manual_input`
2. Select a model (e.g., Random Forest)
3. Fill in all 23 fields
4. Submit form
5. Verify results show:
   - Selected model name
   - Correct cluster prediction
   - All metrics
   - Appropriate recommendations

### Test Cases:

**High-Value Customer:**
- Income: $75,000
- Age: 45
- Spending: Wine $500, Meat $400, Fish $200
- Expected: Cluster 0, High-Value Segment

**Standard Customer:**
- Income: $35,000
- Age: 28
- Spending: Fruits $50, Sweets $100, Fish $150
- Expected: Cluster 1, Standard Segment

## Files Modified
1. `flask_app/app.py` - Backend logic
2. `flask_app/templates/manual_input.html` - Input form
3. `flask_app/templates/results.html` - Results display

## Compatibility
- All changes maintain backward compatibility
- Existing CSV upload functionality unchanged
- Red and black theme preserved
- Responsive design maintained
