from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateShortURL.as_view(), name='create'),
    path('list/', views.URLListView.as_view(), name='list'),
    path('deactivate/<str:short_code>/', views.DeactivateURL.as_view(), name='deactivate'),
    path('<str:short_code>/', views.RedirectToOriginalView.as_view(), name='redirect'),
]
