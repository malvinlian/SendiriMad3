"""SendiriMad3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.conf.urls import include, url  # < Django-2.0
from django.urls import include, path  # > Django-2.0
from django.contrib import admin
from oscar.app import application
from . import views

urlpatterns = [
    #url(r'^i18n/', include('django.conf.urls.i18n')),
     path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    #url(r'^admin/', admin.site.urls),
     path('admin/', admin.site.urls),  # > Django-2.0

    #url(r'', application.urls),
     path('', application.urls),  # > Django-2.0
     path('Home/', views.home, name='home'),
     path('OnSale/',views.OnSale, name='OnSale'),
     path('ArtisanOfTheMonth/',views.artisanofthemonth, name='artisanofthemonth'),
     path('FAQ/',views.faq, name='faq'),
     path('BecomeAnArtisan/',views.artisan, name='artisan'),
  
  
    #ShopsCategories
     path('HomeDecor/',views.homedecor, name='homedecor'),
     path('LifeStyle/',views.lifestyle, name='lifestyle'),
     path('Fashion/',views.fashion, name='fashion'),
     path('Jewelry/',views.jewelry, name='jewelry'),
     path('BeautyProduct/',views.beautyproduct, name='beautyproduct'),
     path('Music&Arts/',views.musicart, name='musicart'),
     path('Hobbies/',views.hobbies, name='hobbies'),
     path('Food&Beverages /',views.foodbeverages, name='foodbeverages'),
     path('Weddings/',views.weddings, name='weddings'),
     path('GiftIdeas/',views.giftideas, name='giftideas'), 
  
]