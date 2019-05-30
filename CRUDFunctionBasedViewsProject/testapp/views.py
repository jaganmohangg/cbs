from django.shortcuts import render,redirect
from testapp.models import FBV_MODEL
from testapp.forms import FBV_FORM


# Create your views here
def retrive_view(request):
    employeesdata=FBV_MODEL.objects.all()
    return render(request,'testapp/home.html',{'employeesdata':employeesdata})

def create_view(request):
    form=FBV_FORM()
    if request.method=='POST':
        form=FBV_FORM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/create.html',{'form':form})
def delete_view(request,id):
    employeesdata=FBV_MODEL.objects.get(id=id)
    employeesdata.delete()
    return redirect('/')
def update_view(request,id):
    employeesdata=FBV_MODEL.objects.get(id=id)
    if request.method=='POST':
        form=FBV_FORM(request.POST,instance=employeesdata)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'employeesdata':employeesdata})
