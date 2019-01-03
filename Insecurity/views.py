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

def search(request):
    #import pdb; pdb.set_trace()
    if request.method == 'GET':
        search = request.GET.get('search_query')
#        import pdb; pdb.set_trace()

        with connection.cursor() as cursor:
        #    import pdb; pdb.set_trace()
            print(search)
            sql= 'Select * from InsecureModel where title="' + search + '"'
            print(sql)
            cursor.execute(sql)
            row=cursor.fetchone()
    return render(request,'results.html',context={'row':row})
