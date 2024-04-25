from django.urls import path, include

urlpatterns = [
    path(
        "works/",
        include(
            "logic.endpoints.works.urls",
        ),
    ),
]
