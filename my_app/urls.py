from django.urls import path
from .views import *

urlpatterns = [
    path("", product_list, name="product_list"),
path("<int:product_id>/", get_product_by_id, name="product_details")

]

