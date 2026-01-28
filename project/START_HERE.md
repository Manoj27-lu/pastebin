# ✅ PASTEBIN-LITE - READY FOR SUBMISSION

## Status: COMPLETE ✓

All requirements from the take-home assignment have been implemented and verified.

## What You Have

### ✅ Fully Functional Application
- **Backend**: Django REST API running on `http://localhost:8000`
- **Frontend**: React SPA running on `http://localhost:3000`
- **Database**: SQLite (persistent, file-based)
- **All Routes**: `/api/healthz`, `/api/pastes` (POST), `/api/pastes/:id` (GET), `/p/:id` (GET)

### ✅ Complete Documentation
1. **README.md** - Full project documentation
2. **DEPLOYMENT.md** - Step-by-step deployment guide
3. **SUBMISSION.md** - Assignment compliance checklist
4. **.env.example** - Environment variable template
5. **Procfile** - Production deployment config
6. **runtime.txt** - Python version specification

### ✅ Code Quality
- No hardcoded localhost URLs
- No secrets in code (all env vars)
- No global mutable state
- XSS protection
- Proper CORS configuration
- Clean separation of concerns

## Quick Start (Local Development)

### Terminal 1 - Backend
```bash
cd bakendpastebin
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Runs on http://localhost:8000
```

### Terminal 2 - Frontend
```bash
cd pastebin
npm install
npm start
# Runs on http://localhost:3000
```

Then visit **http://localhost:3000** and start creating pastes!

## API Testing

### Health Check
```bash
curl http://localhost:8000/api/healthz
# {"ok": true}
```

### Create a Paste
```bash
curl -X POST http://localhost:8000/api/pastes \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello World",
    "ttl_seconds": 3600,
    "max_views": 10
  }'

# Returns: {"id": "uuid", "url": "http://localhost:8000/p/uuid"}
```

### Fetch Paste (API)
```bash
curl http://localhost:8000/api/pastes/<id>
# {"content": "Hello World", "remaining_views": 9, "expires_at": "..."}
```

### View Paste (HTML)
```bash
curl http://localhost:8000/p/<id>
# Returns HTML with the paste content
```

## Key Features Verified

✓ Create paste with content
✓ Get shareable URL
✓ View paste via URL
✓ Optional TTL (time-to-live)
✓ Optional max views limit
✓ Both constraints together
✓ Health check endpoint
✓ Persistent storage (SQLite)
✓ Deterministic time for testing
✓ XSS safe rendering
✓ Proper error handling (4xx responses)
✓ View counting
✓ CORS enabled

## Deployment Ready

The application is ready for production deployment on:

### Frontend
- **Vercel** (Recommended)
- Netlify
- GitHub Pages

### Backend
- **Railway.app** (Recommended)
- Heroku
- Render
- AWS/GCP

See **DEPLOYMENT.md** for detailed instructions.

## File Structure

```
pastebin/
├── README.md                  ← START HERE
├── DEPLOYMENT.md             ← How to deploy
├── SUBMISSION.md             ← Assignment checklist
├── .env.example             ← Config template
├── .gitignore               ← Git config
│
├── bakendpastebin/          ← Django Backend
│   ├── Procfile             ← Deployment config
│   ├── runtime.txt          ← Python version
│   ├── requirements.txt      ← Dependencies
│   ├── manage.py
│   ├── db.sqlite3           ← Database
│   ├── bakendpastebin/
│   │   └── settings.py      ← Configuration
│   └── pastes/
│       ├── models.py        ← Paste model
│       ├── views.py         ← API endpoints
│       ├── urls.py
│       └── templates/
│           └── paste.html   ← HTML template
│
└── pastebin/                ← React Frontend
    ├── package.json
    ├── .env                 ← API URL
    ├── src/
    │   ├── App.js           ← Main component
    │   ├── api.js           ← API client
    │   ├── App.css
    │   └── index.js
    └── public/
```

## Persistence Layer

**SQLite Database** (`db.sqlite3`)

- File-based relational database
- Automatically created on first migration
- Persists across server restarts
- Survives deployments (when using persistent storage)
- Table: `pastes_paste` with UUID, content, timestamps, counters
- No external services required
- Perfect for this assignment

## Environment Variables

```bash
# Frontend
REACT_APP_API_URL=http://localhost:8000

# Backend  
SECRET_KEY=your-secret-key              # Change in production
DEBUG=True                              # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1     # Update for production
TEST_MODE=0                             # Set to 1 for testing
```

## Testing Notes

### Standard Testing
```bash
# Everything works as-is
curl http://localhost:8000/api/healthz
```

### Deterministic Time Testing
```bash
export TEST_MODE=1

# Requests with x-test-now-ms use that timestamp
curl -H "x-test-now-ms: 1704067200000" \
  http://localhost:8000/api/pastes/<id>
```

## Code Quality Checklist

✓ No hardcoded absolute URLs (uses env vars)
✓ No secrets or credentials in code
✓ No global mutable state
✓ Server works across requests (stateless)
✓ Clean code, proper separation
✓ Error handling for all cases
✓ XSS protection
✓ CORS properly configured
✓ Documentation complete
✓ Production-ready

## Support for Automated Tests

The application supports all automated tests required by the assignment:

✓ Service checks (healthz, valid JSON, timeout)
✓ Paste creation (valid id, correct URL format)
✓ Paste retrieval (API & HTML)
✓ View limits (first fetch 200, second 404 for max_views=1)
✓ TTL (available before, 404 after via x-test-now-ms)
✓ Combined constraints (first trigger = unavailable)
✓ Error handling (4xx for invalid input)
✓ Robustness (no negative views, concurrent safe)

## What's Ready for Submission

1. **Deployed URL** - Ready to deploy on Vercel + Railway
2. **Git Repository** - Clean, no secrets, all source code included
3. **README.md** - Comprehensive with:
   - Project description
   - Local run instructions
   - Persistence layer (SQLite)
   - Design decisions

## Next Steps

### For Local Development
1. Run the backend and frontend servers
2. Open http://localhost:3000
3. Create pastes and test functionality

### For Deployment
1. Follow [DEPLOYMENT.md](DEPLOYMENT.md)
2. Set environment variables on your host
3. Deploy frontend to Vercel
4. Deploy backend to Railway
5. Update REACT_APP_API_URL with backend URL

### For Submission
1. Push code to GitHub (all changes committed)
2. Note your deployed URLs (Vercel + Railway)
3. Include this README and DEPLOYMENT.md
4. Submit links to: deployed URL, git repo

## Support

All files include comments explaining:
- API endpoints
- Database design
- Configuration options
- Deployment steps
- Security considerations

Review README.md, DEPLOYMENT.md, and code comments for detailed information.

---

**Status**: ✅ **READY FOR SUBMISSION**

The application is fully functional, properly documented, and ready for automated testing and evaluation.

Start developing locally or deploy to production using the guides provided.

Good luck! 🚀
