from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client['survey_db']
collection = db['responses']

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = {
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "income": float(request.form['income']),
            "expenses": {
                category: float(request.form.get(category, 0))
                for category in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
                if request.form.get(category)
            }
        }
        collection.insert_one(data)
        return redirect('/thankyou')
    return render_template('form.html')

@app.route('/thankyou')
def thank_you():
    return "<h2>Thank you for submitting your data!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
