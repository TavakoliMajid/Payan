from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from website import views  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.home, name='home'),

    # Authentication Endpoints
    path('check-email/', views.check_email, name='check_email'),
    path('login/', views.login_user, name='login_user'),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('signup/', views.signup, name='signup'),

    # Buy Page (Ensure `buy.html` is inside `templates/`)
    path('buy/', views.buy, name='buy'),
    path('buy.html', TemplateView.as_view(template_name="buy.html"), name='buy_page'),

    # Include other app URLs if necessary
    path('', include('website.urls')),
]
