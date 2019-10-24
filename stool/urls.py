from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view()),
    path('profile/', views.profile),
    path('', views.home),
    path('logout/', views.logout_view),
    path('signup/', views.sign_up),
    path('<username>/', views.post_on_wall, name="post_on_wall"),
]
