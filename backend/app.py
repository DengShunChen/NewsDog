from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

app = Flask(__name__)
app.secret_key = 'change_this_secret'
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user store
USERS = {'admin': {'password': 'password'}}

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
    news_list = [
        {'title': 'Example News', 'content': 'News content here'},
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
    # Here you would integrate with a translation service
    translated_text = f"[translated {text} to {target}]"
    return {'translated': translated_text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
