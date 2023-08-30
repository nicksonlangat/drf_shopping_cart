from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from cart.views import ProductAPI, CartAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', ProductAPI.as_view(), name='products'),
    path('cart', CartAPI.as_view(), name='cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
