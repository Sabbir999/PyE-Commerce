"""
Django URL Patterns for Routing Requests:

Functionality:
- Imports the necessary modules (`django.urls` and local `views` module) for defining URL patterns.
- Defines urlpatterns as a list of path() functions, mapping URL patterns to view functions.

URL Patterns:
- path('', views.home, name="home"): Maps the root URL ('/') to the home view function (`views.home`) with the name "home".
- path('register', views.register, name="register"): Maps '/register' URL to the register view function (`views.register`) with the name "register".
- path('login', views.login_page, name="login"): Maps '/login' URL to the login_page view function (`views.login_page`) with the name "login".
- path('logout', views.logout_page, name="logout"): Maps '/logout' URL to the logout_page view function (`views.logout_page`) with the name "logout".
- path('cart', views.cart_page, name="cart"): Maps '/cart' URL to the cart_page view function (`views.cart_page`) with the name "cart".
- path('fav', views.fav_page, name="fav"): Maps '/fav' URL to the fav_page view function (`views.fav_page`) with the name "fav".
- path('favviewpage', views.favviewpage, name="favviewpage"): Maps '/favviewpage' URL to the favviewpage view function (`views.favviewpage`) with the name "favviewpage".
- path('remove_fav/<str:fid>', views.remove_fav, name="remove_fav"): Maps '/remove_fav/<fid>' URL to the remove_fav view function (`views.remove_fav`) with the name "remove_fav".
- path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"): Maps '/remove_cart/<cid>' URL to the remove_cart view function (`views.remove_cart`) with the name "remove_cart".
- path('collections', views.collections, name="collections"): Maps '/collections' URL to the collections view function (`views.collections`) with the name "collections".
- path('collections/<str:name>', views.collectionsview, name="collections"): Maps '/collections/<name>' URL to the collectionsview view function (`views.collectionsview`) with the name "collections".
- path('collections/<str:cname>/<str:pname>', views.product_details, name="product_details"): Maps '/collections/<cname>/<pname>' URL to the product_details view function (`views.product_details`) with the name "product_details".
- path('addtocart', views.add_to_cart, name="addtocart"): Maps '/addtocart' URL to the add_to_cart view function (`views.add_to_cart`) with the name "addtocart".


"""

from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
]