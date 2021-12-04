from django.urls import path
from .views import profile_view, update_profile

urlpatterns = [
    path('profile/', profile_view, name='profile-view'),
    path('update/', update_profile, name='update'),

]