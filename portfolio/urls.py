from django.urls import path

from .views import homepage
from .views import print_context
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', homepage),
    path('context/', print_context),
]

urlpatterns += staticfiles_urlpatterns()