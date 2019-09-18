from rest_framework.routers import DefaultRouter

from .views import DonationsDataViewSet, TopTenDonationsViewSet

router = DefaultRouter()

router.register(r'topten', TopTenDonationsViewSet, basename='toptendonations')
router.register(r'', DonationsDataViewSet, basename='donations')

urlpatterns = router.urls