# PyStuff-ELTE

#  ELTE Python Course Work - [Kendi J]

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python 3.10](https://img.shields.io/badge/Python-3.10%2B-blue)

## 🗺️ Table of Contents
* [Course Overview](#course-overview)
* [Repository Structure](#-repository-structure)
* [Setup & Running the Code](#-setup--running-the-code)

---

## Course Overview


### Weeks 1–5: Foundations of Python

| Topic | Description |
| :--- | :--- |
| **Foundations** | Introduction, scalar/non-scalar data objects, flow control (branching, loops). |
| **Operators** | Numbering systems, bitwise operators. |
| **Abstraction** | Functions and parameter handling. |
| **Pythonic Expressions** | Data sequence comprehensions (list, set, dict), lambda functions. |
| **File Handling** | Reading/writing files, CSV/JSON management, directory operations. |
| **Package Management** | Installing, upgrading, and managing Python packages (pip). |
| **OOP** | Classes, objects, inheritance, and encapsulation. |
| **Error Handling** | Errors, exceptions, and error-handling patterns. |
| **Testing** | Unit tests (`unittest`, `pytest`), and debugging tools. |

### Weeks 6–12: Using Python in Various Domains

| Topic | Focus |
| :--- | :--- |
| **Automation & Scripting** | OS tasks, batch processing, and web scraping. |
| **Web Development – API Design** | Building and consuming APIs with frameworks like Flask or FastAPI. |
| **Databases** | Working with persistent storage using SQLite. |
| **Data Science** | Data manipulation (Pandas, NumPy) and visualization (Matplotlib, Seaborn). |
| **Machine Learning** | Basic concepts, model training and evaluation with scikit-learn. |

---

## Repository Structure

The files are organized to mirror the course progression, with dedicated folders for graded work.

| Folder | Content | Syllabus Weeks |
| :--- | :--- | :--- |
| `01-Foundations/` | Class exercises and notes on Core Python concepts (OOP, Files, Functions). | Weeks 1-5 |
| `02-Domains/` | Code for specific applications (Web Dev, Data Science, ML). | Weeks 6-12 |
| `Assignments/` | Dedicated folders for graded Programming Assignments 1 and 2. | Throughout Semester |
| `Exams/` | Practice problems and prep materials for the Midterm and End-term. | N/A |

---

## Setup & Running the Code

To run the Python code in this repository, it is highly recommended to use a **Virtual Environment** to manage dependencies specific to this course.

1. **Clone the Repository:**
    ```bash
    git clone [your-repo-url-here]
    cd Python-Course-Work
    ```

2. **Create and Activate Virtual Environment (venv):**
    ```bash
    # Create the environment (do this only once)
    python3 -m venv venv

    # Activate the environment (do this every time you start work)
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate  # On Windows PowerShell
    ```

3. **Install Dependencies (when needed):**
    If a project requires special packages (like `pandas` or `flask`), install them using the `requirements.txt` file found in the repository root.
    ```bash
    pip install -r requirements.txt
    ```

4. **Run a File:**
    ```bash
    python3 01-Foundations/01-Basics-Types/variables.py
    ```
---

### Next Step

Now that you have your repository structure and a professional `README.md` set up, let's create your first Python file inside the **`01-Foundations/01-Basics-Types/`** folder.

Would you like to start with a script on **variables and basic data types**?