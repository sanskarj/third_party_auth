from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import regform,searchingform,deleteform,updateform
from .models import Userinfo


# Create your views here.

from django.http import HttpResponse


def index(request):
    msg = "Registration Portal"
    if request.method=="POST":
        form  = regform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            q = Userinfo(name=info['Name'],email=info['email'],age=info['age'],mobile=info['mobile'],password=info['password'])
            q.save()
            return HttpResponseRedirect('/registration/thanks/0') 
    else:
        form = regform()
    return render(request,'registration/reg_form.html',{'form': form,'msg':msg,'flag':False,'id':0})

def message(request,flag):
    form =  searchingform()
    formdel = deleteform() 
    formupdate = updateform()
    if request.method == 'GET':
        form = searchingform(request.GET)
        
        if form.is_valid():

            url  = '../../detail/' + '0/'+ str(form.cleaned_data['id'])
            return HttpResponseRedirect(url)
   
    
    
    elif request.method =='POST':
        
        formdel = deleteform(request.POST)
        formupdate = updateform(request.POST)
        
        if formdel.is_valid() and flag=='1':
            url = '../../detail/' + '1/'+ str(formdel.cleaned_data['id'])
            return HttpResponseRedirect(url)
        if formupdate.is_valid() and flag=='2':
            url = '../../update/' + str(formupdate.cleaned_data['id'])
            return HttpResponseRedirect(url)
    
    
    return render(request,'registration/thanks.htm',{'form':form,'formdel':formdel,'formupdate':formupdate})
def detailview(request,flag,idnumber):
    if flag=='0':
        try:
            p = Userinfo.objects.get(id=int(idnumber))
            return render(request,'registration/detail.htm',{'user':p})
        except Exception as e:

            return HttpResponse(e)
    elif flag=='1':
        try:
            p = Userinfo.objects.get(id=int(idnumber))
            p.delete()
            return HttpResponse('The user with given id number has been deleted successfully')
        except Exception as e:
            return HttpResponse(e)
        


def entiredata(request):
    return render(request,'registration/database.htm',{'usercollection':Userinfo.objects.order_by('-id')})
def updatedata(request,idnumber):
    try:
        p = Userinfo.objects.get(id=int(idnumber))
        form = regform(initial={'Name':p.name,'email':p.email,'age':p.age,'mobile':p.mobile,'password':p.password})
        msg = "Change the info of the user with id " + idnumber
        return render(request,'registration/reg_form.html',{'form':form,'msg':msg,'id':idnumber,'flag':True})
    except Exception as e:
        return HttpResponse('User with id '+str(idnumber)+' does not exist')

    

    
    
     
    
    
    
