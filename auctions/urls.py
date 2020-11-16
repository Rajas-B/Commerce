from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("user/<str:username>", views.prof, name="prof"),
    path("categories", views.category, name="category"),
    path("createlisting", views.create, name="create"),
    path("product/<int:id>", views.prod1, name="prod1"),
    path("categories/<str:category>", views.categoryprods, name="categoryprods"),
    path("my_watchlist", views.watchlist, name="watchlist")
 ]
