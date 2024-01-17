from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

app_name = "pegasus_employees"

urlpatterns = [
    path(
        "objects/",
        login_required(
            TemplateView.as_view(
                template_name="pegasus/employees/object_lifecycle_home.html",
                extra_context={"active_tab": "object_lifecycle"},
            )
        ),
        name="object_lifecycle_home",
    ),
    path("objects/react/", views.ReactObjectLifecycleView.as_view(), name="react_object_lifecycle"),
    path("objects/react/<path:path>", views.ReactObjectLifecycleView.as_view(), name="react_object_lifecycle_w_path"),
    path("charts/", views.ChartsView.as_view(), name="charts"),
    path("api/employee-data/", views.EmployeeDataAPIView.as_view(), name="employee_data"),
]


# drf config
router = routers.DefaultRouter()
router.register("api/employees", views.EmployeeViewSet)

urlpatterns += router.urls