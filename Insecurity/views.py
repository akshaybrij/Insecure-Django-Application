from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from .forms import InsecureForm
def results(request):
    return render(request,'results.html',{})

def insecure_form_handling(request):
    if request.method=="POST":
        form=InsecureForm(request.POST,request.FILES)
       # import pdb;pdb.set_trace()
        if form.is_valid():
            print('request')
            form.save()
        return HttpResponseRedirect('/results')
    else:
        form = InsecureForm()
        return render(request,'form.html',context={'form':form})

def search(request,string):
    with connection.cursor() as cursor:
        cursor.execute('Select * from InsecureModel where title= %s',[string])
        row=cursor.fetchone()
    print(row)
