# pages/urls.py

from django.contrib import admin
from django.urls import path
from pages.views import login_view, logout_view, main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', main_view, name='main'),  # Main landing page
]
