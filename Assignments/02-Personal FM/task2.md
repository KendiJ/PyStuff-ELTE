# **Assignment 2 – Personal Finance Manager (Extended Version)**

**Total: 25 points**
**Deadline: December 19, 23:59**
**Submission:** Source code + SQLite DB file + video presentation (MP4 or link)

---

## **1. Overview**

In this assignment, you will extend your personal finance manager by:

1. Migrating from CSV to **SQLite** for persistent data storage
2. Creating a Flask-based REST API to access tshe data instead of CLI
3. Integrating **statistical analysis** of financial data
4. Implementing **linear regression** to predict future income
5. Creating a **short video presentation** demonstrating your application

This assignment builds on the functionality from Assignment 1 and introduces concepts from databases, web APIs, and data analysis.

---

# **2. Requirements and Grading (25 points)**

---

## **A. SQLite Database + Flask API (10 points)**

### **1. Database (4 points)**

You must use **SQLite** instead of CSV.
Create a database schema with at least the following tables:

* **accounts(id, name, currency)**
* **transactions(id, account_id, date, amount, type, category, note)**
* **income(id, account_id, date, amount, source)**

**Points:**

* Database schema created correctly — *2 pts*
* Insert, update, delete operations implemented — *2 pts*

### **2. Flask API (6 points)**

Implement a minimal REST API with endpoints such as:

* `GET /transactions?from=YYYY-MM-DD&to=YYYY-MM-DD`
* `POST /transactions`
* `GET /income`
* `POST /income`
* `GET /stats/summary` (for statistics)
* `GET /stats/income_forecast`

You must test your API using curl or Postman.
(A simple HTML/JS frontend is optional, not required.)

**Points:**

* Basic endpoints work correctly — *4 pts*
* Correct integration with SQLite (queries, input validation) — *2 pts*

---

## **B. Statistical Analysis (5 points)**

Implement static analysis on transactions or income over a selected period.
Your API should compute at least:

* **mean**
* **median**
* **min**
* **max**
* **standard deviation**
* (Optional) simple distribution by category

Return the results in JSON format via an endpoint such as:

```
GET /stats/summary?from=&to=
```

**Points:**

* Correct calculation of central tendency — *2 pts*
* Additional stats (std, min/max, category distribution) — *3 pts*

---

## **C. Linear Regression for Income Prediction (5 points)**

Implement a simple income forecasting feature:

1. Aggregate monthly income (e.g., sum per month)
2. Fit a **linear regression model**
3. Predict **the next N months** (e.g., 3 months)
4. Return output as JSON:

```json
{
  "history": [
    {"month": "2025-01", "income": 300000},
    {"month": "2025-02", "income": 320000}
  ],
  "forecast": [
    {"month": "2025-03", "predicted_income": 330000},
    {"month": "2025-04", "predicted_income": 340000}
  ]
}
```

You may use:

* Use scikit-learn (LinearRegression) to implement the income prediction.
* Alternatively, you may use NumPy or your own implementation.

**Points:**

* Correct aggregation of monthly data — *2 pts*
* Working regression + forecast endpoint — *3 pts*

---

## **D. Video Presentation (5 points)**

Prepare a **5–7 minute video** demonstrating your app.

### **Your video must include:**

1. **Introduction (30–60 seconds)**

   * What your app does
   * What features you implemented

2. **Database demonstration**

   * Show your SQLite tables (DB Browser or CLI)
   * Explain briefly what data is stored

3. **API demonstration using Postman, browser, or curl**

   * Add a transaction or income
   * Retrieve data
   * Show summary statistics endpoint
   * Show income forecast endpoint

4. **Short explanation of your regression approach**

   * Very simple explanation is enough
   * No deep math required

5. **Conclusion**

   * What you learned
   * Any challenges you faced

**Points:**

Clear explanation and logical structure — 2 pts
Demonstration of the application and its features — 2 pts
Good audio and visual quality — 1 pt

No need to show your face; screen recording with voice is enough.

---

# **3. Submission Package**

Upload a ZIP file containing:

```
/project
    app.py
    db.py
    models.py (optional)
    requirements.txt
    finance.db (SQLite file)
    README.md (instructions to run your app)
video_presentation.mp4  (or link)
```

Your **README.md** must include:

* How to install dependencies
* How to run the Flask app
* Example API calls (curl/Postman)

---

# **4. Evaluation Rules**

* All code must be your own.
* Plagiarism or copying will result in zero points.
* If you do not submit the video presentation, the assignment will not be graded.
---

# **5. Optional Extensions (not graded)**

If you want to experiment:

* Simple HTML/JS frontend
* Additional regression models
* Visualization of expenses/income
* Authentication for the API

These are optional and do not affect your grade.


