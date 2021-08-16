from django.urls import path
from . import views

app_name = 'info_manager'
urlpatterns = [
    path('info-list-7/',views.info_list_7,name='info_list_7'),
    path('info-list-8/',views.info_list_8,name='info_list_8'),
    path('info-list-9/',views.info_list_9,name='info_list_9'),
    path('upload-index-7/',views.upload_index_7,name='upload_index_7'),
    path('upload-index-8/',views.upload_index_8,name='upload_index_8'),
    path('upload-index-9/',views.upload_index_9,name='upload_index_9'),
    path('info-update-7/<int:id>/',views.info_update_7,name='info_update_7'),
    path('info-update-8/<int:id>/',views.info_update_8,name='info_update_8'),
    path('info-update-9/<int:id>/',views.info_update_9,name='info_update_9'),
    path('upload-finished/',views.upload_finished,name='upload_finished'),
    path('info-index/',views.info_index,name='info_index'),
    path('export-7/', views.export_excel_7, name='export_7'),
    path('export-8/', views.export_excel_8, name='export_8'),
    path('export-9/', views.export_excel_9, name='export_9'),
]