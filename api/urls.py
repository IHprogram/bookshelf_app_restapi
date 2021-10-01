from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, BookListView, BookRetrieveView, BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('list-book/', BookListView.as_view(), name='list-book'),
    path('detail-book/<str:pk>/', BookRetrieveView.as_view(), name='detail-book'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]