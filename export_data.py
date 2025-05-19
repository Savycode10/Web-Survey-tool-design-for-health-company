import csv

from pymongo import MongoClient

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

client = MongoClient("mongodb://localhost:27017/")
db = client['survey_db']
collection = db['responses']

users = []
for doc in collection.find():
    user = User(doc['age'], doc['gender'], doc['income'], doc['expenses'])
    users.append(user)

with open('user_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Age', 'Gender', 'Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])

    for u in users:
        expenses = u.expenses
        writer.writerow([
            u.age, u.gender, u.income,
            expenses.get('utilities', 0),
            expenses.get('entertainment', 0),
            expenses.get('school_fees', 0),
            expenses.get('shopping', 0),
            expenses.get('healthcare', 0)
        ])
