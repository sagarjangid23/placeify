from django.urls import path
from .views import home_view, upload_view, place_detail_view

urlpatterns = [
    path("", home_view, name="home"),
    path("upload/", upload_view, name="upload"),
    path('places/<int:place_id>/', place_detail_view, name='place_detail'),
]
