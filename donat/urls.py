from rest_framework.routers import DefaultRouter

from .views import DonationsDataViewSet, TopTenDonationsViewSet, EventViewSet

router = DefaultRouter()

router.register(r'event', EventViewSet, basename='event')
router.register(r'topten', TopTenDonationsViewSet, basename='toptendonations')
router.register(r'', DonationsDataViewSet, basename='donations')

urlpatterns = router.urls