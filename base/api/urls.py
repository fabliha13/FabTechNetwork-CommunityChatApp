from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes),
    # path('', include('base.urls')),
    # path('api/', include('base.api.urls'))
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),

]
