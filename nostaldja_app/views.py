from django.shortcuts import render, redirect
from .models import Decades, Fads
from .forms import DecadesForm, FadsForm

# Create your views here.

#Decades

def decade_list(req):
    decades = Decades.objects.all()
    return render(req, 'nostaldja/decade_list.html', {'decades': decades})

#----Read----
def decade_info(req, pk):
    decade = Decades.objects.get(id=pk)
    return render(req, 'nostaldja/decade_info.html', {'decade': decade})

#---Create---
def decade_create(req):
    if req.method == 'POST':
        form = DecadesForm(req.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_info', pk=decade.pk)
    else:
        form = DecadesForm()
    return render(req, 'nostaldja/decade_form.html', {'form': form})

#---Edit---
def decade_edit(req, pk):
    decade = Decades.objects.get(pk=pk)
    if req.method == "POST":
        form = DecadesForm(req.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_info', pk=decade.pk)
    else:
        form = DecadesForm(instance=decade)
    return render(req, 'nostaldja/decade_form.html', {'form': form})

#---Delete---
def decade_delete(req, pk):
    Decades.objects.get(id=pk).delete()
    return redirect('artist_list')
#Fads

def fad_list(req):
    fads = Fads.objects.all()
    return render(req, 'nostaldja/fad_list.html', {'fads': fads})

#----Read---
def fad_info(req, pk):
    fad = Fads.objects.get(id=pk)
    return render(req, 'nostaldja/fad_info.html', {'fad': fad})

#---Create---
def fad_create(req):
    if req.method == 'POST':
        form = FadsForm(req.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_info', pk=fad.pk)
    else:
        form = FadsForm()
    return render(req, 'nostaldja/fad_form.html', {'form': form})

#---Edit---
def fad_edit(req, pk):
    fad = Fads.objects.get(pk=pk)
    if req.method == "POST":
        form = FadsForm(req.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_info', pk=fad.pk)
    else:
        form = FadsForm(instance=fad)
    return render(req, 'nostaldja/fad_form.html', {'form': form})

#---Delete---
def fad_delete(req, pk):
    Fads.objects.get(id=pk).delete()
    return redirect('artist_list')