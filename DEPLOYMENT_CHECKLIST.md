# ✅ DEPLOYMENT CHECKLIST

Print this and check off items as you prepare to deploy Robo Shop.

---

## 📋 PRE-DEPLOYMENT (Local)

### Code Quality
- [ ] All code committed to Git
- [ ] No uncommitted changes
- [ ] `.env` file created (NOT committed)
- [ ] `.gitignore` includes sensitive files
- [ ] No hardcoded secrets in code

### Django Configuration
- [ ] Run `python check_deployment.py`
- [ ] Run `python manage.py check --deploy`
- [ ] DEBUG = False in .env
- [ ] SECRET_KEY is strong (not default)
- [ ] ALLOWED_HOSTS contains your domain(s)
- [ ] INSTALLED_APPS includes all your apps

### Database
- [ ] Run `python manage.py makemigrations`
- [ ] Run `python manage.py migrate`
- [ ] All migrations applied successfully
- [ ] Test database operations work

### Static & Media Files
- [ ] Run `python manage.py collectstatic --noinput`
- [ ] staticfiles/ directory created
- [ ] STATIC_ROOT configured correctly
- [ ] MEDIA_ROOT configured correctly
- [ ] Static files load locally

### Testing
- [ ] Test signup as seller
- [ ] Test signup as buyer
- [ ] Test product creation with image
- [ ] Test add to cart functionality
- [ ] Test checkout process
- [ ] Test admin panel access
- [ ] No console errors in browser

### Dependencies
- [ ] requirements.txt is up-to-date
- [ ] All dependencies in requirements.txt
- [ ] Gunicorn (21.2.0 or higher) in requirements.txt
- [ ] WhiteNoise (6.6.0 or higher) in requirements.txt
- [ ] python-decouple in requirements.txt

### Security
- [ ] SECURE_SSL_REDIRECT enabled
- [ ] SESSION_COOKIE_SECURE enabled
- [ ] CSRF_COOKIE_SECURE enabled
- [ ] SECURE_BROWSER_XSS_FILTER enabled
- [ ] No sensitive data in templates
- [ ] Password hashing working

---

## 📦 DEPLOYMENT FILES

### Required Files
- [ ] Procfile exists
- [ ] runtime.txt exists (Python 3.11.0)
- [ ] requirements.txt up-to-date
- [ ] .env.example created
- [ ] .gitignore properly configured

### Documentation
- [ ] README.md complete
- [ ] DEPLOYMENT.md created
- [ ] HOSTING_SETUP.md created
- [ ] COMMANDS_REFERENCE.md created
- [ ] GETTING_STARTED.md created

---

## 🌐 CHOOSE HOSTING PLATFORM

### Option A: Railway.app ⭐
- [ ] Create railway.app account
- [ ] Connect GitHub repository
- [ ] Set environment variables:
  - [ ] DEBUG=False
  - [ ] SECRET_KEY=<secure-key>
  - [ ] ALLOWED_HOSTS=<your-domain>
- [ ] Add PostgreSQL plugin
- [ ] Click Deploy
- [ ] Monitor first deployment

### Option B: PythonAnywhere
- [ ] Create pythonanywhere.com account
- [ ] Upload code (Git or ZIP)
- [ ] Create Web App (Manual Config)
- [ ] Configure WSGI file
- [ ] Set environment variables
- [ ] Configure static files
- [ ] Configure media files
- [ ] Reload web app

### Option C: Render.com
- [ ] Create render.com account
- [ ] Connect GitHub repository
- [ ] Set build command
- [ ] Set environment variables
- [ ] Create PostgreSQL instance
- [ ] Set DATABASE_URL variable
- [ ] Deploy
- [ ] Monitor deployment

---

## 📋 ENVIRONMENT VARIABLES

Set these on your hosting platform:

### Required
- [ ] DEBUG=False
- [ ] SECRET_KEY=<generate-new-key>
- [ ] ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

### Optional (if using external database)
- [ ] DATABASE_URL=postgresql://...

### Optional (if sending emails)
- [ ] EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
- [ ] EMAIL_HOST=smtp.gmail.com
- [ ] EMAIL_PORT=587
- [ ] EMAIL_HOST_USER=your-email@gmail.com
- [ ] EMAIL_HOST_PASSWORD=app-password

---

## 🗄️ DATABASE SETUP

### SQLite (Default, Small Projects)
- [ ] db.sqlite3 exists locally
- [ ] Database migrated successfully
- [ ] Keep backups of db.sqlite3

### PostgreSQL (Recommended for Production)
- [ ] PostgreSQL created on platform
- [ ] DATABASE_URL variable set
- [ ] Migrations run on platform
- [ ] Superuser created on platform

---

## 👤 ADMIN SETUP

- [ ] Superuser created on local database
- [ ] Superuser created on production database
- [ ] Admin can login at /admin/
- [ ] Admin panel functional

---

## 🧪 POST-DEPLOYMENT TESTING

### Functionality
- [ ] Site loads without errors
- [ ] Static files (CSS, JS) load correctly
- [ ] Images display properly
- [ ] Signup works
- [ ] Login works
- [ ] Logout works
- [ ] Product creation works (Seller)
- [ ] Product list displays (Buyer)
- [ ] Cart functionality works
- [ ] Checkout works
- [ ] Admin panel accessible

### Security
- [ ] HTTPS enforced (green lock)
- [ ] No sensitive data in HTML source
- [ ] LOGIN_URL redirects correctly
- [ ] CSRF tokens present in forms

### Performance
- [ ] Pages load reasonably fast
- [ ] No 500 errors
- [ ] Images lazy-load
- [ ] Responsive design works

---

## 📊 MONITORING

### First Week
- [ ] Check logs daily for errors
- [ ] Monitor database size
- [ ] Check media folder growth
- [ ] Monitor server resources

### Ongoing
- [ ] Set up automatic backups
- [ ] Monitor error logs weekly
- [ ] Check dependency updates monthly
- [ ] Review user feedback

---

## 🔄 MAINTENANCE

### Weekly
- [ ] Check for deployment errors
- [ ] Review recent logs
- [ ] Verify backups

### Monthly
- [ ] Update dependencies (if safe)
- [ ] Review security advisories
- [ ] Analyze usage metrics

### Quarterly
- [ ] Full backup
- [ ] Security audit
- [ ] Performance review

---

## 📞 TROUBLESHOOTING

### If Deployment Fails
- [ ] Check platform logs
- [ ] Verify environment variables
- [ ] Run `python manage.py migrate` on platform
- [ ] Check Procfile syntax
- [ ] Verify Python version matches

### If Static Files Missing
- [ ] Run `python manage.py collectstatic --noinput`
- [ ] Verify STATIC_ROOT path
- [ ] Redeploy application

### If Database Connection Fails
- [ ] Verify DATABASE_URL format
- [ ] Check database is running
- [ ] Verify credentials
- [ ] Check firewall rules

### If Images Don't Upload
- [ ] Verify media directory exists
- [ ] Check file permissions
- [ ] Verify MEDIA_ROOT is writable
- [ ] Check disk space

---

## 🎉 SUCCESS INDICATORS

✅ You're successful when:
- [ ] Site loads without errors
- [ ] All features work as expected
- [ ] HTTPS is enabled
- [ ] Admin panel is accessible
- [ ] Images display correctly
- [ ] Database is persistent
- [ ] Logs show no critical errors
- [ ] Users can signup and shop

---

## 📞 SUPPORT CONTACTS

- **Django Docs:** https://docs.djangoproject.com/5.2/
- **Railway Support:** https://railway.app/support
- **PythonAnywhere Help:** https://help.pythonanywhere.com/
- **Render Support:** https://render.com/support

---

## 🎯 FINAL STEPS

1. [ ] Complete this checklist
2. [ ] Follow DEPLOYMENT.md for your platform
3. [ ] Deploy to production
4. [ ] Run post-deployment tests
5. [ ] Monitor first week closely
6. [ ] Celebrate! 🎉

---

**Date Started:** _______________
**Date Deployed:** _______________
**Platform:** _______________
**Domain:** _______________
**Notes:** _______________

---

**Keep this checklist for reference and future deployments!**
