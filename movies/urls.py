from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views
from api.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')), #allow login/logout for non-admin from local server page
    path('api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.movie_list),
    path('api/movies/', views.movie_list),
    path('api/movies/<int:pk>', views.getMovie),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
