# Quick Start Guide

## Running the Application

### Windows
Simply double-click `run.bat` or run in terminal:
```bash
run.bat
```

### macOS/Linux
Make the script executable and run:
```bash
chmod +x run.sh
./run.sh
```

### Manual Start
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run app
python app.py
```

## Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

## First Time Setup

The `run.bat` or `run.sh` script will automatically:
1. Create virtual environment (if needed)
2. Install all dependencies
3. Create required directories
4. Start the Flask server

## Testing with Sample Data

### Manual Input Example:
- Annual Income: 50000
- Age: 35
- Wine Spending: 100
- Meat Spending: 200
- Web Purchases: 5
- Store Purchases: 10

### CSV Upload:
Use the sample data from `Data/data.csv` in your project folder.

## Stopping the Server

Press `Ctrl + C` in the terminal to stop the Flask server.

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, edit `app.py` line 227:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port
```

### Module Not Found Errors
```bash
pip install -r requirements.txt
```

### Permission Errors (Linux/macOS)
```bash
chmod +x run.sh
sudo chown -R $USER uploads/
```

## Features Overview

✅ **Home Page**: Choose between manual input or CSV upload
✅ **Manual Input**: Enter single customer data
✅ **CSV Upload**: Bulk process multiple customers
✅ **Insights Page**: View statistics and visualizations
✅ **About Page**: Learn about the application

Enjoy using the Retail Buyer Segmentation App! 🚀
