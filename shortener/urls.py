from django.urls import path
from . import views
from .views import CreateShortURL, URLListView, DeactivateURL, RedirectToOriginalView, GlobalStatsView

urlpatterns = [
    path('create/', views.CreateShortURL.as_view(), name='create-short-url'),
    path('list/', views.URLListView.as_view(), name='show-list'),
    path('deactivate/<str:short_code>/', views.DeactivateURL.as_view(), name='deactivate'),
    path('stats/', views.GlobalStatsView.as_view(), name='global-stats'),
]
