from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('data',views.data),
    path('sellerreg',views.sellerreg),
    path('logout',views.logout),
    path('allorder',views.allorder),
    path('statuschange/<int:oid>',views.statuschange,name='statuschange'),
    path('newstatus/<int:oid>', views.newstatus, name='newstatus'),
]