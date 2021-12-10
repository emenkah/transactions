from django.urls import path
from . views import ReadDataView

urlpatterns = [
    path('read-data/', ReadDataView.as_view()),

]