from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
import db

app = Flask(__name__)

# Initialize the database when the app starts
with app.app_context():
    db.init_db()

# Root Route 
@app.route('/')
def home():
    return "Personal Finance API is running! Use /transactions or /stats endpoints."

# Account Endpoints 
@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify(db.get_accounts())

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    if not data or 'name' not in data or 'currency' not in data:
        return jsonify({"error": "Missing name or currency"}), 400
    db.add_account(data['name'], data['currency'])
    return jsonify({"message": "Account created"}), 201

# Transactions endpoint
@app.route('/transactions', methods=['GET'])
def transactions_list():
    # Read query parameters like ?from=2023-01-01
    start = request.args.get('from')
    end = request.args.get('to')
    data = db.get_transactions(start, end)
    return jsonify(data)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    required = ['account_id', 'date', 'amount', 'type', 'category']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
    
    db.add_transaction(
        data['account_id'], data['date'], data['amount'], 
        data['type'], data['category'], data.get('note', '')
    )
    return jsonify({"message": "Transaction added"}), 201

# Income endpoint
@app.route('/income', methods=['GET'])
def income_list():
    return jsonify(db.get_income())

@app.route('/income', methods=['POST'])
def add_income():
    data = request.json
    required = ['account_id', 'date', 'amount', 'source']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
        
    db.add_income(data['account_id'], data['date'], data['amount'], data['source'])
    return jsonify({"message": "Income recorded"}), 201

# Statistical Analysis 
@app.route('/stats/summary', methods=['GET'])
def stats_summary():
    # We analyze transactions for this summary
    transactions = db.get_transactions()
    if not transactions:
        return jsonify({"message": "No data available"}), 200
    
    # Extract just the amounts into a numpy array
    amounts = [t['amount'] for t in transactions]
    
    summary = {
        "count": len(amounts),
        "mean": float(np.mean(amounts)),
        "median": float(np.median(amounts)),
        "min": float(np.min(amounts)),
        "max": float(np.max(amounts)),
        "std_dev": float(np.std(amounts))
    }
    return jsonify(summary)

# Linear Regression 
@app.route('/stats/income_forecast', methods=['GET'])
def forecast():
    # Get data grouped by month
    history = db.get_monthly_income()
    
    # We need at least 2 months to draw a line
    if len(history) < 2:
        return jsonify({"error": "Not enough data to forecast (need 2+ months)"}), 400
    
    # 2. Prepare data for Scikit-Learn

    X = []
    y = []
    for i, record in enumerate(history):
        X.append([i])
        y.append(record['total'])
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next 3 months
    last_month_index = len(history)
    future_X = [[last_month_index], [last_month_index + 1], [last_month_index + 2]]
    predictions = model.predict(future_X)
    
    # Format results
    forecast_results = []
    for i, pred in enumerate(predictions):
        forecast_results.append({
            "month_offset": i + 1,
            "predicted_income": round(pred, 2)
        })
        
    return jsonify({
        "history": history,
        "forecast": forecast_results
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)