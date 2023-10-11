"""
URL configuration for commodoresPizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from customer.views import Index, About, Menu, CarouselImage, PizzaQuiz, cart
from django.conf import settings
from django.conf.urls.static import static
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('menu/', Menu.as_view(), name='menu'),
    path('cart/', views.cart, name='cart'),
    path("add_to_cart", views.add_to_cart, name = "add_to_cart"),
    path('carousel/', CarouselImage.as_view(), name='view_carousel'),
    path('delete_cart_menu_item/<int:id>', views.deleteCartMenuItem, name='delete_cart_menu_item'),
    path('increase_quantity/<int:id>', views.increaseQuantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>', views.decreaseQuantity, name='decrease_quantity'),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('quiz/', PizzaQuiz.as_view(), name='quiz'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)