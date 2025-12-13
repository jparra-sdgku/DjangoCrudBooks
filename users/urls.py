from django.urls import include, path
from . import views

urlpatterns=[
    # Use django's built-in auth views
    path('accounts/', include('django.contrib.auth.urls')),

    # Route for our custom signup view
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #Route for the user profile
    path('profile/', views.profile_view, name='profile'),

    ]