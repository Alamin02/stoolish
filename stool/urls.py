from django.urls import path, include
from django.contrib.auth.views import login
from . import views
from .forms import LoginForm

urlpatterns = [
    path('login/', login, kwargs={'authentication_form':LoginForm}),
    path('profile/', views.profile),
    path('', views.home),
    path('logout/', views.logout_view),
    path('signup/', views.sign_up),
    path('<username>/', views.post_on_wall),
]
