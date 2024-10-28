from flask import Flask, render_template, redirect, request, url_for
from config import db

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Logic for creating an account
        pass
    return render_template('create_account.html')

@app.route('/home')
def home():
    # Fetch devices from the database to display
    return render_template('home.html')

@app.route('/campus/<campus_name>')
def campus_page(campus_name):
    # Fetch devices by campus from the database
    return render_template('campus_page.html', campus=campus_name)

if __name__ == "__main__":
    app.run(debug=True)
