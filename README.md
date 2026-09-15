# My Favorite Places

A small Django site with a list of my favorite places to go out -
cafés, bookshops and a few secret spots. You can browse the list,
open any place to read the full description, add your own places,
or let the site pick one for you.

## Features

- Home page with a short description and a "Where to go?" button
  that picks a random place - places with a higher rating are more
  likely to be chosen
- List of all places with a preview card for each one
- Detail page for every place with the full description
- Form for adding a new place, with validation
- Places added through the form are stored in the user session,
  so every visitor has their own list

## Requirements

- Python 3.12
- Django 6.1.1 (installed from `requirements.txt`)

## How to run

1. Clone the repository and go into the project folder:

```bash
   git clone https://github.com/YOUR-USERNAME/bogaevska-02-fav-places-lab2.git
   cd bogaevska-02-fav-places-lab2
```

2. Create and activate a virtual environment:

```bash
   python -m venv .venv

   # for Windows:
   .venv\Scripts\activate.ps1
   # for Linux/macOS:
   source .venv/bin/activate
```

3. Install the dependencies:

```bash
   python -m pip install -r requirements.txt
```

4. Apply the migrations (needed for sessions):

```bash
   python manage.py migrate
```

5. Start the development server:

```bash
   python manage.py runserver
```

6. Open http://127.0.0.1:8000/places/ in your browser.

## Project structure

- `mysite/` - project settings and the root URL configuration
- `places/` - the application
  - `data.py` - the fixed list of places shown to every visitor
  - `views.py` - page logic
  - `urls.py` - application routes
  - `forms.py` - the form for adding a new place
  - `templates/places/` - HTML templates
  - `static/places/` - CSS and images

## Code style

The project follows PEP 8. To verify before submitting:

```bash
python check_submission.py
```

To fix formatting automatically:

```bash
python check_submission.py --format
```

## Author

Daryna Bogaevska, AVIS-2, 14/09/2026