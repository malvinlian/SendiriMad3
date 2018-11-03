from django.shortcuts import render

# Create your views here.

def home(request):
  context = locals()
  template = 'promotions/home.html'
  return render(request,template,context)

def OnSale(request):
  context = locals()
  template = 'SendiriMade/onsale.html'
  return render(request,template,context)

def artisanofthemonth(request):
  context = locals()
  template = 'SendiriMade/artisanofthemonth.html'
  return render(request,template,context)

def faq(request):
  context = locals()
  template = 'SendiriMade/faq.html'
  return render(request,template,context)

def artisan(request):
  context = locals()
  template = 'SendiriMade/artisan.html'
  return render(request,template,context)


# Shops Categories View

def homedecor(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/homedecor.html'
  return render(request,template,context)

def lifestyle(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/lifestyle.html'
  return render(request,template,context)

def fashion(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/fashion.html'
  return render(request,template,context)

def jewelry(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/jewelry.html'
  return render(request,template,context)

def beautyproduct(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/beautyproduct.html'
  return render(request,template,context)

def musicart(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/musicart.html'
  return render(request,template,context)

def hobbies(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/hobbies.html'
  return render(request,template,context)

def foodbeverages(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/foodbeverages.html'
  return render(request,template,context)

def weddings(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/weddings.html'
  return render(request,template,context)


def giftideas(request):
  context = locals()
  template = 'SendiriMade/ShopCategories/giftideas.html'
  return render(request,template,context)









