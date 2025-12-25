@echo off
REM Setup script for Robo Shop development

echo Creating .env file...
copy .env.example .env

echo.
echo Updating .env with development settings...
REM This is a placeholder - user needs to edit .env manually

echo.
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Creating superuser...
python manage.py createsuperuser

echo.
echo Setup complete! Run the server with: python manage.py runserver
