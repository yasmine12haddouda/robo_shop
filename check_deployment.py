#!/usr/bin/env python
"""
Deployment readiness checker for Robo Shop
Verifies all required configurations before hosting
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robo_shop.settings')
django.setup()

from django.conf import settings
from django.core.management import call_command

def check_requirements():
    """Verify all requirements are met"""
    BASE_DIR = Path(__file__).resolve().parent
    issues = []
    
    print("🔍 Checking Robo Shop Deployment Readiness...")
    print("-" * 50)
    
    # 1. Check required files
    print("\n✓ Checking required files...")
    required_files = [
        'Procfile',
        'runtime.txt',
        'requirements.txt',
        '.env.example',
        'DEPLOYMENT.md',
        'README.md',
    ]
    
    for file in required_files:
        path = BASE_DIR / file
        if path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - MISSING")
            issues.append(f"Missing {file}")
    
    # 2. Check Django settings
    print("\n✓ Checking Django settings...")
    
    if settings.DEBUG:
        print(f"  ⚠️  DEBUG = {settings.DEBUG} (should be False in production)")
    else:
        print(f"  ✅ DEBUG = False")
    
    if not settings.ALLOWED_HOSTS:
        print(f"  ⚠️  ALLOWED_HOSTS is empty (will fail in production)")
    else:
        print(f"  ✅ ALLOWED_HOSTS configured: {settings.ALLOWED_HOSTS}")
    
    if settings.SECRET_KEY.startswith('django-insecure'):
        print(f"  ⚠️  SECRET_KEY uses insecure default (change in production)")
    else:
        print(f"  ✅ SECRET_KEY is set")
    
    # 3. Check installed apps
    print("\n✓ Checking installed apps...")
    required_apps = [
        'accounts.apps.AccountsConfig',
        'store',
        'shopping_cart',
        'sales',
    ]
    
    for app in required_apps:
        if app in settings.INSTALLED_APPS:
            print(f"  ✅ {app}")
        else:
            print(f"  ❌ {app} - NOT INSTALLED")
            issues.append(f"App {app} not in INSTALLED_APPS")
    
    # 4. Check middleware
    print("\n✓ Checking middleware...")
    if 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE:
        print(f"  ✅ WhiteNoise middleware configured")
    else:
        print(f"  ⚠️  WhiteNoise middleware not found")
    
    # 5. Check static/media configuration
    print("\n✓ Checking file serving...")
    print(f"  ✅ STATIC_URL: {settings.STATIC_URL}")
    print(f"  ✅ MEDIA_URL: {settings.MEDIA_URL}")
    print(f"  ✅ STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"  ✅ MEDIA_ROOT: {settings.MEDIA_ROOT}")
    
    # 6. Check database
    print("\n✓ Checking database...")
    db_engine = settings.DATABASES['default']['ENGINE']
    print(f"  ℹ️  Database: {db_engine}")
    if 'sqlite' in db_engine:
        print(f"  ⚠️  SQLite detected (recommend PostgreSQL for production)")
    
    # 7. Check environment variables (.env file)
    print("\n✓ Checking environment configuration...")
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        print(f"  ✅ .env file exists")
    else:
        print(f"  ⚠️  .env file not found (create from .env.example)")
    
    # 8. Summary
    print("\n" + "-" * 50)
    if issues:
        print(f"\n⚠️  Found {len(issues)} issue(s):\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        return False
    else:
        print("\n✅ All checks passed! Ready for deployment.")
        print("\nNext steps:")
        print("  1. Update ALLOWED_HOSTS for your domain")
        print("  2. Generate a new SECRET_KEY")
        print("  3. Create .env file with production values")
        print("  4. Run: python manage.py collectstatic --noinput")
        print("  5. Run: python manage.py migrate")
        print("  6. Push to GitHub and deploy")
        return True

if __name__ == '__main__':
    success = check_requirements()
    sys.exit(0 if success else 1)
