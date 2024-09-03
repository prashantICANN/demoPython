from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session as login_session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key
app.config['SESSION_TYPE'] = 'filesystem'
login_session(app)

# Dummy user data for login
users = {"testuser": "password123"}

# Dummy data for the user table
user_data = [
    {"username": "john_test", "name": "John Doe", "age": 30, "salary": 50000, "department": "IT",
     "marital_status": "Single", "gender": "Male"},
    {"username": "jane_Test", "name": "Jane Smith", "age": 25, "salary": 60000, "department": "HR",
     "marital_status": "Married", "gender": "Female"},
    {"username": "alice_johnson", "name": "Alice Johnson", "age": 28, "salary": 55000, "department": "Marketing",
     "marital_status": "Single", "gender": "Female"},
    {"username": "bob_williams", "name": "Bob Williams", "age": 35, "salary": 70000, "department": "Finance",
     "marital_status": "Married", "gender": "Male"},
    {"username": "charlie_brown", "name": "Charlie Brown", "age": 40, "salary": 65000, "department": "Sales",
     "marital_status": "Single", "gender": "Male"},
    {"username": "diana_king", "name": "Diana King", "age": 27, "salary": 62000, "department": "HR",
     "marital_status": "Single", "gender": "Female"},
    # Add 14 more users similarly...
]


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return "Invalid credentials! Try again with correct credential.", 401


@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    search_query = request.form.get('search') if request.method == 'POST' else ''

    # Filter user data based on the search query (username)
    filtered_users = [user for user in user_data if search_query.lower() in user['username'].lower()]

    return render_template('home.html', users=filtered_users, search_query=search_query)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
