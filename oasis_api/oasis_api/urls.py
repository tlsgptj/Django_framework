"""oasis_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import RegisterView
from mileage.views import MileageListView
from payments.views import CardCreateView
from store.views import StoreListView
from users.views import LogoutView
from reviews.views import ReviewCreateView, ReviewListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('my-mileage/', MileageListView.as_view(), name='mileage-list'),
    path('add-card/', CardCreateView.as_view(), name='add-card'),
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('list/', ReviewListView.as_view(), name='review-list'),
    
]
