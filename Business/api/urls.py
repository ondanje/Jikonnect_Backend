from django.urls import path
from  Business.api.views import  get_business,update_business,create_business,detail_business ,get_business_admin

urlpatterns = [
    path('business/edit/<str:name>/',update_business, name='business-update'),
    path('business/get/<str:name>/',get_business, name='business-get'),
    path('business/get/',get_business, name='business-get'),
    path('admin_business/get/',get_business_admin, name='business-get'),
    path('business/detail/<str:name>/', detail_business, name='business-detail'),
    path('business/', create_business, name='business-create'),
    
]