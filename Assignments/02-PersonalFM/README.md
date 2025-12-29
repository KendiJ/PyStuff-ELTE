# Personal Finance Manager (API Version)

This is the Extended Version of the Personal Finance Manager. It migrates the original CLI application to a REST API architecture using Flask, SQLite, and Scikit-Learn for financial forecasting.

## Key Features

* Persistent Storage: Migrated from CSV to SQLite (finance.db).

* Web API: A Flask-based REST API replacing the command-line menu.

* Statistical Analysis: Automated calculation of Mean, Median, and Standard Deviation.

* AI Forecasting: Uses Linear Regression to predict future income based on history.

## 1. Setup & Installation

### Prerequisites

* Python 3.x installed.

* Postman (Desktop app or Web version) installed for testing API requests.

### Installation Steps

* #### Create a Virtual Environment:

This creates an isolated folder named venv so your project libraries don't conflict with your system.

`python3 -m venv venv`


* #### Activate the Environment:

This tells your terminal to use the Python inside that folder. You should see (venv) appear in your prompt.


Windows:
`venv\Scripts\activate`
 Mac/Linux:
`source venv/bin/activate`


* #### Install Dependencies:

This reads requirements.txt and automatically installs Flask, scikit-learn, etc.

`pip install -r requirements.txt`


Alternatively, you can install them manually:

`pip install Flask`

`pip install scikit-learn`

`pip install numpy`

* #### Run the Application:

This starts the  Server. It will wait for requests from Postman.

`python3 app.py`


## You should see: Running on http://127.0.0.1:5000

Keep this terminal open. If you close it, the site goes down. You will see logs appear here every time you send a request.

### 2. Postman Testing Guide

Since there is no visual menu, we use Postman to send data to the backend. Follow this exact order to populate your database and test the features.

#### Important: For all POST requests, you must set the Content-Type to JSON.

* In the Headers tab, ensure Content-Type is set to application/json.

* In the Body tab, select raw and choose JSON from the dropdown.

### Step 1: Create an Account

You cannot add transactions without an account ID.

Method: POST

* URL: http://127.0.0.1:5000/accounts

Body: Select raw -> JSON
```
{
    "name": "Main Savings",
    "currency": "USD"
}
```

`Expected Output: {"message": "Account created"}`

### Step 2: Add Historical Income (Required for AI Forecast)

The AI needs at least 2 months of history to draw a trend line. Let's add 3 months.

Entry 1 (January):

Method: POST

* URL: http://127.0.0.1:5000/income

Body (JSON):
```
{
    "account_id": 1,
    "date": "2025-01-15",
    "amount": 3000,
    "source": "Salary"
}
```

Entry 2 (February - Income went up):

Method: POST

URL: http://127.0.0.1:5000/income

Body (JSON):
```
{
    "account_id": 1,
    "date": "2025-02-15",
    "amount": 3200,
    "source": "Salary"
}
```

Entry 3 (March - Income went up again):

Method: POST

URL: http://127.0.0.1:5000/income

Body (JSON):
```
{
    "account_id": 1,
    "date": "2025-03-15",
    "amount": 3400,
    "source": "Salary"
}
```


### Step 3: Add Transactions (Required for Stats)

Method: POST

* URL: http://127.0.0.1:5000/transactions

Body (JSON):
```
{
    "account_id": 1,
    "date": "2025-03-20",
    "amount": 50.50,
    "type": "expense",
    "category": "Groceries",
    "note": "Weekly shopping"
}
```

(Click "Send" a few times, maybe change the amount to 100 or 20 to vary the data).

### Step 4: Get Statistical Summary

Method: GET

* URL: http://127.0.0.1:5000/stats/summary

Expected Output: A JSON object showing the Mean, Median, Min, Max, and Std Dev of your transactions.

### Step 5: Get Income Forecast (The AI Feature)

Method: GET

* URL: http://127.0.0.1:5000/stats/income_forecast

Expected Output:
```
{
    "history": [ ...your past months... ],
    "forecast": [
        { "month_offset": 1, "predicted_income": 3600.0 },
        { "month_offset": 2, "predicted_income": 3800.0 },
        { "month_offset": 3, "predicted_income": 4000.0 }
    ]
}
```

* The AI sees your income rose by 200 each month, so it predicts it will continue rising. This is explained in the video

## To exit the server:
* Press CTRL+C to quit
* type `deactivate` to deactivate the virtual enviroment
