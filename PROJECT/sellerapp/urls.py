from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('data',views.data),
    path('sellerreg',views.sellerreg),
    path('logout',views.logout),
]