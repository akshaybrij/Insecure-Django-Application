from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
import os
from .forms import InsecureForm
from django.db.utils import OperationalError
from InsecureApp import settings
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

def search(request):
    #import pdb; pdb.set_trace()
    if request.method == 'GET':
        search = request.GET.get('search_query')
#        import pdb; pdb.set_trace()

        with connection.cursor() as cursor:
        #    import pdb; pdb.set_trace()
        #    print(search)
            sql= 'Select * from InsecureModel where title="' + search + '"'
        #    print(sql)
            try:
                cursor.execute(sql)
                row=list(cursor.fetchall())
            except OperationalError as e:
                #import pdb; pdb.set_trace()
                print(str(e))
                row=None
            source=[]
            if row != None:
                for r in row:
                #    print(r)
                    last= list(r)
                    source.append(last[-1])
            else:
                source=None
    print(source)
    return render(request,'results.html',context={'row':row, 'source':source})

def branch(request):
    pass

def extra_features(request):
    pass


