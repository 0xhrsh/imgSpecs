from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from classifier.views import FileUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^img/(?P<src>.+)$', FileUploadView.as_view()),
]
