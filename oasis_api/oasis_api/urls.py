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
from django.urls import path, include
from mileage.views import MileageListView
from payments.views import register_card
from store.views import StoreListView
from users.api import LogoutAPI, UserDetailAPI, RegisterAPI
from reviews.views import ReviewCreateView, ReviewListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('me/', UserDetailAPI.as_view(), name='user_detail'),  # 사용자 정보 조회 API
    path('register/', RegisterAPI.as_view(), name='auth_register'),  # 사용자 등록 API
    path('logout/', LogoutAPI.as_view(), name='auth_logout'),  # 로그아웃 API
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신
    path('my-mileage/', MileageListView.as_view(), name='mileage-list'),  # 마일리지 조회
    path('api/', include('payments.urls')),
    path('stores/', StoreListView.as_view(), name='store-list'),  # 스토어 목록 조회
    path('api/auth/', include('dj_rest_auth.urls')),  # 인증 관련 URL들 (로그인, 패스워드 리셋 등)
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # 회원가입 관련 URL들
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('list/', ReviewListView.as_view(), name='review-list'),  # 리뷰 목록 조회
]

