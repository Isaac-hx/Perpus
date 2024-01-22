from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku


#Membuat sebuah Form default django
class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'


        #form widgets menambahkan attribute class 
        widgets={
            'judul':forms.TextInput({'class':'form-control'}),
            'penulis':forms.TextInput({'class':'form-control'}),
            'penerbit':forms.TextInput({'class':'form-control'}),
            'jumlah':forms.NumberInput({'class':'form-control'}),
            'kelompok':forms.Select({'class':'form-control'})

        }