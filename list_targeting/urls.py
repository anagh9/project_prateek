from django.urls import path

from .views import *

app_name = 'list_targeting'

urlpatterns = [
    path('', index, name='index'),
    path('list-targeting/', list_targeting, name='list_targeting'),
    path('list-targeting/<int:request_id>',
         list_targetin_request_id, name='list_targetin_request_id'),
    path('criteria-targeting/', criteria_targeting, name='criteria_targeting'),
    path('reporting-dashboard/', reporting_dashboard, name='reporting_dashboard'),
    path('reporting-dashboard-2/', reporting_dashboard2,
         name='reporting_dashboard'),
    path('api/get-report-data/', get_report_data,
         name='get_report_data_api'),
]
