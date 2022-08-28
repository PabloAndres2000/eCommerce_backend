from rest_framework import routers

from pro_shop_backend.apps.products.api.views.product import ProductViewSet


router = routers.SimpleRouter()

router.register(r"products/product", ProductViewSet, basename="products")


urlpatterns = router.urls
