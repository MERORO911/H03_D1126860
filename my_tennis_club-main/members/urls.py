from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('', include('web.urls')),
    path('court/', include('places.urls')),  
    path('admin/', admin.site.urls),

    # 其他路由...
]
