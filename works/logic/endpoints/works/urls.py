from django.urls import path

from .endpoints import WorkListEndpoint

urlpatterns = [
    path(
        "",
        WorkListEndpoint.as_view(),
        name="work-list-endpoint",
    ),
]
