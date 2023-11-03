
from django.urls import path,include
from note import views


urlpatterns = [
    path('',views.dailynote, name='dailynote'),
]
