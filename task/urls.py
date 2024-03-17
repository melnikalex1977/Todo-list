from django.urls import path

from . import views
from .views import (
    index,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDone,
    TaskNotDoneView,

)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path('task-done/<int:pk>/', TaskDone.as_view(), name='task-done'),
    path('task-not-done/<int:pk>/', TaskNotDoneView.as_view(), name='task-not-done'),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("drivers/", TagListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", TagDetailView.as_view(), name="driver-detail"
    ),
    path("drivers/create/", TagCreateView.as_view(), name="driver-create"),
    path(
        "drivers/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="driver-update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="driver-delete"
    ),
]

app_name = "task"
