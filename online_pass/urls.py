from django.contrib import admin
from django.urls import include, path
from register import views as v

from django.views.defaults import page_not_found

from passwords.admin import admin_view
admin.site.admin_view = admin_view
urlpatterns = [
    path('', include("passwords.urls")),
    path('register/', v.register, name="register"),
    path('admin/login/', page_not_found),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
]
