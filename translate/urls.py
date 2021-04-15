from django.urls import path
from . import views

app_name = "translate"
urlpatterns = [
  path("create/", views.TranslateCreateView.as_view(),name="create"),
  path("", views.TranslateListView.as_view(),name="list"),
  path("<str:pk>/", views.TranslateDetailView.as_view(),name="detail"),
]