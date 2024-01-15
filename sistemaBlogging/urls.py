from django.urls import path
from blogging.views import PublicacionListCreate, PublicacionRetrieveUpdateDestroy

urlpatterns = [
    path('publicaciones/', PublicacionListCreate.as_view()),
    path('publicaciones/<int:pk>/', PublicacionRetrieveUpdateDestroy.as_view()),
]