from django.urls import path
from django.urls.conf import include
from accounts import views

urlpatterns = [
    path("registration", include("dj_rest_auth.registration.urls")),
    path("google/login", views.google_login, name="google_login"),
    path("google/callback/", views.google_callback, name="google_callback"),
    path(
        "google/login/finish/",
        views.GoogleLogin.as_view(),
        name="google_login_todjango",
    ),
]
