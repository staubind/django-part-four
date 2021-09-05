from django.urls import path
from basic_app import views

# so that we can point to our paths here using relative paths
app_name = 'basic_app' # always set this to whatever the application's name is
# allows us to use template tagging.

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]