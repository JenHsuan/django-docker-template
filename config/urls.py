from django.contrib import admin
from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentListView.as_view(), name='students')
]
