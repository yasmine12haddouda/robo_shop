# Robo Shop - E-Commerce Platform

A Django-based e-commerce platform with seller and buyer roles, product management with image uploads, shopping cart, and payment processing.

## Features

✅ **User Authentication**
- Role-based signup (Seller/Buyer)
- Secure login/logout
- Email-based accounts

✅ **Seller Dashboard**
- Add products with images
- Manage inventory
- View product listings

✅ **Product Management**
- Image uploads for products
- Price and description management
- Stock tracking

✅ **Shopping Cart**
- Add/remove items
- Quantity selection
- Real-time total calculation
- Stock validation

✅ **Payment Processing**
- Contact information collection
- Algerian state selection (48 wilayas)
- Multiple payment methods
- Order confirmation

✅ **Responsive Design**
- Bootstrap 5.3.2 UI
- Mobile-friendly templates
- Accessible forms

## Tech Stack

- **Backend:** Django 5.2.7
- **Frontend:** Bootstrap 5.3.2
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Image Processing:** Pillow
- **Web Server:** Gunicorn (production)
- **Static Files:** WhiteNoise

## Installation

### Quick Start (Windows)

```bash
# Run setup script
setup.bat

# Edit .env file if needed
# Then start development server
python manage.py runserver
```

### Manual Setup (All Platforms)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Visit: http://localhost:8000

## Project Structure

```
robo_shop/
├── accounts/          # User authentication
│   ├── models.py      # Seller model
│   ├── views.py       # Signup/login views
│   ├── forms.py       # SignupForm with role
│   └── templates/
├── store/             # Product management
│   ├── models.py      # Product model with images
│   ├── views.py       # Seller dashboard, product list
│   └── templates/
├── shopping_cart/     # Cart functionality
│   ├── views.py       # Add/remove cart items
│   └── templates/
├── sales/             # Payment processing
│   ├── models.py      # Payment model
│   ├── views.py       # Checkout, payment success
│   └── templates/
├── robo_shop/         # Main project config
│   ├── settings.py    # Django settings
│   ├── urls.py        # URL routing
│   └── wsgi.py        # WSGI application
├── Procfile           # Deployment configuration
├── runtime.txt        # Python version
└── requirements.txt   # Dependencies
```

## User Roles

### Seller
- Create and manage products
- Upload product images
- View dashboard at `/seller/`
- Track inventory

### Buyer
- Browse products
- Add items to cart
- Checkout with payment details
- View product listings

## Key URLs

| URL | Purpose |
|-----|---------|
| `/` | Home / Product List |
| `/signup/` | User Registration |
| `/login/` | User Login |
| `/logout/` | User Logout |
| `/seller/` | Seller Dashboard |
| `/cart/` | Shopping Cart |
| `/checkout/` | Payment Checkout |
| `/admin/` | Django Admin |

## Database Models

### User (Django Built-in)
- username, email, password
- is_staff, is_superuser

### Seller
- user (OneToOneField to User)
- phone, address

### Product
- name, description, price
- image (ImageField)
- seller (ForeignKey to Seller)
- stock

### Cart Item (Session-based)
- Stored in `request.session['cart']`
- Product ID and quantity pairs

### Payment
- first_name, last_name, phone
- state (Algerian wilaya)
- amount, payment_method
- user (optional, ForeignKey to User)

## Configuration

### Environment Variables (.env)

```env
DEBUG=True                    # Set to False in production
SECRET_KEY=your-secret-key   # Change in production
ALLOWED_HOSTS=localhost      # Add domains in production
```

See `.env.example` for full list.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete hosting instructions.

**Quick Summary:**
- Recommended: Railway.app (free, easy)
- Alternative: PythonAnywhere, Render.com
- Database: PostgreSQL for production
- Static files: Handled by WhiteNoise

### Pre-deployment Checklist

```bash
# Collect static files
python manage.py collectstatic --noinput

# Check for issues
python manage.py check

# Run migrations
python manage.py migrate
```

## Development Commands

```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Collect static files for production
python manage.py collectstatic --noinput

# Check Django configuration
python manage.py check

# Interactive Python shell
python manage.py shell
```

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Image uploads not working
- Ensure `media/` directory exists
- Check file permissions
- Verify MEDIA_ROOT in settings.py

### Database errors
- Run migrations: `python manage.py migrate`
- Check DATABASE configuration in settings.py

### Login/authentication issues
- Clear browser cookies
- Check EMAIL_BACKEND in settings
- Verify user exists in database

## Future Enhancements

- [ ] Email notifications on order
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Advanced search filters
- [ ] Payment gateway integration (real)
- [ ] Admin dashboard analytics
- [ ] Seller ratings

## Support

For issues or questions:
1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for hosting help
2. Review Django documentation: https://docs.djangoproject.com
3. Check Bootstrap docs: https://getbootstrap.com/docs

## License

MIT License - Feel free to use and modify

## Security Notes

- Never commit `.env` file with real secrets
- Always set DEBUG=False in production
- Use HTTPS in production
- Keep dependencies updated: `pip list --outdated`
- Change SECRET_KEY for production

---

**Ready to deploy?** Follow the [DEPLOYMENT.md](DEPLOYMENT.md) guide.
