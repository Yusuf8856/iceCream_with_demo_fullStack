from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Yusuf Admin"  # Changes "Django administration" at the top
admin.site.site_title = "Ice Cream Admin"           # Changes the browser tab title
admin.site.index_title = "Welcome to My Ice Cream Shop"

urlpatterns = [
    path("admin/", admin.site.urls),   # This is my admin url of my project
    path("", include("home.urls")),    # It sends the response to my app (home) 
]