from django.urls import path
from . import views

app_name = 'info_manager'
urlpatterns = [
    path('info-list/<int:index>/',views.info_list,name='info_list'),
    path('upload-index/<int:grade>/',views.upload_index,name='upload_index'),
    path('info-update/<int:grade>/<int:id>/',views.info_update,name='info_update'),
    # path('info-update-8/<int:id>/',views.info_update_8,name='info_update_8'),
    # path('info-update-9/<int:id>/',views.info_update_9,name='info_update_9'),
    path('upload-finished/',views.upload_finished,name='upload_finished'),
    path('info-index/',views.info_index,name='info_index'),
    path('export-7/<int:index>/', views.export_excel, name='export'),
]