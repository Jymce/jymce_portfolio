from django_distill import distill_path

from . import views

app_name = "portfolio"


def get_project_slugs():
    for project in views.PROJECTS:
        yield (project["slug"],)


urlpatterns = [
    distill_path("", views.home, name="home"),
    distill_path("404.html", views.not_found, name="not_found"),
    distill_path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail",
        distill_func=get_project_slugs,
    ),
]
