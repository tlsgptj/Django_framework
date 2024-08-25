from django.contrib import admin
from django.urls import path, include
from mileage.views import MileageListView
from payments.views import register_card
from gift.views import purchase_gifticon, GifticonViewSet, UserGifticonViewSet
from store.views import StoreListView
from users.api import LogoutAPI, UserDetailAPI, RegisterAPI
from reviews.views import ReviewCreateView, ReviewListView, MyReviewListView
from rest_framework.routers import DefaultRouter
from users.views import CustomTokenObtainPairView, CustomTokenRefreshView

# DRF Router 설정
router = DefaultRouter()
router.register(r'gifticons', GifticonViewSet, basename='gifticon')
router.register(r'my-gifticons', UserGifticonViewSet, basename='user_gifticon')

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    
    # 인증 및 사용자 관련 API
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailAPI.as_view(), name='user_detail'),
    path('register/', RegisterAPI.as_view(), name='auth_register'),
    path('logout/', LogoutAPI.as_view(), name='auth_logout'),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # 마일리지 및 결제 관련 API
    path('register_card/', register_card, name='register_card'),
    path('my-mileage/', MileageListView.as_view(), name='mileage-list'),

    # 기프티콘 관련 API
    path('purchase/', purchase_gifticon, name='purchase_gifticon'),

    # 스토어 및 리뷰 관련 API
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('my-reviews/', MyReviewListView.as_view(), name='my-review-list'),
    path('all-reviews/', ReviewListView.as_view(), name='all-review-list'),

    # Gifticon 관련 ViewSet 연결
    path('api/', include(router.urls)),
]

