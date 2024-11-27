from django.urls import path

from new_app import views

urlpatterns = [
    path("logi",views.logi,name="logi"),
    path("", views.index, name="index"),
    path("dash", views.dash, name="dash"),
    path("SellerR",views.SellerR,name="SellerR"),
    path("CustomerR",views.CustomerR,name="CustomerR"),
    path("login",views.Login_view,name="login"),
    path("blog",views.blog_posting,name="blog"),
    path("table",views.table,name="table"),
    path('rmv/<int:id>/',views.rmv, name="rmv"),
    path('update/<int:id>/',views.update,name="update"),

]
