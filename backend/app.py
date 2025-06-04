import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

app = Flask(__name__)
import json

app.secret_key = os.environ.get('SECRET_KEY', 'a_default_fallback_key_if_not_set')
login_manager = LoginManager()
login_manager.init_app(app)

# Load users from users.json
USERS = {}
try:
    with open(os.path.join(os.path.dirname(__file__), 'users.json'), 'r') as f:
        USERS = json.load(f)
except FileNotFoundError:
    print("WARNING: users.json not found. No users will be loaded.")
except json.JSONDecodeError:
    print("WARNING: users.json is not valid JSON. No users will be loaded.")

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None

@app.route('/')
def index():
    # This would normally fetch news from an API
    # Placeholder news data. Replace this with a real news fetching mechanism.
    news_list = [
        {'title': 'Placeholder News Title 1', 'content': 'This is sample news content. Integrate a real news API here.'},
        {'title': 'Placeholder News Title 2', 'content': 'Another piece of sample news. This should be dynamically fetched.'},
    ]
    return render_template('index.html', news_list=news_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Placeholder endpoint to demonstrate translation
@app.route('/translate')
def translate():
    target = request.args.get('lang', 'en')
    text = request.args.get('text', '')
    # Placeholder translation logic. Replace this with a real translation service integration.
    translated_text = f"[Placeholder: Simulated translation of '{text}' to '{target}'. Integrate a real translation service here.]"
    return {'translated': translated_text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
