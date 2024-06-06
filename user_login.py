# urls.py (in project directory)
from django.urls import path, include

urlpatterns = [
    # Include matching app URLs
    path('api/', include('matching.urls')),
    # Include users app URLs
    path('api/', include('users.urls')),
]

# urls.py (in matching app)
from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for retrieving list of livestock
    path('livestock/', views.livestock_list, name='livestock-list'),
]

# urls.py (in users app)
from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for user login
    path('login/', views.user_login, name='user-login'),
]
