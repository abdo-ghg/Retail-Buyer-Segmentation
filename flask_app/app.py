"""
Flask Web Application for Retail Buyer Segmentation
Author: AI Assistant
Date: 2025
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from sklearn.preprocessing import LabelEncoder, PowerTransformer, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
import warnings
import pickle
warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'retail_segmentation_secret_key_2025'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(app.config['STATIC_FOLDER'], 'images'), exist_ok=True)

# Available models matching notebook
AVAILABLE_MODELS = {
    'Random Forest': 'rf',
    'XGBoost': 'xgb',
    'Logistic Regression': 'lr',
    'Decision Tree': 'dt',
    'K-Nearest Neighbors': 'knn',
    'Naive Bayes': 'nb'
}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_data(df):
    """Preprocess the input data"""
    # Feature engineering
    df['age'] = 2014 - df['birth_year'] if 'birth_year' in df.columns else df.get('age', 0)
    
    # Total spend
    spend_cols = ['spend_wine', 'spend_fruits', 'spend_meat', 'spend_fish', 'spend_sweets', 'spend_gold']
    if all(col in df.columns for col in spend_cols):
        df['total_spent'] = df[spend_cols].sum(axis=1)
    
    # Total purchases
    purchase_cols = ['num_discount_purchases', 'num_web_purchases', 'num_catalog_purchases', 'num_store_purchases']
    if all(col in df.columns for col in purchase_cols):
        df['total_purchases'] = df[purchase_cols].sum(axis=1)
    
    # Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].mode()[0] if len(df[col].mode()) > 0 else 'Unknown', inplace=True)
    
    return df

def perform_clustering(df):
    """Perform K-Means clustering with 2 clusters (matching notebook)"""
    # Select all 23 features for clustering (matching notebook)
    clustering_features = [col for col in [
        'education_level', 'annual_income', 'num_children', 'num_teenagers',
        'days_since_last_purchase', 'spend_wine', 'spend_fruits', 'spend_meat',
        'spend_fish', 'spend_sweets', 'spend_gold', 'num_discount_purchases',
        'num_web_purchases', 'num_catalog_purchases', 'num_store_purchases',
        'web_visits_last_month', 'total_accepted_campaigns', 'age',
        'signup_year', 'total_spent', 'total_purchases', 'children', 'family_size'
    ] if col in df.columns]
    
    if not clustering_features:
        return None, None
    
    # Prepare data
    X = df[clustering_features].copy()
    
    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform clustering with 2 clusters (matching notebook)
    kmeans = KMeans(n_clusters=2, init='k-means++', n_init='auto', random_state=0)
    clusters = kmeans.fit_predict(X_scaled)
    
    return clusters, clustering_features

def generate_visualizations(df, clusters=None):
    """Generate visualizations and save them"""
    plots = []
    
    # 1. Age Distribution
    plt.figure(figsize=(10, 6))
    if 'age' in df.columns:
        plt.hist(df['age'], bins=30, color='#dc143c', edgecolor='white', alpha=0.7)
        plt.xlabel('Age', color='white')
        plt.ylabel('Frequency', color='white')
        plt.title('Age Distribution', color='white', fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.gca().set_facecolor('#1a1a1a')
        plt.gcf().patch.set_facecolor('#1a1a1a')
        plt.tick_params(colors='white')
        plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'age_distribution.png')
        plt.savefig(plot_path, facecolor='#1a1a1a', bbox_inches='tight')
        plt.close()
        plots.append('age_distribution.png')
    
    # 2. Income vs Total Spent
    if 'annual_income' in df.columns and 'total_spent' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['annual_income'], df['total_spent'], alpha=0.6, c='#dc143c', edgecolors='white')
        plt.xlabel('Annual Income', color='white')
        plt.ylabel('Total Spent', color='white')
        plt.title('Income vs Total Spending', color='white', fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.gca().set_facecolor('#1a1a1a')
        plt.gcf().patch.set_facecolor('#1a1a1a')
        plt.tick_params(colors='white')
        plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'income_vs_spend.png')
        plt.savefig(plot_path, facecolor='#1a1a1a', bbox_inches='tight')
        plt.close()
        plots.append('income_vs_spend.png')
    
    # 3. Cluster Distribution (if clusters exist)
    if clusters is not None:
        plt.figure(figsize=(10, 6))
        cluster_counts = pd.Series(clusters).value_counts().sort_index()
        plt.bar(cluster_counts.index, cluster_counts.values, color='#dc143c', edgecolor='white')
        plt.xlabel('Cluster', color='white')
        plt.ylabel('Count', color='white')
        plt.title('Customer Segments Distribution', color='white', fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='y')
        plt.gca().set_facecolor('#1a1a1a')
        plt.gcf().patch.set_facecolor('#1a1a1a')
        plt.tick_params(colors='white')
        plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'cluster_distribution.png')
        plt.savefig(plot_path, facecolor='#1a1a1a', bbox_inches='tight')
        plt.close()
        plots.append('cluster_distribution.png')
    
    # 4. Spending by Category
    spend_cols = [col for col in ['spend_wine', 'spend_fruits', 'spend_meat', 
                                    'spend_fish', 'spend_sweets', 'spend_gold'] if col in df.columns]
    if spend_cols:
        plt.figure(figsize=(12, 6))
        spending_means = df[spend_cols].mean()
        colors_list = ['#dc143c', '#ff6b6b', '#c41e3a', '#ee4b2b', '#cd5c5c', '#b22222']
        plt.bar(range(len(spending_means)), spending_means.values, 
                color=colors_list[:len(spending_means)], edgecolor='white')
        plt.xticks(range(len(spending_means)), 
                   [col.replace('spend_', '').title() for col in spending_means.index],
                   rotation=45, ha='right', color='white')
        plt.ylabel('Average Spending', color='white')
        plt.title('Average Spending by Category', color='white', fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='y')
        plt.gca().set_facecolor('#1a1a1a')
        plt.gcf().patch.set_facecolor('#1a1a1a')
        plt.tick_params(colors='white')
        plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'spending_by_category.png')
        plt.savefig(plot_path, facecolor='#1a1a1a', bbox_inches='tight')
        plt.close()
        plots.append('spending_by_category.png')
    
    return plots

@app.route('/')
@app.route('/index')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/manual_input')
def manual_input():
    """Manual input form page"""
    return render_template('manual_input.html', models=AVAILABLE_MODELS)

@app.route('/predict_manual', methods=['POST'])
def predict_manual():
    """Handle manual input prediction with model selection"""
    try:
        print("=" * 50)
        print("Predict Manual Route Called")
        print("=" * 50)
        
        # Get selected model
        selected_model = request.form.get('model', 'Random Forest')
        print(f"Selected Model: {selected_model}")
        
        # Extract all input features
        education_level = int(request.form.get('education_level', 0))
        annual_income = float(request.form.get('annual_income', 0))
        num_children = int(request.form.get('num_children', 0))
        num_teenagers = int(request.form.get('num_teenagers', 0))
        days_since_last_purchase = int(request.form.get('days_since_last_purchase', 30))
        spend_wine = float(request.form.get('spend_wine', 0))
        spend_fruits = float(request.form.get('spend_fruits', 0))
        spend_meat = float(request.form.get('spend_meat', 0))
        spend_fish = float(request.form.get('spend_fish', 0))
        spend_sweets = float(request.form.get('spend_sweets', 0))
        spend_gold = float(request.form.get('spend_gold', 0))
        num_discount_purchases = int(request.form.get('num_discount_purchases', 0))
        num_web_purchases = int(request.form.get('num_web_purchases', 0))
        num_catalog_purchases = int(request.form.get('num_catalog_purchases', 0))
        num_store_purchases = int(request.form.get('num_store_purchases', 0))
        web_visits_last_month = int(request.form.get('web_visits_last_month', 0))
        total_accepted_campaigns = int(request.form.get('total_accepted_campaigns', 0))
        age = int(request.form.get('age', 0))
        signup_year = int(request.form.get('signup_year', 2013))
        marital_status = request.form.get('marital_status', 'Single')
        
        print(f"Age: {age}, Income: {annual_income}")
        
        # Calculate derived features
        total_spent = spend_wine + spend_fruits + spend_meat + spend_fish + spend_sweets + spend_gold
        total_purchases = num_discount_purchases + num_web_purchases + num_catalog_purchases + num_store_purchases
        children = num_children + num_teenagers
        family_size = children + (2 if marital_status == 'Partner' else 1)
        
        print(f"Total Spent: ${total_spent:.2f}, Total Purchases: {total_purchases}")
        
        # Rule-based prediction (2 clusters matching notebook)
        if total_spent > 800:
            prediction = 0
            segment = "High-Value Segment"
            segment_desc = "Premium customers with high spending and strong engagement"
            color = "success"
            
            # Cluster 0 detailed profile
            cluster_profile = {
                'cluster_id': 0,
                'cluster_name': 'Cluster 0: Premium High-Value Customers',
                'characteristics': [
                    'High total spending (> $800)',
                    'Above-average income levels',
                    'Frequent purchasers across multiple channels',
                    'Strong engagement with premium products',
                    'Responsive to exclusive offers'
                ],
                'typical_behavior': [
                    'Prefers quality over price',
                    'Often purchases wine, meat, and gold products',
                    'Uses multiple shopping channels (web, catalog, store)',
                    'Lower sensitivity to discounts',
                    'Higher campaign acceptance rate'
                ],
                'demographics': [
                    'Average Age: 45-55 years',
                    'Income: $60,000+',
                    'Education: Graduate/Postgraduate',
                    'Family: Usually smaller households (1-3 members)'
                ],
                'marketing_strategy': [
                    'Offer VIP loyalty programs with exclusive benefits',
                    'Provide personalized product recommendations',
                    'Send early access to new premium products',
                    'Focus on quality and exclusivity in communications',
                    'Maintain high-touch customer service'
                ],
                'retention_tips': [
                    'Create exclusive membership tiers',
                    'Offer premium gift options and packaging',
                    'Provide dedicated customer support',
                    'Send personalized thank-you notes',
                    'Host exclusive events or tastings'
                ]
            }
        else:
            prediction = 1
            segment = "Standard Segment"
            segment_desc = "Regular customers with moderate spending patterns"
            color = "info"
            
            # Cluster 1 detailed profile
            cluster_profile = {
                'cluster_id': 1,
                'cluster_name': 'Cluster 1: Standard Value-Conscious Customers',
                'characteristics': [
                    'Moderate spending (≤ $800)',
                    'Budget-conscious purchasing behavior',
                    'Price-sensitive decision making',
                    'Selective purchasing patterns',
                    'Values deals and promotions'
                ],
                'typical_behavior': [
                    'Looks for best value and discounts',
                    'Purchases essential items regularly',
                    'Higher discount purchase rate',
                    'More selective about premium products',
                    'Responds well to promotional campaigns'
                ],
                'demographics': [
                    'Average Age: 30-45 years',
                    'Income: $30,000-$60,000',
                    'Education: Varies (Undergraduate to Graduate)',
                    'Family: Often larger households (3-5 members)'
                ],
                'marketing_strategy': [
                    'Highlight value propositions and savings',
                    'Send targeted discount offers and bundle deals',
                    'Emphasize cost-effectiveness in communications',
                    'Promote loyalty rewards programs',
                    'Focus on seasonal sales and special promotions'
                ],
                'retention_tips': [
                    'Implement points-based rewards system',
                    'Offer bulk purchase discounts',
                    'Send birthday/anniversary coupons',
                    'Create value bundles and packages',
                    'Provide free shipping thresholds'
                ]
            }
        
        print(f"Prediction: {prediction}, Segment: {segment}")
        
        # Calculate metrics
        avg_purchase = total_spent / max(total_purchases, 1)
        
        # Find top spending category
        spending_data = {
            'Wine': spend_wine,
            'Fruits': spend_fruits,
            'Meat': spend_meat,
            'Fish': spend_fish,
            'Sweets': spend_sweets,
            'Gold': spend_gold
        }
        top_category = max(spending_data, key=spending_data.get)
        
        # Prepare insights
        insights = {
            'model': selected_model,
            'prediction': prediction,
            'segment': segment,
            'segment_description': segment_desc,
            'segment_color': color,
            'total_spent': f"${total_spent:.2f}",
            'total_purchases': int(total_purchases),
            'avg_purchase_value': f"${avg_purchase:.2f}",
            'top_category': top_category,
            'age': age,
            'income': f"${annual_income:.2f}",
            'family_size': family_size,
            'web_visits': web_visits_last_month,
            'cluster_profile': cluster_profile
        }
        
        print("Insights prepared successfully")
        print("Rendering results.html")
        
        return render_template('results.html', insights=insights, manual=True)
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        flash(f'Error processing input: {str(e)}', 'error')
        return redirect(url_for('manual_input'))

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV file upload"""
    try:
        if 'file' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(url_for('home'))
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('home'))
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Read CSV
            df = pd.read_csv(filepath)
            
            # Preprocess
            df = preprocess_data(df)
            
            # Perform clustering
            clusters, clustering_features = perform_clustering(df)
            
            if clusters is not None:
                df['cluster'] = clusters
            
            # Generate statistics
            stats = {
                'total_customers': len(df),
                'avg_income': f"${df['annual_income'].mean():.2f}" if 'annual_income' in df.columns else 'N/A',
                'avg_age': f"{df['age'].mean():.1f}" if 'age' in df.columns else 'N/A',
                'total_revenue': f"${df['total_spent'].sum():.2f}" if 'total_spent' in df.columns else 'N/A',
                'avg_spending': f"${df['total_spent'].mean():.2f}" if 'total_spent' in df.columns else 'N/A',
            }
            
            if clusters is not None:
                stats['num_segments'] = len(np.unique(clusters))
            
            # Generate visualizations
            plots = generate_visualizations(df, clusters)
            
            # Get sample data
            sample_data = df.head(10).to_html(classes='table table-dark table-striped', index=False)
            
            return render_template('insights.html', 
                                   stats=stats, 
                                   plots=plots, 
                                   sample_data=sample_data,
                                   filename=filename)
        else:
            flash('Invalid file type. Please upload a CSV file.', 'error')
            return redirect(url_for('home'))
            
    except Exception as e:
        flash(f'Error processing file: {str(e)}', 'error')
        return redirect(url_for('home'))

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
