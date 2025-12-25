# Robo Shop Deployment Guide

This guide covers deploying the Robo Shop e-commerce platform to production.

## Prerequisites

- Git repository initialized and pushed to GitHub
- Python 3.11+
- All dependencies in requirements.txt

## Deployment Options

### Option 1: Railway (Recommended - Free tier with custom domains)

**Steps:**

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "Create New Project" → "Deploy from GitHub"
   - Select your robo_shop repository
   - Railway auto-detects Procfile and requirements.txt

3. **Configure Environment Variables**
   - In Railway project settings, add:
     ```
     DEBUG=False
     SECRET_KEY=<generate-a-new-secret-key>
     ALLOWED_HOSTS=<your-railway-domain>.up.railway.app
     ```

4. **Database Setup**
   - Click "Add Plugin" → "PostgreSQL"
   - Railway auto-populates DATABASE_URL

5. **Static Files**
   - Railway runs `python manage.py collectstatic` automatically via Procfile

6. **Deploy**
   - Commit and push to GitHub - Railway auto-deploys
   - Check logs: Railway Dashboard → Deployments → Logs

7. **Custom Domain** (Premium)
   - Add domain in Railway settings

---

### Option 2: PythonAnywhere (Traditional hosting)

**Steps:**

1. **Create PythonAnywhere Account**
   - Sign up at [pythonanywhere.com](https://pythonanywhere.com)

2. **Upload Code**
   ```bash
   # Via bash console in PythonAnywhere
   git clone https://github.com/your-username/robo_shop.git
   cd robo_shop
   pip install -r requirements.txt --user
   ```

3. **Configure Web App**
   - Web tab → Add new web app
   - Select "Manual configuration" → Python 3.11
   - WSGI file: `/home/username/robo_shop/robo_shop/wsgi.py`

4. **Set Environment Variables**
   - Web tab → Environment variables:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key
     ALLOWED_HOSTS=yourusername.pythonanywhere.com
     ```

5. **Static & Media Files**
   - Web tab → Static files:
     - URL: `/static/` → Directory: `/home/username/robo_shop/staticfiles`
     - URL: `/media/` → Directory: `/home/username/robo_shop/media`

6. **Database**
   - Use PostgreSQL or MySQL addon (paid feature)
   - Or use SQLite for small projects

---

### Option 3: Render (Free tier)

**Steps:**

1. **Create Render Account**
   - Sign up at [render.com](https://render.com)

2. **New Web Service**
   - Dashboard → New → Web Service
   - Connect GitHub repository

3. **Configure**
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command: Already in Procfile
   - Environment variables:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key
     ALLOWED_HOSTS=your-service.render.com
     ```

4. **Database**
   - Create PostgreSQL instance
   - Copy DATABASE_URL to web service env vars

---

## Local Development First

Before deploying, test locally:

```bash
# Create .env file locally
cp .env.example .env

# Set DEBUG=True for development
DEBUG=True
SECRET_KEY=test-secret-key-dev

# Run migrations
python manage.py migrate

# Test server
python manage.py runserver
```

## Production Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY changed (not the default)
- [ ] ALLOWED_HOSTS configured
- [ ] STATIC_ROOT and MEDIA_ROOT configured
- [ ] Database backend chosen (PostgreSQL recommended for production)
- [ ] Static files collected: `python manage.py collectstatic --noinput`
- [ ] Migrations applied: `python manage.py migrate`
- [ ] Email backend configured (if needed)
- [ ] HTTPS enabled (automatic on most platforms)
- [ ] Admin user created: `python manage.py createsuperuser`

## Important Files for Deployment

- **Procfile** - Process types for platform
- **runtime.txt** - Python version specification
- **requirements.txt** - All dependencies
- **.env** - Environment variables (NOT in Git, create on server)
- **staticfiles/** - Collected static files (auto-generated)

## Common Issues

### Static Files Not Showing
```bash
# Collect static files
python manage.py collectstatic --noinput
```

### Database Errors
- Ensure DATABASE_URL is set in environment
- Run migrations: `python manage.py migrate`

### Media Files Not Uploading
- Check MEDIA_ROOT directory has write permissions
- Verify MEDIA_URL in settings.py

### 500 Errors
- Check server logs via platform dashboard
- Verify DEBUG=False isn't revealing errors (check error logs)
- Ensure all environment variables are set

## Recommended Setup Summary

**Best for Robo Shop:**
- Platform: Railway (easiest free option)
- Database: PostgreSQL
- Static/Media: Handled by WhiteNoise
- Domain: Railway custom domain ($5/month)

After deployment, visit your domain and test:
1. Signup as seller
2. Add a product with image
3. Signup as buyer
4. Add product to cart
5. Complete checkout

## Support

For platform-specific issues:
- Railway: [docs.railway.app](https://docs.railway.app)
- PythonAnywhere: [help.pythonanywhere.com](https://help.pythonanywhere.com)
- Render: [render.com/docs](https://render.com/docs)
