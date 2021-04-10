from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import FigureCreateForm,FigureEditForm
from django.contrib.auth.decorators import permission_required
from .models import Figure


@login_required
def figure_list(request):
    object_list = Figure.objects.all()

    return render(request,'figures/figure/figure_list.html',{'figures':object_list})

@login_required
def figure_detail(request,id):
    figure = get_object_or_404(Figure, id=id)

    return render(request,'figures/figure/detail.html',{'figure':figure,'id':id})



@permission_required('auth.view_user')
def figure_create(request):
    if request.method == 'POST':
        form = FigureCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/objects')

    else:
        form = FigureCreateForm()

    return render(request,'figures/figure/figure_create_form.html',{'form':form})

@permission_required('auth.view_user')
def figure_edit(request,pk):
    if request.method == 'POST':
        figure = Figure.objects.get(id=pk)
        form = FigureEditForm(data=request.POST, files=request.FILES,instance=figure)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/objects')

    else:
        figure = Figure.objects.get(id=pk)
        form = FigureEditForm(instance=figure)

    return render(request,'figures/figure/figure_edit_form.html',{'form':form,'id':pk})

@permission_required('auth.view_user')
def figure_delete(request,pk):
    figure = Figure.objects.get(id=pk)
    figure.delete()
    return HttpResponseRedirect('/objects')
