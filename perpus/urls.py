"""
URL configuration for perpus project.

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
from django.urls import path
#apps from perpustakaan
from perpustakaan.views import buku
from perpustakaan.views import penerbit
from perpustakaan.views import tambah_buku
from perpustakaan.views import ubah_buku
from perpustakaan.views import hapus_buku

# ini views
# def buku(request):
#     return HttpResponse('Halaman Buku')

#Mendaftarkan route pada url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/',buku,name='buku'),
    path('penerbit/',penerbit),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>',hapus_buku,name='hapus_buku'),
]
