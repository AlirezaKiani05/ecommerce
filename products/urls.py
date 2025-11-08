from rest_framework.routers import DefaultRouter
from .views import CategortyViewSet,BrandViewSet,ProductViewSet

router = DefaultRouter()
router.register(r'category',CategortyViewSet,basename='categories')
router.register(r'brand',BrandViewSet,basename='brands')
router.register(r'product',ProductViewSet,basename='products')

urlpatterns = router.urls

