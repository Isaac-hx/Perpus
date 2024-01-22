from django.shortcuts import render,redirect
from django.http import HttpResponse
#Mengimpor model 
from perpustakaan.models import Buku,Kelompok
#mengimpor formModel
from perpustakaan.forms import FormBuku



def hapus_buku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    return redirect('buku')

def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form =FormBuku(request.POST,instance=buku)
        if form.is_valid():
            form.save()
            return redirect('ubah_buku',id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        context = {
            'form':form,
            'buku':buku
        }
    return render(request,template,context )



# Create your views here.
def buku(request):


    #Melakukan queryset pada model Buku
    book = Buku.objects.all()
    #Melakukan queryset pada model Kelompok
    genre = Kelompok.objects.all()
    



    list_title = ["Sapiens","Machine Learning","Dunia Anna"]
    context = {
        "judul_heading" : "Ini adalah halaman buku",
        "judul" : "Dunia Sophie",
        "penulis" : "Jostein Gaarder",
        "list_judul" : list_title,
        "books" : book,
        "genre":genre
    }
    return render(request,'buku.html',context)


def penerbit(request):
    return HttpResponse("Halaman Penerbit")


def tambah_buku(request):
    response = False
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            response = True
            context = {
                'form':form,
                'response':response
                
                
            }
            return redirect('buku')
            # return render(request,'tambah-buku.html',context)
    
    #Mendefinisikan variabel form dengan value class FormBuku dari forms.py
    else :
        form = FormBuku()
        response = False
        context = {
            'form':form,
            'response':response
        }
        return render(request,'tambah-buku.html',context)