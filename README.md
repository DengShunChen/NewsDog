# NewsDog

A simple Flask-based news collector with a magical newspaper-style UI. This project demonstrates a basic setup for collecting news, translating content, tracking popular articles, and managing user logins. Everything runs with Docker Compose.

## Features

-   **News Fetching**: Fetches and displays news articles (currently uses placeholder data).
-   **Content Translation**: Translates article content to a selected language (currently a placeholder).
-   **User Authentication**: Basic user login/logout with `Flask-Login`.
-   **Gemini AI Integration**: Placeholder for future Gemini AI features.
-   **Popularity Tracking**: Tracks article views to highlight popular news.

## Project Structure

```
.
├── backend
│   ├── static
│   │   └── styles.css
│   ├── templates
│   │   ├── index.html
│   │   └── login.html
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── .gitignore
├── README.md
└── docker-compose.yml
```

-   **`backend/`**: Contains all the backend Flask application code.
    -   **`static/`**: Holds static files like CSS, JavaScript, and images.
    -   **`templates/`**: Contains Jinja2 templates for rendering HTML pages.
    -   **`Dockerfile`**: Defines the Docker image for the Flask application.
    -   **`app.py`**: The main entry point of the application, containing all routes and core logic.
    -   **`requirements.txt`**: Lists the Python dependencies.
-   **`docker-compose.yml`**: Defines and configures the multi-container Docker application.

## Running the Project

Make sure you have Docker and Docker Compose installed.

1.  **Build and Start the Containers**:

    ```bash
    docker compose up --build
    ```

2.  **Access the Application**:

    The app will be available at `http://localhost:5000`.

## Configuration

### Secret Key

The application uses a `SECRET_KEY` for session management and other security-related features. This key is loaded from an environment variable.

**For Development:**

-   The `docker-compose.yml` file sets a default `SECRET_KEY` for development purposes. You can modify it there:
    ```yaml
    services:
      web:
        # ...
        environment:
          SECRET_KEY: 'your_new_development_secret_key_here'
    ```

**For Production:**

-   **It is crucial to use a strong, unique secret key for production.** Do not use the default development key.
-   Set the `SECRET_KEY` environment variable in your production environment. A strong key can be generated using Python:
    ```python
    import secrets
    secrets.token_hex(32)
    ```

### User Data

User authentication data is loaded from `backend/users.json`.

**Example `backend/users.json`:**

```json
{
  "admin": {
    "password": "password"
  }
}
```

**Important Security Note:**
The `backend/users.json` file is included in the project's `.gitignore` to prevent accidental commitment of user credentials.

## Contributing

Contributions are welcome. Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.
