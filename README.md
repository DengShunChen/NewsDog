# NewsDog

A simple Flask-based news collector with a magical newspaper-style UI. This project demonstrates a basic setup for collecting news, translating content, tracking popular articles, and managing user logins. Everything runs with Docker Compose.

## Features
- Fetch and display news articles
- Translate content to a selected language
- Basic user login/logout with `Flask-Login`
- Placeholder for Gemini AI integration
- Tracks article views to highlight popular news

## Running
Make sure you have Docker and Docker Compose installed.

```bash
docker compose up --build
```

The app will be available at `http://localhost:5000`.

## Configuration

### Secret Key
The application uses a `SECRET_KEY` for session management and other security-related features. This key is loaded from an environment variable.

**For Development:**
- The `docker-compose.yml` file sets a default `SECRET_KEY` for development purposes. You can modify it there:
  ```yaml
  services:
    web:
      # ...
      environment:
        SECRET_KEY: 'your_new_development_secret_key_here'
  ```
- Alternatively, you can set this variable in your shell environment if you modify `docker-compose.yml` to use environment variable substitution (e.g., `SECRET_KEY: ${SECRET_KEY_FROM_HOST}`).

**For Production:**
- **It is crucial to use a strong, unique secret key for production.** Do not use the default development key.
- Set the `SECRET_KEY` environment variable in your production environment. The method for doing this will depend on your deployment platform (e.g., Docker Swarm secrets, Kubernetes secrets, platform-specific environment variable settings). A strong key can be generated using Python:
  ```python
  import secrets
  secrets.token_hex(32)
  ```

### User Data
User authentication data is loaded from `backend/users.json`. This file contains a simple JSON object mapping usernames to their password information.

**Example `backend/users.json`:**
```json
{
  "admin": {
    "password": "password"
  }
}
```

**Important Security Note:**
The `backend/users.json` file is included in the project's `.gitignore` file. This is a security measure to prevent accidental commitment of user credentials to the version control system. Even though it currently contains dummy data, in a real-world scenario, this file would hold sensitive information.
- For development, you can manually create and manage this file.
- For production, you should ensure this file is properly secured and managed outside of the repository, or consider using a more robust user management system (e.g., a database with hashed passwords).
