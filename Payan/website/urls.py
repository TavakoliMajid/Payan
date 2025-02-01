from django.urls import path
from .views import home  # ✅ Ensure `home` is the correct function in `views.py`

urlpatterns = [
    path('', home, name='home'),
]
