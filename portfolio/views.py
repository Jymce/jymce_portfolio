from django.http import Http404
from django.shortcuts import render

PROJECTS = [
    {
        "slug": "echonote",
        "title": "EchoNote",
        "description": (
            "Real-time video conferencing with live AI transcription, "
            "speaker-ordered transcripts, and AI meeting summaries."
        ),
        "details": (
            "EchoNote is a real-time video conferencing app built for pure, "
            "focused meetings. Create instant rooms, get speaker-ordered live "
            "transcripts in English and Tagalog, generate AI summaries, and "
            "translate meeting records. Guests can join with just a meeting "
            "code — no account needed. Runs on Django + Channels (ASGI) with "
            "WebRTC for the video layer, deployed on Render."
        ),
        "tech": ["Django", "Django Channels", "WebRTC", "AI Transcription", "Render"],
        "demo": "https://echonotes-zkcl.onrender.com/",
        "repo": "",
        "logo": "img/projects/echonote.svg",
    },
    {
        "slug": "thackey",
        "title": "Thackey",
        "description": (
            "Typing test app with AI-powered analysis that pinpoints your "
            "weak areas and helps you improve where it matters most."
        ),
        "details": (
            "Thackey is a typing test application that goes beyond raw speed. "
            "AI processing analyzes your typing patterns to identify the keys, "
            "words, and patterns where you struggle most, then helps you train "
            "those specific weak areas. Built with Django and deployed on "
            "PythonAnywhere."
        ),
        "tech": ["Django", "AI Analysis", "JavaScript", "PythonAnywhere"],
        "demo": "https://thackey.pythonanywhere.com/",
        "repo": "",
        "logo": "img/projects/thackey.svg",
    },
    {
        "slug": "wellfind",
        "title": "WellFind",
        "description": (
            "E-commerce web app with product catalog, cart, and checkout "
            "powered by PayPal integration."
        ),
        "details": (
            "WellFind is an e-commerce application featuring a browsable "
            "product catalog, shopping cart, and a complete checkout flow "
            "integrated with PayPal (sandbox) for payment processing. Built "
            "with Django and deployed on PythonAnywhere."
        ),
        "tech": ["Django", "PayPal API", "E-commerce", "PythonAnywhere"],
        "demo": "https://wellfind.pythonanywhere.com/",
        "repo": "",
        "logo": "img/projects/wellfind.png",
    },
]


def home(request):
    context = {
        "name": "Jymce Bertillo",
        "role": "Software Developer",
        "tagline": (
            "I build reliable web applications and APIs with Django "
            "and modern tooling."
        ),
        "about": (
            "I'm a software developer who enjoys designing clean APIs "
            "and data-driven applications. My core stack is Django and Django "
            "REST Framework, paired with Tailwind CSS for polished front-ends "
            "and MySQL, PostgreSQL, or Supabase for storage."
        ),
        "skills": [
            {
                "name": "Django",
                "category": "Backend",
                "description": "Full-stack web framework for building robust, maintainable applications.",
                "logo": "img/icons/django.svg",
            },
            {
                "name": "Django REST Framework",
                "category": "Backend",
                "description": "Powerful toolkit for designing and shipping clean REST APIs.",
                "logo": "img/icons/djangorest.svg",
            },
            {
                "name": "Tailwind CSS",
                "category": "Frontend",
                "description": "Utility-first CSS for fast, consistent, modern interfaces.",
                "logo": "img/icons/tailwindcss.svg",
            },
            {
                "name": "MySQL",
                "category": "Database",
                "description": "Reliable relational database for production workloads.",
                "logo": "img/icons/mysql.svg",
            },
            {
                "name": "PostgreSQL",
                "category": "Database",
                "description": "Advanced open-source relational database with rich features.",
                "logo": "img/icons/postgresql.svg",
            },
            {
                "name": "Supabase",
                "category": "Backend / Database",
                "description": "Postgres-powered backend-as-a-service with auth and realtime.",
                "logo": "img/icons/supabase.svg",
            },
        ],
        "projects": PROJECTS,
        "socials": {
            "github": "https://github.com/Jymce",
            "linkedin": "https://www.linkedin.com/in/jymcebertillo/",
            "email": "mailto:jymcebrian@gmail.com",
        },
    }
    return render(request, "portfolio/home.html", context)


def project_detail(request, slug):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if project is None:
        raise Http404("Project not found")
    return render(request, "portfolio/project_detail.html", {"project": project})
