from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("note_app.urls")),
    path("auth/", include("user_profiles.urls")),


]
