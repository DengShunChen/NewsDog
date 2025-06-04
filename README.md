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
