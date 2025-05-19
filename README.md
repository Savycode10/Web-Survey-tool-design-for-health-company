# Web Survey Tool for Healthcare Industry

## 📌 Project Overview

This project is a **Flask-based web application** developed as part of a final assignment for a data analysis company in Washington, DC. The goal is to collect participant data and analyze their **income spending patterns** in preparation for a **new healthcare product launch**.

---

## 🛠️ Features

### ✅ Web Development with Flask

* A simple and interactive web interface to collect user input.
* Collects basic details: **Age**, **Gender**, **Total Income**, and **Expenses**.

### ✅ Data Storage with MongoDB

* Stores user-submitted data in **MongoDB Atlas**.
* Expense categories are captured using checkboxes with text fields:

  * Utilities
  * Entertainment
  * School Fees
  * Shopping
  * Healthcare

### ✅ Data Processing with Python

* Implements a `User` class to encapsulate user data.
* Collected records are written to a CSV file for analysis.
* CSV is loaded and processed in a **Jupyter Notebook** for visualization.

### ✅ Data Visualization

Using data from the CSV, we created:

* A bar chart showing **ages with the highest income**.
* A grouped chart showing **gender distribution across spending categories**.
* Visualizations are exported as image files for use in **PowerPoint presentations**.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Savycode10/Web-Survey-tool-design-for-health-company.git
cd Web-Survey-tool-design-for-health-company
```

### 2. Set Up the Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

* Create a **MongoDB Atlas** account.
* Set up a **free-tier cluster**.
* Create a **database** and **collection** (e.g., `survey_db` and `responses`).
* Whitelist your IP address and get the **MongoDB connection URI**.
* Replace the URI in your Flask app (`app.py`) with the one from your MongoDB dashboard.

### 5. Run the App Locally

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

---

## 🌍 Deployment

This project is deployable on [**Render**](https://render.com):

1. Create a `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

2. Create a `Procfile` with the following line:

   ```
   web: gunicorn app:app
   ```

3. Push your project to GitHub.

4. On Render:

   * Create a new **Web Service**.
   * Connect it to your GitHub repo.
   * Use `main` as the branch.
   * Build and deploy.

---

## 📊 Jupyter Notebook Visualizations

After data is collected:

* Open `analysis.ipynb` or any notebook created.
* Load the CSV file.
* Perform analysis and generate plots.
* Export visualizations as `.png` or `.jpeg` for use in presentations.

---

## 📁 Project Structure

```
🔹 app.py                # Main Flask app
🔹 templates/            # HTML templates
🔹 static/               # Static assets (CSS, JS)
🔹 data.csv              # User data (generated)
🔹 analysis.ipynb        # Jupyter notebook for analysis
🔹 requirements.txt      # Python dependencies
🔹 Procfile              # For deployment (Render)
🔹 README.md             # Project documentation
```

---

## 👨‍💻 Author

**Dan Saviour** — R & Python Developer
📍 Lagos, Nigeria
GitHub: [@Savycode10](https://github.com/Savycode10)
LinkedIn: [Saviour Dan](https://linkedin.com/in/saviour-dan)

---

## 📄 License

This project is for educational purposes and not intended for commercial use without permission.
