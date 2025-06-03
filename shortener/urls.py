from django.urls import path
from . import views
from .views import CreateShortURL, URLListView, DeactivateURL, RedirectToOriginalView

urlpatterns = [
    path('create/', views.CreateShortURL.as_view(), name='create-short-url'),
    path('list/', views.URLListView.as_view(), name='show-list'),
    path('deactivate/<str:short_code>/', views.DeactivateURL.as_view(), name='deactivate'),
    path('<str:short_code>/', views.RedirectToOriginalView.as_view(), name='redirect'),
]
