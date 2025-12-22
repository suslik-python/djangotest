from django.contrib import admin
from django.urls import path
from core.views import mainVeiew, contacts_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainVeiew),
    path('contacts/', contacts_page)
]
