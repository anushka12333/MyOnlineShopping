from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="myonlineshop"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackerStatus"),
    path("products/<int:myid>",views.productview,name="ProductView"),
    path("search/",views.search,name="search"),
    path("checkout/",views.checkout,name="checkout"),

]
