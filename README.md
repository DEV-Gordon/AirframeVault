# AirframeVault Backend

This is the backend for AirframeVault, a Django 6.x project for managing and exposing data about DCS World aircraft, their images, videos, manufacturers, developers, and roles. It provides a REST API (read-only) and a Django admin interface for data management.

## Features
- Django 6.x with modular app structure (`core`, `api`)
- REST API using Django REST Framework (DRF)
- Filtering, pagination, and read-only permissions for API
- Media support for multiple images and videos per aircraft
- Custom admin with previews and API links
- English docstrings and comments for maintainability

## Project Structure
```
backend/
    manage.py
    requirements.txt
    airframevault/
        settings.py
        urls.py
    apps/
        core/
            models.py
            admin.py
        api/
            serializers.py
            views.py
            urls.py
prototypes/
```

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```sh
   python manage.py migrate
   ```
3. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
4. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Usage
- All endpoints are read-only (GET only).
- Filtering and pagination are enabled.
- Example endpoint: `/api/aircraft-types/`
- See the API output for JSON structure.

## Admin Usage
- All data creation and modification is done via the Django admin panel.
- Admin includes image/video previews and API view buttons.

## Requirements
- Python 3.11+
- Django 6.x
- Django REST Framework
- django-filter
- Pillow

## License
MIT License
