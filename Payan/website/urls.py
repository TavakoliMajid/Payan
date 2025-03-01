from django.urls import path
from .views import home  # ✅ Ensure `home` is the correct function in `views.py`
from . import  views
urlpatterns = [
    path('', views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),  # New sell page
    path('login/', views.login_view, name='login'),  # New login page
    path('signup/', views.signup, name='signup'),  # New signup page
]
from django.urls import path
from . import views

urlpatterns = [
    path("check-email/", views.check_email, name="check_email"),
    path("login/", views.login_user, name="login_user"),
    path("guest-login/", views.guest_login, name="guest_login"),
    path("signup/", views.signup, name="signup"),
]

