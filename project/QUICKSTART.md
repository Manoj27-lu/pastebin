# Quick Start Guide - Pastebin Django + React

## ✅ Setup Complete!

### Status:
- ✅ Django dependencies installed
- ✅ Database migrations applied
- ✅ Django backend running on port 8000
- ⏳ React frontend needs to be started

---

## Running the Application

### Terminal 1 - Django Backend (Already Running)
```
Django running at: http://127.0.0.1:8000
Health check: http://127.0.0.1:8000/api/healthz
Database: db.sqlite3 (SQLite)
```

### Terminal 2 - React Frontend
If you encounter PowerShell execution policy errors, use one of these approaches:

**Option A: Change PowerShell Execution Policy (Admin Terminal)**
```powershell
Set-ExecutionPolicy RemoteSigned -Force
```
Then run:
```powershell
cd d:\pastebin\pastebin
npm start
```

**Option B: Use CMD instead of PowerShell**
```cmd
cd d:\pastebin\pastebin
npm start
```

**Option C: Use bash (Git Bash or similar)**
```bash
cd /d/pastebin/pastebin
npm start
```

Once React starts, it will open at: `http://localhost:3000`

---

## What Works Now

### ✅ Django Backend
- Health check: `GET /api/healthz` → `{"ok": true}`
- Create paste: `POST /api/pastes` → Saves to SQLite
- Fetch paste: `GET /api/pastes/<id>` → Retrieves from SQLite
- View HTML: `GET /p/<id>` → Renders HTML view

### ✅ React Frontend
Once started on port 3000:
- **Create Tab**: Create new pastes with TTL and max views
- **Fetch Tab**: Retrieve pastes by UUID
- Backend status indicator shows connection health

---

## Testing

### Test 1: Health Check
```bash
curl http://localhost:8000/api/healthz
# Should return: {"ok": true}
```

### Test 2: Create Paste (React → Django Redirect)
1. Open http://localhost:3000
2. Enter content in the textarea
3. Click "Create Paste"
4. Should redirect to Django HTML page: `http://localhost:8000/p/<uuid>`

### Test 3: Fetch Paste (JSON API)
```bash
curl http://localhost:8000/api/pastes/YOUR_PASTE_ID
# Returns: {"content": "...", "remaining_views": 9, "expires_at": "..."}
```

### Test 4: View HTML
Visit `http://localhost:8000/p/YOUR_PASTE_ID` directly in browser

---

## Database Options

### Current: SQLite (db.sqlite3)
- ✅ Works out of the box
- ✅ No external database needed
- ✅ Perfect for development
- ⚠️ Single-user/file-based

### Optional: Switch to MySQL
1. Start MySQL server
2. Create database: `CREATE DATABASE pastebin_db;`
3. Update `bakendpastebin/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pastebin_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
4. Run migrations again:
```bash
python manage.py migrate
```

---

## File Locations

```
d:\pastebin\
├── bakendpastebin/          # Django project
│   ├── manage.py
│   ├── requirements.txt      # ✅ Installed
│   ├── db.sqlite3           # ✅ Created (database)
│   ├── bakendpastebin/
│   │   └── settings.py      # ✅ Configured
│   └── pastes/              # ✅ Created
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── migrations/      # ✅ Applied
│
├── pastebin/                # React project
│   ├── package.json
│   ├── .env                 # ✅ Configured
│   ├── src/
│   │   ├── api.js           # ✅ Created
│   │   ├── App.js           # ✅ Updated
│   │   └── App.css
│   └── public/
│
└── INTEGRATION_GUIDE.md     # Full documentation
```

---

## Troubleshooting

### Django not responding to requests?
- Check if server is running: `http://localhost:8000/admin`
- Look for errors in terminal where Django is running
- Verify SQLite database was created: `db.sqlite3` file should exist

### React showing "Backend: ✗ Disconnected"?
- Ensure Django is running on port 8000
- Check browser console for CORS errors
- Verify `REACT_APP_API_URL=http://localhost:8000` in `.env`

### npm: Permission denied or execution policy error?
- Use cmd.exe instead of PowerShell
- Or run: `Set-ExecutionPolicy RemoteSigned` (requires admin)
- Or use Git Bash if available

### Database error "table doesn't exist"?
- Run migrations: `python manage.py migrate`
- Check `db.sqlite3` file exists in bakendpastebin folder

---

## Next Steps

1. **Start Django** (Already done ✅)
   ```
   http://127.0.0.1:8000/
   ```

2. **Start React** (Do this next)
   ```
   cd d:\pastebin\pastebin
   npm start
   ```

3. **Use the App**
   - Open http://localhost:3000
   - Create a paste with content
   - Copy the ID
   - Fetch the paste using ID

---

## Environment Details

- **Python**: 3.11.2 (venv at `d:\pastebin\env`)
- **Django**: 5.2.10
- **React**: 19.2.4
- **Database**: SQLite (db.sqlite3) or MySQL (optional)
- **Node**: npm (required for React)

---

## Commands Reference

### Django
```bash
# Navigate to Django folder
cd d:\pastebin\bakendpastebin

# Run migrations
D:/pastebin/env/Scripts/python.exe manage.py migrate

# Start server
D:/pastebin/env/Scripts/python.exe manage.py runserver

# Create superuser
D:/pastebin/env/Scripts/python.exe manage.py createsuperuser

# Shell access
D:/pastebin/env/Scripts/python.exe manage.py shell
```

### React
```bash
# Navigate to React folder
cd d:\pastebin\pastebin

# Install dependencies
npm install

# Start dev server
npm start

# Build for production
npm run build
```

---

**✅ You're all set! Start React and enjoy your Pastebin app!**
