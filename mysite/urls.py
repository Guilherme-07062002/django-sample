from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include(("polls.urls", "polls"), namespace="polls")),
    path("tasks/", include(("todolist.urls", "tasks"), namespace="tasks")),
    path("admin/", admin.site.urls),
]