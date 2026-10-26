# Jymce Bertillo — Portfolio

A modern personal portfolio built with **Django**, styled with **Tailwind CSS** using a
**shadcn/ui-style component system** — the same CSS-variable design tokens and
variant classes (`btn`, `btn-outline`, `card`, `badge-secondary`, ...), adapted for
Django templates instead of React.

## Stack

- Django 5.2 (LTS)
- Tailwind CSS 3.4 via the standalone CLI — compiled CSS, no Node/npm needed
- shadcn/ui design tokens in `static/css/input.css` + `tailwind.config.js`
- Component classes (`btn`, `badge`, `card` variants) + icon partials in
  `templates/portfolio/components/ui/`
- SQLite for local dev (swap to MySQL/PostgreSQL/Supabase in `settings.py` if needed)

## Local development

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Tailwind / theming

The CSS is compiled with the [Tailwind standalone CLI](https://github.com/tailwindlabs/tailwindcss/releases)
(a single binary — download `tailwindcss-windows-x64.exe` or the macOS/Linux build to
the project root as `tailwindcss`).

```bash
# Rebuild once (production)
python manage.py tailwind build

# Watch mode while editing templates
python manage.py tailwind start
```

(`manage.py tailwind` wraps the standalone CLI; you can also invoke
`./tailwindcss -i static/css/input.css -o static/css/output.css --watch` directly.)

- Design tokens (light/dark) live in `@layer base` in `static/css/input.css`
- Reusable variants live in `@layer components` — add new ones there
- Theme extension (colors, fonts, radius) lives in `tailwind.config.js`

## Editing content

All page content lives in `portfolio/views.py` — update `name`, `role`, `tagline`,
`about`, `skills`, `socials`, and add entries to `projects` when ready:

```python
"projects": [
    {
        "title": "My Project",
        "description": "What it does.",
        "tech": ["Django", "DRF", "PostgreSQL"],
        "demo": "https://...",
        "repo": "https://github.com/...",
    },
],
```

## Deploying to PythonAnywhere

1. Push this repo to GitHub, then on PythonAnywhere open a **Bash console**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   python3.13 -m venv venv        # or any Python >= 3.10
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic
   ```

2. **Web tab → Add a new web app → Manual configuration** (pick the same Python version
   as your venv).

3. On the web app config page:
   - **Virtualenv**: `/home/yourusername/your-repo/venv`
   - **WSGI file** (`/var/www/yourusername_pythonanywhere_com_wsgi.py`): replace contents
     with:
     ```python
     import os, sys
     path = '/home/yourusername/your-repo'
     if path not in sys.path:
         sys.path.insert(0, path)
     os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
     os.environ['DJANGO_DEBUG'] = 'False'
     os.environ['DJANGO_ALLOWED_HOSTS'] = 'yourusername.pythonanywhere.com'
     os.environ['DJANGO_SECRET_KEY'] = 'generate-a-long-random-string'
     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```
   - **Static files** mapping: URL `/static/` → directory
     `/home/yourusername/your-repo/staticfiles`

4. Click **Reload**. Done.

> `static/css/output.css` is committed to the repo, so no build step is needed on
> PythonAnywhere — just `collectstatic`. If you change templates/styles before
> deploying, rebuild it locally with the Tailwind CLI first.
