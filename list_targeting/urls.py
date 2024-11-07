from django.urls import path

from .views import *

app_name = 'list_targeting'

urlpatterns = [
    path('', index, name='index'),
    path('list-targeting/', list_targeting, name='list_targeting'),
    path('list-targeting/<int:request_id>',
         list_targetin_request_id, name='list_targetin_request_id'),
    path('criteria-targeting/', criteria_targeting, name='criteria_targeting'),
]