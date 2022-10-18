from django.urls import path
from numpy import insert
from . import views

urlpatterns = [
    path("categories",views.ListCategory.as_view(),name="categories"),
    path('categories/<int:pk>',views.DetailCategory.as_view(),name="singlecategory"),
    path("products",views.ListProduct.as_view(),name="Products"),
    path("products/<int:pk>",views.DetailProduct.as_view(),name="singleproduct"),
    path("blogs",views.ListBlog.as_view(),name="blogs"),
    path('blogs/<int:pk>',views.DetailBlog.as_view(),name="singleBlog"),
    path("register",views.register_request,name="register"),
    path("login",views.login_request,name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('addblog',views.add_blog,name='addblog'),
    path('',views.allblog,name='allblog'),
    path('editblog/<int:id>',views.editblog,name="editblog"),
    path("deleteblog/<int:id>",views.deleteblog,name="deleteblog"),
    path('profile',views.profile,name="profile"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('myblog',views.myblog,name='myblog')

]
    

