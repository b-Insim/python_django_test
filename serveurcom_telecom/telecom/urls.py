from django.urls import path

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('references/', views.listing, name="listing"), # "telecom" will call the method "home" in "views.py"
    path('menu/', views.listing, name="listing"),
    path('references/<ref_id>', views.detail, name="detail"),
    path('search/', views.search, name="search"),
    # path('bars/', views.comptoir),
    # path('stock/<ID_COMPTOIR>/', views.stock),
]

app_name = 'telecom'