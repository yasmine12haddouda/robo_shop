# 🐍 Django Commands Quick Reference

Essential commands for developing and deploying Robo Shop.

## Development Server

```bash
# Run local development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run accessible from other machines
python manage.py runserver 0.0.0.0:8000
```

## Database Management

```bash
# Create migrations for model changes
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations accounts store shopping_cart sales

# Apply migrations to database
python manage.py migrate

# Migrate specific app
python manage.py migrate accounts

# Show migration history
python manage.py showmigrations

# Reverse migrations
python manage.py migrate accounts 0001
```

## User & Admin

```bash
# Create superuser for admin
python manage.py createsuperuser

# Change superuser password
python manage.py changepassword username

# Create user interactively
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@example.com', 'password')
```

## Static Files

```bash
# Collect static files for production
python manage.py collectstatic

# Collect without prompting
python manage.py collectstatic --noinput

# Clear collected static files
python manage.py collectstatic --clear

# Show collected static files
python manage.py collectstatic --dry-run
```

## Testing

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test accounts

# Run specific test
python manage.py test accounts.tests.SignupTest

# Run with verbose output
python manage.py test --verbosity=2

# Run with coverage (requires coverage package)
coverage run --source='.' manage.py test
coverage report
```

## Database Shell

```bash
# Access database shell (SQLite)
python manage.py dbshell

# For SQLite, you can also use sqlite3 directly
sqlite3 db.sqlite3
```

## Django Shell

```bash
# Interactive Python shell with Django context
python manage.py shell

# Example usage:
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> users = User.objects.filter(is_active=True)
>>> users.count()
>>> from store.models import Product
>>> Product.objects.create(name='Test', price=99.99)
```

## Debugging & Validation

```bash
# Check Django configuration
python manage.py check

# Check specific app
python manage.py check accounts

# Show settings value
python manage.py shell
>>> from django.conf import settings
>>> settings.DEBUG

# Show installed apps
python manage.py shell
>>> from django.conf import settings
>>> settings.INSTALLED_APPS
```

## Data Management

```bash
# Dump database to JSON
python manage.py dumpdata > db.json

# Dump specific app
python manage.py dumpdata accounts > accounts.json

# Load data from JSON
python manage.py loaddata db.json

# Delete all data from database
python manage.py flush
```

## URLs

```bash
# Show all URL patterns
python manage.py show_urls

# Show URLs with patterns (requires django-extensions)
pip install django-extensions
# Add 'django_extensions' to INSTALLED_APPS
python manage.py show_urls
```

## Cache & Sessions

```bash
# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()

# Clear expired sessions
python manage.py clearsessions
```

## Custom Management Commands

```bash
# Create custom command template
python manage.py startapp yourcommand

# Then create: yourcommand/management/commands/yourcommand.py
# Run custom command:
python manage.py yourcommand
```

## Production Deployment

```bash
# Collect static files for production
python manage.py collectstatic --noinput

# Run migrations (should be in Procfile)
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Django checks before deployment
python manage.py check --deploy

# Generate SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Useful Django Shell Queries

```python
# Users
from django.contrib.auth.models import User
User.objects.all()
User.objects.filter(is_staff=True)
user = User.objects.get(username='username')
user.set_password('newpassword')
user.save()

# Products
from store.models import Product
Product.objects.all()
Product.objects.filter(seller__user__username='seller_name')
product = Product.objects.get(id=1)
product.delete()

# Sellers
from accounts.models import Seller
Seller.objects.all()
seller = Seller.objects.get(user__username='username')

# Payments
from sales.models import Payment
Payment.objects.all()
Payment.objects.filter(user__username='username')
Payment.objects.filter(state='Algiers')
```

## Useful Shortcuts

```bash
# Alias for quick restart
alias dmr='python manage.py runserver'

# Run manage.py from any directory
export PYTHONPATH="${PYTHONPATH}:/path/to/robo_shop"

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

## Environment Variables (Development)

```bash
# Create .env file for local development
DEBUG=True
SECRET_KEY=your-test-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Load in Python
from decouple import config
debug = config('DEBUG', default=True, cast=bool)
```

## Error Troubleshooting

```bash
# ModuleNotFoundError: No module named 'modulename'
pip install modulename
pip install -r requirements.txt

# django.core.exceptions.ImproperlyConfigured
# Usually means INSTALLED_APPS or DATABASES configuration issue
python manage.py check

# Template not found
# Check TEMPLATES setting in settings.py
# Verify app is in INSTALLED_APPS

# Permission denied (database locked)
# SQLite database locked - close other connections
rm db.sqlite3-journal

# Port already in use
python manage.py runserver 8080  # Use different port
```

---

**💡 Pro Tip:** Create a `Makefile` for common commands:

```makefile
.PHONY: help runserver migrate test shell

help:
	@echo "Available commands:"
	@echo "  make runserver - Start development server"
	@echo "  make migrate - Run migrations"
	@echo "  make test - Run tests"
	@echo "  make shell - Open Django shell"

runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

test:
	python manage.py test

shell:
	python manage.py shell
```

Then run with: `make runserver`, `make migrate`, etc.

---

See [Django Documentation](https://docs.djangoproject.com/5.2/) for more commands!
