
from django import urls
from django.urls import path, include

urlpatterns = [
    path('first_test/', include('first_test.urls')),
    path('', include('random_word.urls'))
]
