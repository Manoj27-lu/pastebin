# Pastebin-Lite - Full Implementation

A complete Pastebin-like application with **Django REST API** backend and **React** frontend. Fully compliant with all assignment requirements.

## ✅ Features

- ✅ **Create pastes** with arbitrary text content
- ✅ **Shareable URLs** for each paste
- ✅ **Time-based expiry** (TTL/ttl_seconds)
- ✅ **View-count limits** (max_views)
- ✅ **Health check** endpoint (`GET /api/healthz`)
- ✅ **Persistent storage** (SQLite → PostgreSQL-ready)
- ✅ **Deterministic time** for testing (`x-test-now-ms` header)
- ✅ **XSS-safe** HTML rendering
- ✅ **CORS enabled** for cross-origin requests
- ✅ **Stateless design** (serverless-compatible)

## 🏗️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Django 5.2.10 + DRF |
| Frontend | React 19.2.4 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| HTTP | Fetch API + CORS |
| Styling | PrismJS (syntax highlighting) |
| Icons | React Icons |

## Project Structure

```
pastebin/
├── bakendpastebin/              # Django project
│   ├── manage.py
│   ├── db.sqlite3              # Database (auto-created)
│   ├── requirements.txt
│   ├── bakendpastebin/
│   │   ├── settings.py         # Django configuration
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── pastes/                 # Main app
│       ├── models.py           # Paste model with UUID, TTL, views
│       ├── views.py            # API and HTML views
│       ├── urls.py
│       ├── apps.py
│       ├── migrations/
│       └── templates/
│           └── paste.html
│
├── pastebin/                    # React frontend
│   ├── package.json
│   ├── .env                    # API URL config
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── App.css
│   │   ├── api.js              # Django API client
│   │   └── index.js
│   └── public/
│
├── README.md                   # This file
└── QUICKSTART.md              # Quick reference
```

## Persistence Layer

**SQLite Database** (`db.sqlite3`)
- Simple, file-based relational database
- Perfect for this assignment
- No external services required
- Survives across server restarts and deployments
- Table: `pastes_paste` with:
  - `id`: UUID primary key
  - `content`: TextField for paste content
  - `created_at`: Auto-set timestamp
  - `expires_at`: Optional expiration time
  - `max_views`: Optional view limit
  - `views`: Current view counter

## Running Locally

### Prerequisites
- Python 3.11+ (with venv)
- Node.js 18+
- SQLite (built-in)

### Backend Setup (Terminal 1)

```bash
cd bakendpastebin

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (creates db.sqlite3)
python manage.py migrate

# Start Django server
python manage.py runserver
# Backend: http://localhost:8000
```

### Frontend Setup (Terminal 2)

```bash
cd pastebin

# Install dependencies
npm install

# Start React dev server
npm start
# Frontend: http://localhost:3000
```

**Both servers must be running for the app to work.**
cd pastebin

# Install dependencies
npm install

# Start React dev server (runs on port 3000)
npm start
```

Then visit **http://localhost:3000** in your browser.

## API Documentation

### Health Check
```
GET /api/healthz
```
Returns: `{"ok": true}`

### Create Paste
```
POST /api/pastes
Content-Type: application/json

{
  "content": "Hello World",
  "ttl_seconds": 3600,      // Optional
  "max_views": 10           // Optional
}
```

Response (201):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "url": "http://localhost:8000/p/550e8400-e29b-41d4-a716-446655440000"
}
```

### Fetch Paste (API)
```
GET /api/pastes/:id
```

Response (200):
```json
{
  "content": "Hello World",
  "remaining_views": 9,
  "expires_at": "2026-01-28T18:31:52.000Z"
}
```

Returns 404 if paste:
- Does not exist
- Has expired (TTL exceeded)
- View limit reached

### View Paste (HTML)
```
GET /p/:id
```

Returns HTML page containing the paste content (rendered safely, no script execution).

## Deterministic Time for Testing

For automated testing with controlled time:

```bash
# Enable TEST_MODE
export TEST_MODE=1

# Then send requests with x-test-now-ms header
curl -H "x-test-now-ms: 1704067200000" http://localhost:8000/api/pastes/<id>
```

The application will treat the provided timestamp as "now" for TTL calculations.

## Environment Variables

```bash
# Django
DEBUG=True                                  # Set to False in production
SECRET_KEY=your-secret-key-here           # Change in production
ALLOWED_HOSTS=localhost,127.0.0.1         # Comma-separated

# Testing
TEST_MODE=0                                 # Set to 1 to enable deterministic time

# React
REACT_APP_API_URL=http://localhost:8000   # Backend URL
```

## Design Decisions

1. **SQLite for Persistence**: Lightweight, file-based, no external dependencies. Perfect for this assignment and easy to deploy.

2. **UUID for Paste IDs**: Globally unique, difficult to guess, collision-proof.

3. **Automatic View Counting**: Every successful fetch (both API and HTML) increments the view counter, providing consistent behavior.

4. **XSS Protection**: Paste content is rendered with Django's `{{ content|escape }}` filter to prevent script execution.

5. **CORS Enabled**: Allows React frontend on port 3000 to communicate with Django backend on port 8000.

6. **Deterministic Time**: TEST_MODE + x-test-now-ms header allows automated tests to control expiry behavior.

7. **Environment-based Config**: All sensitive/deployment-specific settings use environment variables, no hardcoded values.

## Example Usage

### Via UI
1. Open http://localhost:3000
2. Enter your paste content
3. Click "Create Paste"
4. Get redirected to the Django HTML view with your shareable URL

### Via curl
```bash
# Create a paste
curl -X POST http://localhost:8000/api/pastes \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello from curl!",
    "ttl_seconds": 3600,
    "max_views": 5
  }'

# Fetch the paste (JSON)
curl http://localhost:8000/api/pastes/550e8400-e29b-41d4-a716-446655440000

# View as HTML
curl http://localhost:8000/p/550e8400-e29b-41d4-a716-446655440000
```

## Code Quality

- ✅ No hardcoded localhost URLs (uses env vars)
- ✅ No credentials in code (uses env vars)
- ✅ No global mutable state
- ✅ Clean separation of concerns (backend/frontend)
- ✅ Proper error handling
- ✅ Type-safe database operations

## Deployment Notes

For deployment on Vercel or similar platforms:

1. **Backend**: Deploy Django app to a traditional host (Heroku, Railway, render.com) or serverless (AWS Lambda, Google Cloud Functions)
2. **Database**: SQLite works fine; file persists in the deployment environment
3. **Frontend**: Deploy React app to Vercel with `REACT_APP_API_URL` set to your backend URL
4. **Environment**: Set `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` in production

## License

MIT
