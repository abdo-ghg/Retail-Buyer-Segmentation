# Retail Buyer Segmentation - Flask Web Application

A modern, production-ready Flask web application for retail customer segmentation using machine learning. Features a sleek red-and-black theme with comprehensive analytics and visualization capabilities.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

- **Dual Input Methods**
  - Manual data entry through user-friendly forms
  - Bulk CSV file upload for processing multiple customers

- **Machine Learning**
  - K-Means clustering for customer segmentation
  - Automated data preprocessing and feature engineering
  - Intelligent customer profiling

- **Visual Analytics**
  - Interactive charts and graphs
  - Age distribution analysis
  - Income vs spending correlation
  - Category-wise spending breakdown
  - Customer segment distribution

- **Modern UI/UX**
  - Red and black professional theme
  - Responsive Bootstrap 5 design
  - Smooth animations and transitions
  - Mobile-friendly interface

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## 🛠️ Installation

### 1. Clone or Download the Repository

```bash
cd flask_app
```

### 2. Create Virtual Environment (Recommended)

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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Required Directories

The application will automatically create these, but you can create them manually:

```bash
mkdir uploads
mkdir static\images
```

## 🚀 Running the Application

### Development Mode

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Production Mode

For production deployment, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📁 Project Structure

```
flask_app/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── home.html              # Landing page
│   ├── manual_input.html      # Manual data entry form
│   ├── results.html           # Single customer results
│   ├── insights.html          # CSV upload insights
│   └── about.html             # About page
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Custom red-black theme
│   ├── js/
│   │   └── main.js            # JavaScript functionality
│   └── images/                # Generated plots (auto-created)
│
└── uploads/                    # Uploaded CSV files (auto-created)
```

## 📊 Usage Guide

### Manual Input

1. Navigate to **Home** page
2. Click **"Start Manual Input"**
3. Fill in customer information:
   - Annual Income
   - Age
   - Spending by category (Wine, Fruits, Meat, Fish, Sweets, Gold)
   - Purchase channels (Web, Catalog, Store, Discount)
4. Click **"Predict Segment"**
5. View results with:
   - Customer segment classification
   - Spending metrics
   - Personalized recommendations

### CSV Upload

1. Navigate to **Home** page
2. Click **"Choose File"** under CSV Upload
3. Select a CSV file (max 16MB) with required columns:
   - `annual_income`
   - `age`
   - `spend_wine`, `spend_fruits`, `spend_meat`, `spend_fish`, `spend_sweets`, `spend_gold`
   - `num_web_purchases`, `num_catalog_purchases`, `num_store_purchases`, `num_discount_purchases`
4. Click **"Upload & Analyze"**
5. View comprehensive insights:
   - Summary statistics
   - Visual analytics (4+ charts)
   - Data preview table
   - Customer segment distribution

### CSV Format Example

```csv
annual_income,age,spend_wine,spend_fruits,spend_meat,spend_fish,spend_sweets,spend_gold,num_web_purchases,num_catalog_purchases,num_store_purchases,num_discount_purchases
58138,64,635,88,546,172,88,88,8,10,4,3
46344,67,11,1,42,98,0,0,1,1,2,2
71613,56,426,49,127,111,21,42,8,2,10,1
```

## 🎨 Customization

### Changing Color Theme

Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-red: #dc143c;    /* Main red color */
    --dark-red: #8b0000;       /* Darker red for hover */
    --black: #0a0a0a;          /* Background black */
    --dark-gray: #1a1a1a;      /* Card backgrounds */
}
```

### Adding New Features

1. Add route in `app.py`:
```python
@app.route('/new-feature')
def new_feature():
    return render_template('new_feature.html')
```

2. Create template in `templates/new_feature.html`
3. Update navigation in `templates/base.html`

## 🔧 Configuration

Key configurations in `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
```

## 📈 Machine Learning Details

### Preprocessing Pipeline

1. **Feature Engineering**
   - Calculate total spending
   - Calculate total purchases
   - Compute derived features

2. **Data Cleaning**
   - Handle missing values (median/mode imputation)
   - Remove duplicates
   - Normalize numeric features

3. **Clustering**
   - Algorithm: K-Means
   - Number of clusters: 4
   - Features: Income, age, spending, purchases
   - Scaling: MinMaxScaler

### Customer Segments

- **Premium Customer**: High spending (>$1000)
- **Regular Customer**: Moderate spending ($500-$1000)
- **Budget Customer**: Cost-conscious (<$500)

## 🐛 Troubleshooting

### Port Already in Use

Change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Import Errors

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### File Upload Issues

Check file permissions for `uploads/` directory:
```bash
chmod 755 uploads
```

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/manual_input` | GET | Manual input form |
| `/predict_manual` | POST | Process manual input |
| `/upload` | POST | Process CSV upload |
| `/about` | GET | About page |

## 🔐 Security Features

- File type validation (CSV only)
- File size limits (16MB)
- Secure filename handling
- Input sanitization
- CSRF protection via secret key

## 🌐 Deployment Options

### Heroku

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 📞 Support

For issues or questions:
- Check the [Troubleshooting](#-troubleshooting) section
- Review error logs in the console
- Ensure all dependencies are installed correctly

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🎯 Future Enhancements

- [ ] User authentication
- [ ] Database integration
- [ ] Export results to PDF
- [ ] Real-time dashboard
- [ ] A/B testing capabilities
- [ ] Email notifications
- [ ] API endpoints for integration

## 👏 Acknowledgments

- Built with Flask and scikit-learn
- UI powered by Bootstrap 5
- Icons from Font Awesome
- Visualization with Matplotlib/Seaborn

---

**Made with ❤️ for Retail Analytics**
