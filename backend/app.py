import os
import json
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a_default_fallback_key_if_not_set')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# In-memory store for view counts
view_counts = {}

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
    """Represents a user in the system.

    This class is used by Flask-Login to manage user sessions. It provides
    the necessary properties and methods required by the extension.

    Attributes:
        id (str): The unique identifier for the user, which is their username.
    """
    def __init__(self, username):
        """Initializes a new User instance.

        Args:
            username (str): The username of the user.
        """
        self.id = username


@login_manager.user_loader
def load_user(user_id):
    """Loads a user object from the user ID.

    This function is required by Flask-Login. It's used to reload the user
    object from the user ID stored in the session.

    Args:
        user_id (str): The ID of the user to load.

    Returns:
        User: The user object if found, otherwise None.
    """
    if user_id in USERS:
        return User(user_id)
    return None


@app.route('/')
def index():
    """Renders the main page with a list of news articles.

    This view fetches news from the SauravKanchan/NewsAPI and displays them.

    Returns:
        str: The rendered HTML of the main page.
    """
    news_api_url = "https://saurav.tech/NewsAPI/top-headlines/category/general/in.json"
    try:
        response = requests.get(news_api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        news_data = response.json()
        news_list = news_data.get('articles', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        news_list = []
        flash('Could not fetch news articles. Please try again later.', 'error')


    # Add view counts to each article
    for article in news_list:
        article['views'] = view_counts.get(article['url'], 0)
        article['encoded_url'] = quote(article['url'], safe='')


    return render_template('index.html', news_list=news_list)


@app.route('/view/<path:article_url>')
def view_article(article_url):
    """Tracks a view for an article and redirects to the article's URL.

    Args:
        article_url (str): The URL of the article to view.

    Returns:
        werkzeug.wrappers.response.Response: A redirect to the article's URL.
    """
    # Increment the view count for the article
    view_counts[article_url] = view_counts.get(article_url, 0) + 1
    return redirect(article_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login.

    On a GET request, it displays the login form. On a POST request,
    it validates the user's credentials and, if successful, logs them in
    and redirects to the main page.

    Returns:
        str or werkzeug.wrappers.response.Response: The rendered login page
        or a redirect to the main page upon successful login.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """Logs the current user out.

    Requires the user to be logged in. After logging out, it redirects
    the user to the main page.

    Returns:
        werkzeug.wrappers.response.Response: A redirect to the main page.
    """
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


# Placeholder endpoint to demonstrate translation
@app.route('/translate')
def translate():
    """A placeholder endpoint for text translation.

    This endpoint simulates a translation service. It takes text and a target
    language as query parameters and returns a placeholder translation.

    Returns:
        dict: A dictionary containing the placeholder translated text.
    """
    target = request.args.get('lang', 'en')
    text = request.args.get('text', '')
    # Placeholder translation logic. Replace this with a real translation service integration.
    translated_text = f"[Placeholder: Simulated translation of '{text}' to '{target}'. Integrate a real translation service here.]"
    return {'translated': translated_text}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
