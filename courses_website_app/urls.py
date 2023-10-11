from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_list, name="courses_list"),
    path("course/<int:courses_id>/", views.courses_detail, name="courses_detail")
]