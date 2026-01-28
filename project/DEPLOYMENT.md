# Deployment Guide

This guide explains how to deploy the Pastebin-Lite application.

## Deployment Strategy

Recommended approach:
- **Frontend**: Deploy React app to Vercel (free tier available)
- **Backend**: Deploy Django app to Railway, Render, or Heroku
- **Database**: Use the persistent SQLite file or upgrade to PostgreSQL

## Vercel Deployment (React Frontend)

### Option 1: Deploy via Vercel CLI

```bash
cd pastebin
npm install -g vercel
vercel login
vercel
```

During deployment, set environment variable:
```
REACT_APP_API_URL=https://your-backend.vercel.app
```

### Option 2: Deploy via GitHub

1. Push your repo to GitHub
2. Go to vercel.com → Import Project
3. Select your GitHub repository
4. Set environment variables in Vercel dashboard
5. Deploy

## Backend Deployment (Railway.app - Recommended)

### Step 1: Prepare Backend

```bash
cd bakendpastebin
# Create Procfile for Railway
echo "web: gunicorn bakendpastebin.wsgi" > Procfile

# Update requirements.txt to include gunicorn
pip install gunicorn
pip freeze > requirements.txt
```

### Step 2: Deploy to Railway

1. Go to railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Set environment variables:
   ```
   SECRET_KEY=<generate-a-random-key>
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app,localhost
   ```
5. Railway will auto-detect Django and deploy

### Step 3: Update Frontend

In Vercel dashboard, set:
```
REACT_APP_API_URL=https://your-app.railway.app
```

## Environment Variables for Production

Set these in your deployment platform's settings:

```
SECRET_KEY=<strong-random-key>
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
TEST_MODE=0
```

Generate a strong SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Database Migration in Production

If deploying to a fresh environment, run:

```bash
# Via Railway CLI or your platform's shell
python manage.py migrate
```

SQLite database will be automatically created and persisted.

## Custom Domain Setup

### Vercel
1. Go to Project Settings → Domains
2. Add your custom domain
3. Update DNS records per Vercel's instructions

### Railway
1. Go to Project Settings → Domains
2. Add custom domain
3. Update DNS CNAME record

## Monitoring

- Check Railway/Render logs for errors
- Vercel provides built-in analytics
- Monitor API responses with curl or Postman

## Scaling Notes

For production traffic:
1. **SQLite Limitation**: Works fine for moderate traffic. For high traffic, consider PostgreSQL
2. **Database Upgrade**:
   ```python
   # Update settings.py DATABASES
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.environ.get('DATABASE_NAME'),
           'USER': os.environ.get('DATABASE_USER'),
           'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
           'HOST': os.environ.get('DATABASE_HOST'),
           'PORT': '5432',
       }
   }
   ```
3. Railway and Render both offer PostgreSQL add-ons

## Common Issues

### "Module not found" errors
- Ensure requirements.txt is up to date
- Run `pip install -r requirements.txt` locally first

### CORS errors
- Check ALLOWED_HOSTS in settings.py
- Verify REACT_APP_API_URL in frontend env vars
- Ensure backend CORS_ALLOW_ALL_ORIGINS is enabled

### Database not persisting
- SQLite files persist in Railway/Render
- If using in-memory, data will be lost on redeploy
- Verify db.sqlite3 is in .gitignore (file-based, not tracked)

### Static files not loading
- Run `python manage.py collectstatic`
- Configure STATIC_URL and STATIC_ROOT in production

## Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Generate unique `SECRET_KEY`
- [ ] Use `HTTPS_ONLY=True` in production
- [ ] Set strong database password if using PostgreSQL
- [ ] Configure `ALLOWED_HOSTS` to your domain only
- [ ] Enable CORS only for your domain (production)
- [ ] Use environment variables for all secrets
- [ ] Never commit `.env` files with real credentials
