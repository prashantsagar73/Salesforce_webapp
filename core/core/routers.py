from rest_framework import routers
from sales.views import ContactViewSet
router = routers.SimpleRouter()

router.register(r'', ContactViewSet)
