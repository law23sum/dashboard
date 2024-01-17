from django.urls import path
from django.views.generic import TemplateView


app_name = "tutorial_basics"

urlpatterns = [
    path(
        "basic-html-page/",
        TemplateView.as_view(
            template_name="tutorial/basic_html_page.html", extra_context={"active_tab": "basics_html_page"}
        ),
        name="basics_html_page",
    ),
]